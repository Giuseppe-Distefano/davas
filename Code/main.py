import torch
import torch.nn as nn
import torch.nn.functional as F
from torchmetrics import Accuracy
from tqdm import tqdm

import os
import logging
import warnings
import random
import numpy as np
from parse_args import parse_arguments

from dataset import PACS
from models.resnet import BaseResNet18, ASHResNet18, DAResNet18

from globals import CONFIG

@torch.no_grad()
def evaluate(model, data):
    model.eval()

    acc_meter = Accuracy(task='multiclass', num_classes=CONFIG.num_classes)
    acc_meter = acc_meter.to(CONFIG.device)

    loss = [0.0, 0]
    for x, y in tqdm(data):
        with torch.autocast(device_type=CONFIG.device, dtype=torch.float16, enabled=True):
            x, y = x.to(CONFIG.device), y.to(CONFIG.device)
            logits = model(x)
            acc_meter.update(logits, y)
            loss[0] += F.cross_entropy(logits, y).item()
            loss[1] += x.size(0)

    accuracy = acc_meter.compute()
    loss = loss[0] / loss[1]
    logging.info(f'Accuracy: {100 * accuracy:.2f} - Loss: {loss}')
    # print(f'Accuracy: {100 * accuracy:.2f} - Loss: {loss} \n')


def train(model, data):
    # Create optimizers & schedulers
    optimizer = torch.optim.SGD(model.parameters(), weight_decay=0.0005, momentum=0.9, nesterov=True, lr=0.001)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=int(CONFIG.epochs * 0.8), gamma=0.1)
    scaler = torch.cuda.amp.GradScaler(enabled=True)

    # Load checkpoint (if it exists)
    cur_epoch = 0
    if os.path.exists(os.path.join('record', CONFIG.experiment_name, 'last.pth')):
        checkpoint = torch.load(os.path.join('record', CONFIG.experiment_name, 'last.pth'))
        cur_epoch = checkpoint['epoch']
        optimizer.load_state_dict(checkpoint['optimizer'])
        scheduler.load_state_dict(checkpoint['scheduler'])
        model.load_state_dict(checkpoint['model'])

    # Optimization loop
    for epoch in range(cur_epoch, CONFIG.epochs):
        model.train()

        for batch_idx, batch in enumerate(tqdm(data['train'])):
            
            # use a separate invocation of autocast for every forward pass.
            with torch.autocast(device_type=CONFIG.device, dtype=torch.float16, enabled=True):
                if CONFIG.experiment in ['domain_adaptation']:
                    # Register hook(s) to store the target domain activation maps and perform a forward pass
                    model.eval()
                    src_x, src_y, targ_x = batch
                    targ_x = targ_x.to(CONFIG.device)
                    module_placement = CONFIG.experiment_args['module_placement']
                    model.register_extract_activation_map_hooks(module_placement)
                    with torch.no_grad():
                        model(targ_x)
                    model.remove_extract_activation_map_hooks()
                    model.train()

            # Compute loss
            with torch.autocast(device_type=CONFIG.device, dtype=torch.float16, enabled=True):

                if CONFIG.experiment in ['baseline']:
                    x, y = batch
                    x, y = x.to(CONFIG.device), y.to(CONFIG.device)
                    loss = F.cross_entropy(model(x), y)
                elif CONFIG.experiment in ['random']:
                    x, y = batch
                    x, y = x.to(CONFIG.device), y.to(CONFIG.device)
                    # Randomly turn off some outputs of each layer 
                    module_placement = CONFIG.experiment_args['module_placement']
                    mask_out_ratio = CONFIG.experiment_args['mask_out_ratio']
                    if ('extension' in CONFIG.experiment_args) and (CONFIG.experiment_args['extension'] == 'no_binarization'):
                        model.register_random_activation_maps_hooks(module_placement, mask_out_ratio, binarize=False)
                    elif ('extension' in CONFIG.experiment_args) and (CONFIG.experiment_args['extension'] == 'top_k') and ('k_values' in CONFIG.experiment_args):
                        model.register_random_activation_maps_hooks(module_placement, mask_out_ratio, binarize=False, 
                                                                    top_k=True, k_values=CONFIG.experiment_args['k_values'])
                    else:
                        model.register_random_activation_maps_hooks(module_placement, mask_out_ratio)
                    loss = F.cross_entropy(model(x), y)
                    model.remove_random_activation_maps_hooks()
                elif CONFIG.experiment in ['domain_adaptation']:
                    src_x, src_y, targ_x = batch
                    src_x, src_y = src_x.to(CONFIG.device), src_y.to(CONFIG.device)
                    # Register the Activation Shaping hook(s) and perform a forward pass (source domain images)
                    if ('extension' in CONFIG.experiment_args) and (CONFIG.experiment_args['extension'] == 'no_binarization'):
                        model.register_activation_shaping_hooks(binarize=False)
                    elif ('extension' in CONFIG.experiment_args) and (CONFIG.experiment_args['extension'] == 'top_k') and ('k_values' in CONFIG.experiment_args):
                        model.register_activation_shaping_hooks(binarize=False, top_k=True, k_values=CONFIG.experiment_args['k_values'])
                    else:
                        model.register_activation_shaping_hooks()
                    loss = F.cross_entropy(model(src_x), src_y)
                    model.remove_activation_shaping_hooks()

            # Optimization step
            scaler.scale(loss / CONFIG.grad_accum_steps).backward()

            if ((batch_idx + 1) % CONFIG.grad_accum_steps == 0) or (batch_idx + 1 == len(data['train'])):
                scaler.step(optimizer)
                optimizer.zero_grad(set_to_none=True)
                scaler.update()

        scheduler.step()

        # Test current epoch
        logging.info(f'[TEST @ Epoch={epoch}]')
        evaluate(model, data['test'])

        # Save checkpoint
        checkpoint = {
            'epoch': epoch + 1,
            'optimizer': optimizer.state_dict(),
            'scheduler': scheduler.state_dict(),
            'model': model.state_dict()
        }
        torch.save(checkpoint, os.path.join('record', CONFIG.experiment_name, 'last.pth'))


def main ():
    # Load dataset
    data = PACS.load_data()

    # Load model
    if CONFIG.experiment in ['baseline']:
        model = BaseResNet18()
    elif CONFIG.experiment in ['random']:
        model = ASHResNet18()
    elif CONFIG.experiment in ['domain_adaptation']:
        # module_placement = CONFIG.experiment_args['module_placement']
        model = DAResNet18()

    model.to(CONFIG.device)

    if not CONFIG.test_only:
        train(model, data)
    else:
        evaluate(model, data['test'])


if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=UserWarning)

    # Parse arguments
    args = parse_arguments()
    print(args)
    CONFIG.update(vars(args))

    # Setup output directory
    CONFIG.save_dir = os.path.join('record', CONFIG.experiment_name)
    os.makedirs(CONFIG.save_dir, exist_ok=True)

    # Setup logging
    logging.basicConfig(
        filename=os.path.join(CONFIG.save_dir, 'log.txt'), 
        format='%(message)s', 
        level=logging.INFO, 
        filemode='a'
    )

    # Set experiment's device & deterministic behavior
    if CONFIG.cpu:
        CONFIG.device = torch.device('cpu')

    torch.manual_seed(CONFIG.seed)
    random.seed(CONFIG.seed)
    np.random.seed(CONFIG.seed)
    torch.backends.cudnn.benchmark = True
    torch.use_deterministic_algorithms(mode=True, warn_only=True)

    main()

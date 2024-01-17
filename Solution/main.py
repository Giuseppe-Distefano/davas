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
from models.resnet import BaseResNet18, ASHResNet18

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
            
            # Compute loss
            with torch.autocast(device_type=CONFIG.device, dtype=torch.float16, enabled=True):

                if CONFIG.experiment in ['baseline']:
                    x, y = batch
                    x, y = x.to(CONFIG.device), y.to(CONFIG.device)
                    loss = F.cross_entropy(model(x), y)
                ######################################################
                elif CONFIG.experiment in ['activation_shaping_last', 'activation_shaping_one', 'activation_shaping_three']:
                    x, y = batch
                    x, y = x.to(CONFIG.device), y.to(CONFIG.device)
                    loss = F.cross_entropy(model(x), y)
                elif CONFIG.experiment in ['random']:
                    x, y = batch
                    x, y = x.to(CONFIG.device), y.to(CONFIG.device)
                    loss = F.cross_entropy(model(x), y)

                ######################################################

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


def create_random_mask(layer_name = 'layer4.1.relu', mask_out_ratio = 0.0):

    layer_output_shapes = {
        'layer1.0.conv1': (64, 56, 56),
        'layer1.0.relu': (64, 56, 56),
        'layer1.0.conv2': (64, 56, 56),
        'layer1.1.conv1': (64, 56, 56),
        'layer1.1.bn1': (64, 56, 56),
        'layer1.1.relu': (64, 56, 56),
        'layer1.1.conv2': (64, 56, 56),
        'layer1.1.bn2': (64, 56, 56),
        'layer2.0.conv1': (128, 28, 28),
        'layer2.0.relu': (128, 28, 28),
        'layer2.0.conv2': (128, 28, 28),
        'layer2.1.conv1': (128, 28, 28),
        'layer2.1.relu': (128, 28, 28),
        'layer2.1.conv2': (128, 28, 28),
        'layer3.0.conv1': (256, 14, 14),
        'layer3.0.relu': (256, 14, 14),
        'layer3.0.conv2': (256, 14, 14),
        'layer3.1.conv1': (256, 14, 14),
        'layer3.1.relu': (256, 14, 14),
        'layer3.1.conv2': (256, 14, 14),
        'layer4.0.conv1': (512, 7, 7),
        'layer4.0.relu': (512, 7, 7),
        'layer4.0.conv2': (512, 7, 7),
        'layer4.1.conv1': (512, 7, 7),
        'layer4.1.relu': (512, 7, 7),
        'layer4.1.conv2': (512, 7, 7)
    }

    # create a mask tensor with a given ratio of zeros
    print('mask_out_ratio: ',mask_out_ratio)
    layer_output_shape = layer_output_shapes[layer_name]

    rand_mat = torch.rand(layer_output_shape).to(CONFIG.device)
    mask = torch.where(rand_mat <= mask_out_ratio, 0.0, 1.0).to(CONFIG.device)
    return mask
       
        
# def main(mask_out_ratio=0.4):
def main():    
    
    # Load dataset
    data = PACS.load_data()

    # Load model
    if CONFIG.experiment in ['baseline']:
        model = BaseResNet18()

    ######################################################
    
    elif CONFIG.experiment in ['activation_shaping_last']:
        model = ASHResNet18()
        model.define_network('ash_last', mask_out_ratio=0.1)
    elif CONFIG.experiment in ['activation_shaping_one']:
        model = ASHResNet18()
        model.define_network('ash_one', mask_out_ratio=0.1)
    elif CONFIG.experiment in ['activation_shaping_three']:
        model = ASHResNet18()
        model.define_network('ash_three', mask_out_ratio=0.1)

    elif CONFIG.experiment in ['random']:
        model = ASHResNet18()
        # module_placement = ['layer4.1.relu']
        # module_placement = ['layer3.1.conv2', 'layer4.0.conv2']
        module_placement = CONFIG.experiment_args['module_placement']
        mask_out_ratio = CONFIG.experiment_args['mask_out_ratio']

        for layer_name in module_placement:
            random_mask = create_random_mask(layer_name = layer_name, mask_out_ratio = mask_out_ratio)
            print('random_mask sum(): ', random_mask.sum())
            model.register_activation_shaping_hook(layer_name, random_mask)
        
        # model.define_network('ash_last', mask_out_ratio=mask_out_ratio)        

    ######################################################
    
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

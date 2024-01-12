import torch
import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights
from globals import CONFIG

class BaseResNet18(nn.Module):
    def __init__(self):
        super(BaseResNet18, self).__init__()
        self.resnet = resnet18(weights=ResNet18_Weights)
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, 7)

    def forward(self, x):
        return self.resnet(x)

######################################################

def get_activation_shaping_hook (mask):
    
    # Activation Shaping Module as a function that shall be hooked via 'register_forward_hook'
    def activation_shaping_hook(module, input, output):
        A_binary = torch.where(output<=0, torch.tensor(0.0), torch.tensor(1.0))
        M_binary = torch.where(mask<=0, torch.tensor(0.0), torch.tensor(1.0))
        
        shaped_output = A_binary * M_binary

        return shaped_output
    
    return activation_shaping_hook

######################################################

# 'BaseResNet18' including the Activation Shaping Module
class ASHResNet18(nn.Module):
    def __init__(self):
        super(ASHResNet18, self).__init__()
        self.resnet = resnet18(pretrained=False)
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, 7)


    def activation_shaping_hook (self, module, input, output):
        shaped_output = output * self.mask
        return shaped_output


    def define_network (self, net_name='ash_last', mask=None, mask_out_ratio=0.1):
        if mask is None:
            # Create a mask tensor with a given ratio of zeros
            rand_mat = torch.rand(512, 7, 7).to(CONFIG.device)
            self.mask_out_ratio = mask_out_ratio
            mask = torch.where(rand_mat <= self.mask_out_ratio, 0.0, 1.0).to(CONFIG.device)
        self.mask = mask

        if net_name=='ash_last': # ASH module after last convolutional layer
            hook = get_activation_shaping_hook(mask)
            #self.hook_handle = self.resnet.layer4[1].relu.register_forward_hook(hook)
            self.hook_handle = self.resnet.layer4[0].conv2.register_forward_hook(self.activation_shaping_hook)
        
        elif net_name=='ash_one': # ASH module after each convolutional layer
            self.hook_handles = []
            layers = [self.resnet.layer1, self.resnet.layer2, self.resnet.layer3, self.resnet.layer4]
            for layer in layers:
                for module in layer.children():
                    if isinstance(module, nn.Conv2d):
                        hook = get_activation_shaping_hook(mask)
                        hook_handle = module.register_forward_hook(hook)
                        self.hook_handles.append(hook_handle)
        
        elif net_name=='ash_three': # ASH module after every three convolutional layers
            self.hook_handles = []
            layers = [self.resnet.layer1, self.resnet.layer2, self.resnet.layer3, self.resnet.layer4]
            for i, layer in enumerate(layers):
                for module in layer.children():
                    if isinstance(module, nn.Conv2d):
                        if (i%3 == 0):
                            hook = get_activation_shaping_hook(mask)
                            hook_handle = module.register_forward_hook(hook)
                            self.hook_handles.append(hook_handle)

    
    def register_activation_shaping_hook(self, layer_name = 'layer4.1.relu', mask_out_ratio = 0.0):
        self.layer_name = layer_name
        self.mask_out_ratio = mask_out_ratio

        # create a mask tensor with a given ratio of zeros
        print('self.mask_out_ratio: ', self.mask_out_ratio)
        rand_mat = torch.rand(512, 7, 7).to(CONFIG.device)
        mask = torch.where(rand_mat <= self.mask_out_ratio, 0.0, 1.0).to(CONFIG.device)

        hook = get_activation_shaping_hook(mask)
        # penultimate_layer = self.resnet.layer4[1].bn2
        # self.hook_handle = penultimate_layer.register_forward_hook(hook)

        for name, module in self.resnet.named_modules():
          if (isinstance(module, nn.ReLU) and name == self.layer_name):
            print('Insert activation shaping layer after ', name, module)
            self.hook_handle = module.register_forward_hook(hook)

    
    def remove_activation_shaping_hook (self):
        if self.hook_handle is not None:
            self.hook_handle.remove()

    
    def remove_activation_shaping_hooks (self):
        if self.hook_handles is not None:
            for hook_handle in self.hook_handles:
                hook_handle.remove()


    def forward(self, x):
        return self.resnet(x)

######################################################

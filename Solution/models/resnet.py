import torch
import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights
## from globals import CONFIG

class BaseResNet18(nn.Module):
    def __init__(self):
        super(BaseResNet18, self).__init__()
        self.resnet = resnet18(weights=ResNet18_Weights)
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, 7)

    def forward(self, x):
        return self.resnet(x)

######################################################

# 'BaseResNet18' including the Activation Shaping Module
class ASHResNet18(nn.Module):
    def __init__(self):
        super(ASHResNet18, self).__init__()
        self.resnet = resnet18(weights=ResNet18_Weights)
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, 7)

        self.hook_handles = {}

    def get_random_activation_map_hook(self, mask_out_ratio):
        
        # Activation Shaping Module as a function that shall be hooked via 'register_forward_hook'
        # The hook captures the mask_out_ratio from the parent scope
        
        def random_activation_map_hook(module, input, output):
            # create a mask tensor with a given ratio of zeros
            print('mask_out_ratio: ', mask_out_ratio)
            rand_mat = torch.rand_like(output)
            mask = torch.where(rand_mat <= mask_out_ratio, 0.0, 1.0)
            print('random_mask sum(): ', mask.sum())
            
            # binarize both activation map and mask using zero as threshold
            A_binary = torch.where(output<=0, 0.0, 1.0)
            M_binary = torch.where(mask<=0, 0.0, 1.0)
            
            # return the element-wise product of activation map and mask
            shaped_output = A_binary * M_binary
            return shaped_output
        
        return random_activation_map_hook
            
    def register_random_activation_maps_hooks(self, module_placement, mask_out_ratio):
        for layer_name, module in self.resnet.named_modules():
            # if (isinstance(module, nn.Conv2d) and layer_name in module_placement):
            if ((isinstance(module, nn.ReLU) or isinstance(module, nn.Conv2d)) and layer_name in module_placement):
                print('Register a hook to perform Random Maps Ablation on layer ', layer_name, module)
                hook = self.get_random_activation_map_hook(mask_out_ratio)
                self.hook_handles[layer_name] = module.register_forward_hook(hook)

    def remove_random_activation_maps_hooks(self):
        for layer_name, handle in self.hook_handles.items():
            print('Remove the hook used to perform Activation Shaping on layer ', layer_name)
            handle.remove()

    def forward(self, x):
        return self.resnet(x)
    
######################################################
    
# 'BaseResNet18' including the Activation Shaping Module for Domain Adaptation
class DAResNet18(nn.Module):
    def __init__(self, module_placement=None):
        super(DAResNet18, self).__init__()
        self.resnet = resnet18(weights=ResNet18_Weights)
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, 7)

        self.activation_maps = {}
        self.activation_map_hook_handles = {}
        self.activation_shaping_hook_handles = {}

    def get_extract_activation_map_hook(self, layer_name):
        def extract_activation_map_hook(module, input, output):
            self.activation_maps[layer_name] = output.detach().clone()
        return extract_activation_map_hook
    
    def get_activation_shaping_hook (self, mask):
        # Activation Shaping Module as a function that shall be hooked via 'register_forward_hook'
        # The hook captures mask variable from the parent scope, to update it,
        # remove() the hook and register a new one with the updated mask.
        
        def activation_shaping_hook(module, input, output):
            # print('ASH module registered on: ', module, 'mask shape: ', mask.shape, 'mask sum(): ', mask.sum())
            
            # binarize both activation map and mask using zero as threshold
            A_binary = torch.where(output<=0, 0.0, 1.0)
            M_binary = torch.where(mask<=0, 0.0, 1.0)
            
            # return the element-wise product of activation map and mask
            shaped_output = A_binary * M_binary
            return shaped_output
        
        return activation_shaping_hook

    def register_extract_activation_map_hooks(self, module_placement):
        # Register hook(s) (1st hook) to store activation map
        for layer_name, module in self.resnet.named_modules():
            if (isinstance(module, nn.Conv2d) and layer_name in module_placement):
                print('Register a hook (1st) to store activation map of layer ', layer_name, module)
                hook = self.get_extract_activation_map_hook(layer_name)
                self.activation_map_hook_handles[layer_name] = module.register_forward_hook(hook)

    def remove_extract_activation_map_hooks(self):
        # Remove hook(s) used to store activation map
        for layer_name, handle in self.activation_map_hook_handles.items():
            print('Remove the hook used to store activation map of layer ', layer_name)
            handle.remove()
            
    def register_activation_shaping_hooks(self):
        # Register the Activation Shaping Module hook(s) (2nd hook)
        for layer_name, module in self.resnet.named_modules():
            if (isinstance(module, nn.Conv2d) and layer_name in self.activation_maps):
                print('Register a hook (2nd) to perform Activation Shaping on layer ', layer_name, module)
                hook = self.get_activation_shaping_hook(self.activation_maps[layer_name])
                self.activation_shaping_hook_handles[layer_name] = module.register_forward_hook(hook)

    def remove_activation_shaping_hooks(self):
        # Remove hook(s) used to perform Activation Shaping
        for layer_name, handle in self.activation_shaping_hook_handles.items():
            print('Remove the hook used to perform Activation Shaping on layer ', layer_name)
            handle.remove()
    
    def forward(self, x):
        return self.resnet(x)
    

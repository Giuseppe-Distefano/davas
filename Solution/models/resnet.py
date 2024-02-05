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

def get_activation_shaping_hook (mask):

    # Activation Shaping Module as a function that shall be hooked via 'register_forward_hook'
    # The hook captures mask variable from the parent scope, to update it,
    # remove() the hook and register a new one with the updated mask.

    def activation_shaping_hook(module, input, output):

        # print('ASH module registered on: ', module, 'mask shape: ', mask.shape, 'mask sum(): ', mask.sum())

        # binarize both activation map and mask using zero as threshold
        A_binary = torch.where(output<=0, torch.tensor(0.0), torch.tensor(1.0))
        M_binary = torch.where(mask<=0, torch.tensor(0.0), torch.tensor(1.0))

        # return the element-wise product of activation map and mask
        shaped_output = A_binary * M_binary
        return shaped_output

    return activation_shaping_hook

######################################################

# 'BaseResNet18' including the Activation Shaping Module
class ASHResNet18(nn.Module):
    def __init__(self):
        super(ASHResNet18, self).__init__()
        self.resnet = resnet18(weights=ResNet18_Weights)
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, 7)

        self.hook_handles = {}

    def register_activation_shaping_hook(self, layer_name, mask):
        hook = get_activation_shaping_hook(mask)

        for name, module in self.resnet.named_modules():
            if (isinstance(module, nn.Conv2d) and name == layer_name):
                if not name in self.hook_handles:
                    print('Insert activation shaping layer after ', name, module)
                    self.hook_handles[name] = module.register_forward_hook(hook)

    def remove_activation_shaping_hook(self, name):
        if name in self.hook_handles and self.hook_handles[name] is not None:
            handle = self.hook_handles[name]
            handle.remove()

    def forward(self, x):
        return self.resnet(x)
    
######################################################
    
# 'BaseResNet18' including the Activation Shaping Module for Domain Adaptation
class ASHResNet18DomainAdaptation(nn.Module):
    def __init__(self, module_placement=None):
        super(ASHResNet18DomainAdaptation, self).__init__()
        self.resnet = resnet18(weights=ResNet18_Weights)
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, 7)

        self.module_placement = module_placement
        if module_placement==[]:
            self.module_placement = None
        self.activation_maps = {}
        self.activation_map_hook_handles = {}
        self.activation_shaping_hook_handles = {}

    def get_extract_activation_map_hook(self, layer_name):
        def extract_activation_map_hook(module, input, output):
            self.activation_maps[layer_name] = output.clone().detach()
        return extract_activation_map_hook
    
    '''
    def get_extract_activation_map_hook2 (self, layer_name):
        def extract_activation_map_hook(module, input, output):
            A = torch.where(output<=0, torch.tensor(0.0), torch.tensor(1.0))
            M = self.activation_maps[layer_name]
            A = torch.where(M<=0, torch.tensor(0.0), torch.tensor(1.0))
            shaped_output = A * M
            return shaped_output
        return extract_activation_map_hook
    '''

    def forward(self, x, targ_x=None):
        if (targ_x is not None) and (self.module_placement is not None):
            # Register hook(s) (1st hook) to store activation map ...
            for layer_name, module in self.resnet.named_modules():
                if (isinstance(module, nn.Conv2d) and layer_name in self.module_placement):
                    print('Register a hook (1st) to store activation map of layer ', layer_name, module)
                    hook = self.get_extract_activation_map_hook(layer_name)
                    self.activation_map_hook_handles[layer_name] = module.register_forward_hook(hook)
            # ... and perform a forward pass to actually store the target domain activation maps
            _ = self.resnet(targ_x)
            
            # Remove hooks
            for layer_name, handle in self.activation_map_hook_handles.items():
                print('Remove the hook used to store activation map of layer ', layer_name, module)
                handle.remove()
            
            # Register the Activation Shaping Module hook(s) (2nd hook) ...
            for layer_name, module in self.resnet.named_modules():
                if (isinstance(module, nn.Conv2d) and layer_name in self.activation_maps):
                    print('Register a hook (2nd) to perform Activation Shaping on layer ', layer_name, module)
                    hook = get_activation_shaping_hook(self.activation_maps[layer_name])
                    self.activation_shaping_hook_handles[layer_name] = module.register_forward_hook(hook)
            # ... and perform a forward pass (source domain images)
            out = self.resnet(x)
            
            # Remove hooks
            for layer_name, handle in self.activation_shaping_hook_handles.items():
                print('Remove the hook used to perform Activation Shaping on layer ', layer_name, module)
                handle.remove()
                
        if (targ_x is not None) and (self.module_placement is not None):
            return out
        else:
            return self.resnet(x)

    '''
    def forward(self, x, targ_x=None):
        if targ_x is not None: # First step for point 3
            if self.module_placement is not None:
                # Register a hook and perform a forward pass to store the target domain activation maps
                for layer_name, module in self.resnet.named_modules():
                    if (isinstance(module, nn.Conv2d) and layer_name in self.module_placement):
                        #print('Register a hook to store activation map of layer ', layer_name, module)
                        hook = self.get_extract_activation_map_hook1(layer_name)
                        self.activation_map_hook_handles[layer_name] = module.register_forward_hook(hook)
                _ = self.resnet(targ_x)
        else: # Second step for point 3
            if self.module_placement is not None:
                # Register a hook and perform a forward pass to compute source labels
                for layer_name, module in self.resnet.named_modules():
                    if (isinstance(module, nn.Conv2d) and layer_name in self.module_placement):
                        #print('Register a hook to store activation map of layer ', layer_name, module)
                        hook = self.get_extract_activation_map_hook2(layer_name)
                        self.activation_map_hook_handles[layer_name] = module.register_forward_hook(hook)
        output = self.resnet(x)

        return output
    '''
    
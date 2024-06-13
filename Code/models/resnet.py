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

# 'BaseResNet18' including the Activation Shaping Module for Random Maps Ablation
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

    def get_random_activation_map_hook_no_binarization(self, mask_out_ratio):
        
        # do not binarize the activation map produced by the current layer.
        
        def random_activation_map_hook_no_binarization(module, input, output):
            # create a mask tensor with a given ratio of zeros
            print('mask_out_ratio: ', mask_out_ratio)
            rand_mat = torch.rand_like(output)
            mask = torch.where(rand_mat <= mask_out_ratio, 0.0, 1.0)
            print('random_mask sum(): ', mask.sum())
            
            # return the element-wise product of activation map and mask
            A = output.detach()
            shaped_output = A * mask
            return shaped_output
        
        return random_activation_map_hook_no_binarization

    def get_random_activation_map_hook_top_k(self, mask_out_ratio, k):
        
        # Binarize the mask M, compute the Top K values of the activation map A and 
        # set all the elements of M that are not in the Top K to zero. Then, multiply A and M
        
        def random_activation_map_hook_top_k(module, input, output):
            print('mask_out_ratio: ', mask_out_ratio, 'activation map size: ', output.size(), 'k: ', k)

            # create a mask tensor with a given ratio of zeros
            rand_mat = torch.rand_like(output)
            mask = torch.where(rand_mat <= mask_out_ratio, 0.0, 1.0)
            print('random_mask sum(): ', mask.sum())
            
            # binarize both activation map and mask using zero as threshold
            # A_binary = torch.where(output<=0, 0.0, 1.0)
            # M_binary = torch.where(mask<=0, 0.0, 1.0)
            
            A = output.detach()
            A_flat = A.reshape(*A.shape[:-2],-1)
            # Compute the actual value of k given the shape of the activation map
            actual_k_value = int(k*A_flat.shape[-1])
            print(f'actual_k_value: {actual_k_value}')

            # If largest is False then the k smallest elements are returned.
            _, indices = torch.topk(A_flat, k=A_flat.shape[-1] - actual_k_value, largest=False)
            
            # Set all the elements of M that are not in the Top K to zero
            M_flat = mask.reshape(*mask.shape[:-2],-1)
            M_flat.scatter_(2, indices, 0.0)
            M = M_flat.reshape(*mask.shape)
            
            # return the element-wise product of activation map and mask
            # shaped_output = A * M
            return output * M
            # return shaped_output
        
        return random_activation_map_hook_top_k
    
    def get_k(self, layer_name, k_values):
        stage=int(layer_name.split('.')[0].replace('layer','')) -1
        return k_values[stage]
    
    def register_random_activation_maps_hooks(self, module_placement, mask_out_ratio, binarize=True, top_k=False, k_values=None):
        for layer_name, module in self.resnet.named_modules():
            if ((isinstance(module, nn.ReLU) or isinstance(module, nn.Conv2d) or isinstance(module, nn.BatchNorm2d))):
                if layer_name in module_placement:
                    print(f'Register a hook to perform Random Maps Ablation on layer {layer_name} Binarize (both): {binarize} Top-K: {top_k}')
                    if binarize:
                        hook = self.get_random_activation_map_hook(mask_out_ratio)
                    else:
                        if not top_k:
                            hook = self.get_random_activation_map_hook_no_binarization(mask_out_ratio)
                        else:
                            k = self.get_k(layer_name, k_values)
                            hook = self.get_random_activation_map_hook_top_k(mask_out_ratio, k)
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

    def get_activation_shaping_hook_no_binarization (self, mask):
        
        # Instead of binarizing the mask, keep it as it is and simply multiply it with the activation map produced by the current layer 
        
        def activation_shaping_hook_no_binarization(module, input, output):
            # print('ASH module registered on: ', module, 'mask shape: ', mask.shape, 'mask sum(): ', mask.sum())
            
            # return the element-wise product of activation map and mask
            A = output.detach()
            shaped_output = A * mask
            return shaped_output
        
        return activation_shaping_hook_no_binarization

    def get_activation_shaping_hook_top_k(self, mask, k):
        
        # Binarize the mask M, compute the Top K values of the activation map A and 
        # set all the elements of M that are not in the Top K to zero. Then, multiply A and M
        
        def activation_shaping_hook_top_k(module, input, output):
            print('activation map size: ', output.size(), 'k: ', k)
            
            # binarize the mask using zero as threshold
            M_binary = torch.where(mask<=0, 0.0, 1.0)
            
            A = output.detach()
            A_flat = A.reshape(*A.shape[:-2],-1)
            # Compute the actual value of k given the shape of the activation map
            actual_k_value = int(k*A_flat.shape[-1])
            print(f'actual_k_value: {actual_k_value}')
            # If largest is False then the k smallest elements are returned.
            _, indices = torch.topk(A_flat, k=A_flat.shape[-1] - actual_k_value, largest=False)
            
            # Set all the elements of M that are not in the Top K to zero
            M_flat = M_binary.reshape(*M_binary.shape[:-2],-1)
            M_flat.scatter_(2, indices, 0.0)
            M = M_flat.reshape(*M_binary.shape)
            
            # return the element-wise product of activation map and mask
            # shaped_output = A * M
            return output * M
            # return shaped_output
        
        return activation_shaping_hook_top_k
    
    def register_extract_activation_map_hooks(self, module_placement):
        # Register hook(s) (1st hook) to store activation map
        for layer_name, module in self.resnet.named_modules():
            if ((isinstance(module, nn.ReLU) or isinstance(module, nn.Conv2d) or isinstance(module, nn.BatchNorm2d))):
                if layer_name in module_placement:
                    print('Register a hook (1st) to store activation map of layer ', layer_name, module)
                    hook = self.get_extract_activation_map_hook(layer_name)
                    self.activation_map_hook_handles[layer_name] = module.register_forward_hook(hook)

    def remove_extract_activation_map_hooks(self):
        # Remove hook(s) used to store activation map
        for layer_name, handle in self.activation_map_hook_handles.items():
            print('Remove the hook used to store activation map of layer ', layer_name)
            handle.remove()

    def get_k(self, layer_name, k_values):
        stage=int(layer_name.split('.')[0].replace('layer','')) -1
        return k_values[stage]
    
    def register_activation_shaping_hooks(self, binarize=True, top_k=False, k_values=None):
        # Register the Activation Shaping Module hook(s) (2nd hook)
        for layer_name, module in self.resnet.named_modules():
            if ((isinstance(module, nn.ReLU) or isinstance(module, nn.Conv2d) or isinstance(module, nn.BatchNorm2d))):
                if layer_name in self.activation_maps:
                    print(f'Register a hook (2nd) to perform Activation Shaping on layer {layer_name} Binarize (both): {binarize} Top-K: {top_k}')
                    if binarize:
                        hook = self.get_activation_shaping_hook(self.activation_maps[layer_name])
                    else:
                        if not top_k:
                            hook = self.get_activation_shaping_hook_no_binarization(self.activation_maps[layer_name])
                        else:
                            k = self.get_k(layer_name, k_values)
                            hook = self.get_activation_shaping_hook_top_k(self.activation_maps[layer_name], k)
                    self.activation_shaping_hook_handles[layer_name] = module.register_forward_hook(hook)

    def remove_activation_shaping_hooks(self):
        # Remove hook(s) used to perform Activation Shaping
        for layer_name, handle in self.activation_shaping_hook_handles.items():
            print('Remove the hook used to perform Activation Shaping on layer ', layer_name)
            handle.remove()
    
    def forward(self, x):
        return self.resnet(x)
    

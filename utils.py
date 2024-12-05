import importlib.util
import sys
import random
import numpy as np
import torch

def seed_everything(seed=42):
    """
    Set seed for reproducibility across random modules and libraries.
    
    Args:
        seed (int): The seed value to set. Default is 42.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def import_filename(filepath):
    """
    Dynamically import a Python file as a module.
    
    Args:
        filepath (str): Path to the Python file.
        
    Returns:
        module: Imported module object.
    """
    module_name = filepath.split("/")[-1].rstrip(".py")
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

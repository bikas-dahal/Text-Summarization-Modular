import os 
from box.exceptions import BoxValueError 
from textSummarizer.logging import logger 
from ensure import ensure_annotations 
from box import ConfigBox 
from pathlib import Path 
from typing import Any 
import yaml

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    Read a yaml file and return a ConfigBox object
    
    Args:
    path_to_yaml: Path: Path to the yaml file
    
    Raises:
    BoxValueError: If the yaml file is not found
    e: empty file 
    
    Returns:
    ConfigBox: ConfigBox object
    
    '''
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'Yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('The YAML file is empty')
    except Exception as e:
        raise e 
    

@ensure_annotations 
def create_directories(path_to_directories: list, verbose=True):
    '''
    Create directories if they do not exist
    
    Args:
    path_to_directories: list: List of directories to be created
    verbose: bool: Print the directories created
    
    '''
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Directory created: {path}')
            
            

@ensure_annotations
def get_size(path: Path) -> str:
    '''
    Get the size of a file
    
    Args:
    path: Path: Path to the file
    
    Returns:
    str: Size of the file
    
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'


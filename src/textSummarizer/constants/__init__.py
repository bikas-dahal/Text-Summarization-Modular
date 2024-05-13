from pathlib import Path 
import os 

CONFIG_FILE_PATH = Path('config/config.yaml')
PARAMS_FILE_PATH = Path('params.yaml')


print(CONFIG_FILE_PATH)

if CONFIG_FILE_PATH.exists():
    with open(CONFIG_FILE_PATH, 'r') as f:
        print(f.read())
else:
    print("Config file does not exist.")

# import os
# import yaml
# from pathlib import Path

# # Define the path to your config file
# CONFIG_FILE_PATH = Path('config/config.yaml')

# # Check if the file exists
# if CONFIG_FILE_PATH.exists():
#     # Read data from the existing config file
#     with open(CONFIG_FILE_PATH, 'r') as f:
#         config_data = yaml.safe_load(f)
#         print("Existing config data:")
#         print(config_data)
# else:
#     # Create a new config file and write some initial data
#     initial_config = {
#         'project_name': 'My Project',
#         'variable_list': [1, 2, 3],
#         'boolean': True
#     }
#     with open(CONFIG_FILE_PATH, 'w') as f:
#         yaml.dump(initial_config, f)
#     print("New config file created with initial data.")

# You can now modify or use the config_data as needed!

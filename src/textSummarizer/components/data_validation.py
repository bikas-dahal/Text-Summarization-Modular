import os 
from textSummarizer.logging import logger 
from textSummarizer.entity import DataValidationConfig

class DataValidation: 
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_files_exist(self) -> bool: 
        try: 
            validation_status = None 
            
            all_files = os.listdir(os.path.join('artifacts', 'data_ingestion', 'samsum_dataset'))
            
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False 
                    with open(self.config.STATUS_FILE, 'w') as f: 
                        f.write(f'{file} is missing')
                else: 
                    validation_status = True 
                    with open(self.config.STATUS_FILE, 'w') as f: 
                        f.write('All files are present')
                        
            return validation_status
        
        except Exception as e:
            logger.error(f'Error in validate_all_files_exist: {e}')
            raise e 
        
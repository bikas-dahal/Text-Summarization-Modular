from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger 

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> Stage {STAGE_NAME} completed.. <<<<<')
except Exception as e:
    logger.error(f'Error in {STAGE_NAME} stage: {str(e)}')
    raise e



STAGE_NAME = 'Data Validation stage'

try:
    logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<<')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>> Stage {STAGE_NAME} completed.. <<<<<')
except Exception as e:
    logger.error(f'Error in {STAGE_NAME} stage: {str(e)}')
    raise e
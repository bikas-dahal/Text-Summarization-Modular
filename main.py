from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
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
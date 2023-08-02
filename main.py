from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# logger.info('Custom Logging')
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<< \n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e
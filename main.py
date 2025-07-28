from src.ML_Project_w_MLFlow import logger
from src.ML_Project_w_MLFlow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME= "Data Ingestion Stage"



try:
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started<<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"completed")
except Exception as e:
        logger.exception(e)
        raise e
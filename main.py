from src.ML_Project_w_MLFlow import logger
from src.ML_Project_w_MLFlow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ML_Project_w_MLFlow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.ML_Project_w_MLFlow.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline


STAGE_NAME= "Data Ingestion Stage"



try:
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started<<<<<<<<<")
        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f"completed")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation Stage"

try:
      logger.info(f">>>>>>Stage {STAGE_NAME}<<<<<<<<")
      obj = DataValidationTrainingPipeline()
      obj.main()
      logger.info(f">>>>>>>>>> {STAGE_NAME} completed")

except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Data Transformation Stage"

try:
      logger.info(f">>>>>>Stage {STAGE_NAME}<<<<<<<<")
      data_transformation= DataTransformationTrainingPipeline()
      data_transformation.main()
      logger.info(f">>>>>>>>>> {STAGE_NAME} completed")

except Exception as e:
      logger.exception(e)
      raise e
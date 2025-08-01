from src.ML_Project_w_MLFlow import logger
from src.ML_Project_w_MLFlow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ML_Project_w_MLFlow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.ML_Project_w_MLFlow.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.ML_Project_w_MLFlow.pipeline.stage_04_manager_trainer import ModelTrainertrainingPipeline
from src.ML_Project_w_MLFlow.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

import os

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/zeynepzeytun.2002/MLFlow.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "zeynepzeytun.2002"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "ac89574523f379583a7e25f934daca9ce4763e0e"


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



STAGE_NAME = "Model Trainer Stage"

try: 
       logger.info(f">>>>>{STAGE_NAME} started <<<<<<")
       data_ingestion = ModelTrainertrainingPipeline()
       data_ingestion.main()
       logger.info(f" {STAGE_NAME} is over")

except Exception as e:
       logger.exception(e)
       raise e


STAGE_NAME = "Model Evaluation Stage"

try:
       logger.info(f">>>>{ STAGE_NAME}<<<<<")
       data_ingestion = ModelEvaluationTrainingPipeline()
       data_ingestion.main()
       logger.info(f">>>>> {STAGE_NAME} bitti<<<<<")

except Exception as e:
      logger.exception(e)
      raise e

       
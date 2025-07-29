from src.ML_Project_w_MLFlow.config.configuration import ConfigurationManager
from src.ML_Project_w_MLFlow.components.data_validation import DataValidation
from src.ML_Project_w_MLFlow import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
     
     config= ConfigurationManager()
     data_validation_config = config.get_data_validation_config()
     data_validation = DataValidation(config=data_validation_config)
     data_validation.validate_all_columns()



if __name__ == '__main__':
   
   try:
      logger.info(f">>>>>>Stage {STAGE_NAME}<<<<<<<<")
      obj = DataValidationTrainingPipeline()
      obj.main()
      logger.info(f">>>>>>>>>> {STAGE_NAME} completed")

   except Exception as e:
      logger.exception(e)
      raise e
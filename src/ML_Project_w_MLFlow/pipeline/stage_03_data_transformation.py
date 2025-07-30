from src.ML_Project_w_MLFlow.config.configuration import ConfigurationManager
from src.ML_Project_w_MLFlow.components.data_validation import DataValidation
from src.ML_Project_w_MLFlow import logger
from src.ML_Project_w_MLFlow.components.data_transformation import DataTransformation
from pathlib import Path


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt") , "r") as f:
              status = f.read().strip()

            if status.endswith("True"):
                print(f"its working")
                config= ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.train_test_spliting()
            
            elif status.endswith("False"):
                print(f"it is not working")
                raise Exception("data schema is not valid")


            else :
               
               print(f"what hell is that : {status}")


        except Exception as e:
          raise e
        

if __name__ =='__main__':


  try:
      logger.info(f">>>>>>Stage {STAGE_NAME}<<<<<<<<")
      obj = DataTransformationTrainingPipeline()
      obj.main()
      logger.info(f">>>>>>>>>> {STAGE_NAME} completed")

  except Exception as e:
      logger.exception(e)
      raise e
from src.ML_Project_w_MLFlow.config.configuration import ConfigurationManager
from src.ML_Project_w_MLFlow.components.model_evaluation import ModelEvaluation
from src.ML_Project_w_MLFlow import logger


STAGE_NAME="Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
         config = ConfigurationManager()
         model_evaluation_config = config.get_model_evaluation_config()
         model_evaluation_config =ModelEvaluation(config=model_evaluation_config)
         model_evaluation_config.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>{ STAGE_NAME}<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME}<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
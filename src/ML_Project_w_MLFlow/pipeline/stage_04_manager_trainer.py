from src.ML_Project_w_MLFlow.config.configuration import ConfigurationManager
from src.ML_Project_w_MLFlow.components.model_trainer import ModelTrainer
from src.ML_Project_w_MLFlow import logger


STAGE_NAME= "Model Trainer Stage"


class ModelTrainertrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME}<<<<<<<< started")
        obj = ModelTrainertrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")

    
    except Exception as e:
        logger.exception(e)
        raise e
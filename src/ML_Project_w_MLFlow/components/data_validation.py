import os
from src.ML_Project_w_MLFlow import logger
from src.ML_Project_w_MLFlow.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(
            self,
            config:DataValidationConfig
    ):
        self.config=config


    def validate_all_columns(self)->bool:
        try:
            validation_status:None

            data=pd.read_csv(self.config.unzip_data_dir)
            all_cols=list(data.columns)

            all_schema= self.config.all_schema.keys()


            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Val status: {validation_status}")
                
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"val status: {validation_status} ")

            return validation_status
        

        except Exception as e:
            raise e
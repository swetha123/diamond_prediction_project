import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.logger import logging 
from src.DimondPricePrediction.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")




class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))
            logging.info("read the data as dataframe")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("saving the raw data in artifacts folder")

            train_data,test_data = train_test_split(data,test_size=0.25)
            logging.info("train test data split")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("data ingestion part is completed")

        except Exception as e:
            logging.info("exception occured at the data ingestion phase ")
            raise CustomException(e,sys)    
from src.DimondPricePrediction.components.data_ingestion import DataIngestion

from src.DimondPricePrediction.components.data_transformation import DataTransformation

from src.DimondPricePrediction.components.model_trainer import ModelTrainer

from src.DimondPricePrediction.components.model_evaluation import ModelEvaluation

import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.logger import logging 
from src.DimondPricePrediction.exception import CustomException

class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            data_ingestion=DataIngestion()
            train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
            return train_data_path,test_data_path
        except Exception as e:
            raise CustomException(e,sys)
        
    def start_data_transformation(self,train_data_path,test_data_path):
        
        try:
            data_transformation = DataTransformation()
            train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)
            return train_arr,test_arr
        except Exception as e:
            raise CustomException(e,sys)
    
    def start_model_training(self,train_arr,test_arr):
        try:
            model_trainer=ModelTrainer()
            model_trainer.initate_model_training(train_arr,test_arr)
        except Exception as e:
            raise CustomException(e,sys)
                
    def start_trainig(self):
        try:
            train_data_path,test_data_path=self.start_data_ingestion()
            train_arr,test_arr=self.start_data_transformation(train_data_path,test_data_path)
            self.start_model_training(train_arr,test_arr)
        except Exception as e:
            raise CustomException(e,sys)



obj1 = TrainingPipeline()
train_path,test_path = obj1.start_data_ingestion()
data_transform = DataTransformation()
train_arr , test_arr = data_transform.initiate_data_transformation(train_path,test_path)

model_trainer = ModelTrainer()
model_trainer.initiate_model_training(train_arr,test_arr)
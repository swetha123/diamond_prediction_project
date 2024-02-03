from src.DimondPricePrediction.components.data_ingestion import DataIngestion

import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.logger import logging 
from src.DimondPricePrediction.exception import CustomException

obj = DataIngestion()

obj.initiate_data_ingestion()
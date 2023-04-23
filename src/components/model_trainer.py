#script for model training
#define the algorithms needed to apply

import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

#trains the model
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_array,test_array,preprocessor_path):
        try:
            logging.info('Splitting training and test input data')
            x_train,y_train,x_test,y_test=(
                #select all columns except last column
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "random forest":RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression" : LinearRegression(),
                "K-Neighbour classifier": KNeighborsRegressor(),
                "XGBClassifier" : XGBRegressor(),
                "CatBoosting Classifier" : CatBoostRegressor(verbose=False),
                "AdaBoost Classifier": AdaBoostRegressor()

            }
            model_report:dict=evaluate_model(x_train=x_train,
                                             y_train=y_train,
                                             x_test=x_test,
                                             y_test=y_test,
                                             models=models)
        except:
            


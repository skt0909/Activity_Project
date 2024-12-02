import yaml
from Activity_pstructure.exception.exception import ActivityException
from Activity_pstructure.logging.logger import logging
import os,sys
import dill
from sklearn.metrics import r2_score
import numpy as np
import pickle
from sklearn.impute import SimpleImputer
import mlflow
import mlflow.sklearn

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ActivityException(e, sys) from e
    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise ActivityException(e, sys)
        

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        # Handle missing values in target variables
        imputer = SimpleImputer(strategy='mean')
        y_train = imputer.fit_transform(y_train.reshape(-1, 1)).ravel()
        y_test = imputer.transform(y_test.reshape(-1, 1)).ravel()

        # Iterate over the models in the dictionary
        for model_name, model in models.items():
            logging.info(f"Training and evaluating model: {model_name}")

            # Train the model on training data
            model.fit(X_train, y_train)

            # Predict on training and testing datasets
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Calculate R² scores
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            logging.info(f"{model_name} - Train R²: {train_model_score}, Test R²: {test_model_score}")

            with mlflow.start_run():
                mlflow.log_param("model_name", model_name)
                mlflow.log_metric("train_r2_score", train_model_score)
                mlflow.log_metric("test_r2_score", test_model_score)

            # Store the test R² score in the report
            report[model_name] = test_model_score

        return report
    except Exception as e:
        raise ActivityException(e, sys)
   
def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise ActivityException(e,sys)
    
from dotenv import load_dotenv
load_dotenv()

# Fetch file paths from the environment variables
preprocessor_file_path = os.getenv('PREPROCESSOR_FILE_PATH')
model_file_path = os.getenv('MODEL_FILE_PATH')


def load_preprocessor(preprocessor_file_path):
    try:
        with open(preprocessor_file_path, 'rb') as file:
            preprocessor = pickle.load(file)
        return preprocessor
    except Exception as e:
        raise ActivityException(str(e), sys.exc_info())
    

def load_model(model_file_path):
    try:
        with open(model_file_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        raise ActivityException(str(e), sys.exc_info())
    

    
    
    



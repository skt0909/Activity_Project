from Activity_pstructure.exception.exception import ActivityException
from Activity_pstructure.logging.logger import logging
from Activity_pstructure.utils.main_utils.utils import save_object,evaluate_models
from Activity_pstructure.entity.artifact_entity import ModelTrainerConfig
from Activity_pstructure.logging.logger import logging
import sys
import mlflow
import mlflow.sklearn
import dagshub
dagshub.init(repo_owner='skt0909', repo_name='Activity_Project', mlflow=True)


from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import r2_score
from sklearn.impute import SimpleImputer
import dill
import numpy as np



class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def track_mlflow(self, best_model, best_score, best_model_name):
        # Track the best model and metrics in MLflow
        with mlflow.start_run():
            # Log model name as a parameter
            mlflow.log_param("best_model_name", best_model_name)

            # Log R² Score as a metric
            mlflow.log_metric("r2_score", best_score)

            # Log model hyperparameters (e.g., imputation strategy)
            mlflow.log_param("imputation_strategy", "mean")

            # Log the trained model using MLflow's sklearn wrapper
            mlflow.sklearn.log_model(best_model, "model")

            logging.info("Logged model and metrics to MLflow")


    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and testing data")

            # Splitting data into features and target
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1], train_array[:, -1],
                test_array[:, :-1], test_array[:, -1]
            )

            # Define models
            models = {
                "Linear Regression": LinearRegression(),
                "Gradient Boosting Regressor": GradientBoostingRegressor(),
            }



            # Evaluate models
            model_report: dict = evaluate_models(
                X_train=X_train, y_train=y_train, 
                X_test=X_test, y_test=y_test, 
                models=models
            )

            # Get best model score
            best_model_score = max(sorted(model_report.values()))

            # Get best model name from the dict
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            # Retrieve the best model
            best_model = models[best_model_name]

            # Check if the best model score is below the threshold
            if best_model_score < 0.6:
                raise ActivityException("No best Model found", sys, "Best model score is below the 0.6 threshold")

            logging.info("Best model found on train and test dataset")
    


            # Save the best model object
            save_object(
                file_path=self.model_trainer_config.trained_model_file,
                obj=best_model
            )

            save_object("final_model/model.pkl",best_model)

            # Evaluate on test data
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            logging.info(f"Best model: {best_model_name}, R2 Score: {r2_square}")

            # Track the model and results with MLflow
            self.track_mlflow(best_model, r2_square, best_model_name)

            

            return r2_square

        except Exception as e:
            # Provide error details with more context
            error_details = f"An error occurred during model training in the model_trainer module. Error: {str(e)}"
            raise ActivityException(str(e), error_details)
        
        
        



        

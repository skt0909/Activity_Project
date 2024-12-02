from Activity_pstructure.src.preprocessing_data import preprocess_data
from Activity_pstructure.utils.main_utils.utils import load_preprocessor, load_model
import os
import sys
import numpy as np
from dotenv import load_dotenv
from Activity_pstructure.exception.exception import ActivityException

# Load environment variables
load_dotenv()

# Paths from .env
PREPROCESSOR_FILE_PATH= os.getenv("PREPROCESSOR_FILE_PATH")
MODEL_FILE_PATH = os.getenv("MODEL_FILE_PATH")

def run_prediction():
    try:
        preprocessed_data = preprocess_data()
        preprocessor = load_preprocessor(PREPROCESSOR_FILE_PATH)

        # Load model and predict
        model = load_model(MODEL_FILE_PATH)
        predictions = model.predict(preprocessed_data)
        print("Predictions:", predictions)

    except Exception as e:
        raise ActivityException(str(e), sys.exc_info())  # Use sys.exc_info() here

if __name__ == "__main__":
    run_prediction()

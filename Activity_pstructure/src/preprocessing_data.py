import numpy as np
import sys,os
from dotenv import load_dotenv
import pickle
from sklearn.preprocessing import StandardScaler
from Activity_pstructure.exception.exception import ActivityException
from Activity_pstructure.src.data_loader import fetch_data_from_mongo



def preprocess_data():
    try:
        # Fetch data from MongoDB
        documents = fetch_data_from_mongo()

        # Extract features (ensure these fields are present in your MongoDB documents)
        features_columns = ['steps', 'distance', 'trackerDistance', 'loggedActivitiesDistance', 
                        'veryActiveDistance', 'moderatelyActiveDistance', 'lightActiveDistance', 
                        'sedentaryActiveDistance', 'veryActiveMinutes', 'fairlyActiveMinutes', 
                        'lightlyActiveMinutes', 'sedentaryMinutes']

        # Extract the feature data from MongoDB documents
        features = []
        for doc in documents:
        # Ensure that each feature exists in the document, defaulting to 0 if missing
            feature_row = [doc.get(col, 0) for col in features_columns]
            features.append(feature_row)

        # Convert features to a numpy array
        features = np.array(features)

        # Apply StandardScaler for preprocessing
        scaler = StandardScaler()
        preprocessed_data = scaler.fit_transform(features)
    
        return preprocessed_data
    except Exception as e:
        raise ActivityException(str(e), sys.exc_info()) 



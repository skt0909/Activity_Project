import pandas as pd
import numpy as np
import pymongo
import json
import os

# Create the folder if it doesn't exist
folder_path = "Activity_Dummy_data"
os.makedirs(folder_path, exist_ok=True)

# Generate dummy data
num_records = 2 # Number of dummy records

data = {
    "steps": np.random.randint(1000, 20000, size=num_records),
    "distance": np.random.uniform(1.0, 15.0, size=num_records),  # Distance in km
    "trackerDistance": np.random.uniform(1.0, 15.0, size=num_records),
    "loggedActivitiesDistance": np.random.uniform(1.0, 10.0, size=num_records),
    "veryActiveDistance": np.random.uniform(0.0, 5.0, size=num_records),
    "moderatelyActiveDistance": np.random.uniform(0.0, 5.0, size=num_records),
    "lightActiveDistance": np.random.uniform(0.0, 5.0, size=num_records),
    "sedentaryActiveDistance": np.random.uniform(0.0, 5.0, size=num_records),
    "veryActiveMinutes": np.random.randint(0, 60, size=num_records),
    "fairlyActiveMinutes": np.random.randint(0, 60, size=num_records),
    "lightlyActiveMinutes": np.random.randint(0, 60, size=num_records),
    "sedentaryMinutes": np.random.randint(0, 1440, size=num_records),  # In minutes
    "calories": np.random.randint(1500, 3500, size=num_records)
}

# Convert dictionary to a DataFrame
dummy_data = pd.DataFrame(data)

# File name for the CSV file
file_name = "Activity_D_Data.csv"
file_path = os.path.join(folder_path, file_name)

# Save the DataFrame to a CSV file
dummy_data.to_csv(file_path, index=False)






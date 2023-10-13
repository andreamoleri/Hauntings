# Libraries Import
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the CSV file
file_path = 'hauntings.csv'
df = pd.read_csv(file_path)

# Split the data into features (X) and target (y)
X = df.drop('target_column_name', axis=1)  # Replace 'target_column_name' with the name of the target column
y = df['target_column_name']

def explore_data_frame():
   # Explore the data
    print(df.head())  # Display the first rows of the DataFrame
    print(df.info())  # Display information about the DataFrame 


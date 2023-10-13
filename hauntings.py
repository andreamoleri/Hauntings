# Libraries Import
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the CSV file
file_path = 'hauntings.csv'
df = pd.read_csv(file_path)

print(df)
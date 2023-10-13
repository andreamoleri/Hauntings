# Libraries Import
import pandas as pd
import folium
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'hauntings.csv'
df = pd.read_csv(file_path)

def explore_data_frame():
   # Explore the data
    print(df.head())  # Display the first rows of the DataFrame
    print(df.info())  # Display information about the DataFrame
     
# Conta le occorrenze di ciascuno stato nel DataFrame
state_counts = df['state'].value_counts().reset_index()
state_counts.columns = ['state', 'count']

# Crea una mappa centrata negli Stati Uniti
us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)


# Salva la mappa in un file HTML
us_map.save('us_state_distribution.html')

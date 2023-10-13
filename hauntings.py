# Libraries Import
import pandas as pd
import folium
from folium.plugins import HeatMap
from sklearn.model_selection import train_test_split
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

# Converte 'latitude' e 'longitude' in numeri (float) se non lo sono già
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

# Crea una mappa centrata negli Stati Uniti
us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)


# Crea una lista di coordinate [(lat, lon, peso)] per la Heatmap
heat_data = []
for index, row in df.iterrows():
    
    
    # Controllo se il valore nella colonna "latitude" è nullo prima di accedervi
    if not pd.isnull(df.at[index, 'latitude']):
        latitude = df.at[index, 'latitude']
    else:
        latitude = 100
        
    if not pd.isnull(df.at[index, 'longitude']):
        longitude = df.at[index, 'longitude']
    else:
        longitude = 100
    
    heat_data.append([latitude, longitude, index])

# Aggiungi la Heatmap alla mappa
HeatMap(heat_data).add_to(us_map)

# Salva la mappa in un file HTML
us_map.save('us_state_distribution.html')
print(len(heat_data))

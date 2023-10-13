# Import necessary libraries for data visualization, map plotting, and analysis
import folium
import pandas as pd
import auxiliaryFunctions
from folium.plugins import HeatMap

# Define the path to the CSV containing haunted locations data
# Then read the data from the CSV file into a Pandas DataFrame
file_path = 'hauntings.csv'
dataframe = pd.read_csv(file_path)

# Convert latitude and longitude columns to numeric, handling errors by coercing
dataframe['latitude'] = pd.to_numeric(dataframe['latitude'], errors='coerce')
dataframe['longitude'] = pd.to_numeric(dataframe['longitude'], errors='coerce')

# Create a base map centered around the United States of America
us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Prepare data for a heatmap visualization
heat_data = []
for index, row in dataframe.iterrows():
    if not pd.isnull(dataframe.at[index, 'latitude']):
        latitude = dataframe.at[index, 'latitude']
    else:
        latitude = 0  # Replace missing latitude with an arbitrary value

    if not pd.isnull(dataframe.at[index, 'longitude']):
        longitude = dataframe.at[index, 'longitude']
    else:
        longitude = 0  # Replace missing longitude with an arbitrary value

    heat_data.append([latitude, longitude, index])  # Append every row to the heatmap

# Create a heatmap using the prepared data
# Then save the map as an HTML file
HeatMap(heat_data).add_to(us_map)
us_map.save('HauntingsDistribution.html')
      
# Print haunting stats to a .txt file
auxiliaryFunctions.stats(dataframe)
auxiliaryFunctions.success_message()


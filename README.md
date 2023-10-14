# Hauntings 👻

This Python program processes haunted locations data from a CSV file and generates a heatmap to visualize the most haunted places in the United States of America. It also provides statistics related to these haunted locations.

![Screenshot 2023-10-13 at 22 03 20](https://github.com/andreamoleri/Hauntings/assets/70026300/6dc7d816-e662-4b2c-ad53-63c73154f6ca)

## Prerequisites

Make sure you have the following libraries installed in your Python environment:
- [Folium](https://python-visualization.github.io/folium/)
- [Pandas](https://pandas.pydata.org/)
  
## Installation
You can install the required libraries using pip:
```bash
pip install folium pandas
```
## Usage
### Clone the Repository:
```bash
git clone https://github.com/your-username/hauntings-map.git
cd hauntings-map
```

### Prepare Haunted Locations Data:
- Create a CSV file named **hauntings.csv** containing the haunted locations data. The CSV file should have columns named **latitude** and **longitude** for the location coordinates.
  
### Run the Program:
```bash
python3 hauntings.py
```

### View the Output:
- The script will generate a heatmap named **HauntingsDistribution.html** showcasing the distribution of haunted locations in America. 
- The statistics related to haunting will be printed in the console and saved in a file named **hauntingstats.txt**.
  
## Program Explanation
### Import Libraries:
- Folium is used for map visualization.
- Pandas is used for data manipulation and analysis.
### Read Haunted Locations Data:
- The script reads the haunted locations data from **hauntings.csv** into a Pandas DataFrame. This file was kindly provided in the public domain by Tim Renner (https://data.world/timothyrenner/haunted-places)
### Data Processing:
- Missing latitude and longitude values are replaced with arbitrary values (0) for heatmap generation.
### Heatmap Generation:
- The script creates a heatmap using the processed data and saves it as an HTML file (**'HauntingsDistribution.html'**).
### Statistics:
The script calculates and prints statistics related to the haunted locations, and saves them in **'hauntingstats.txt'**.


  👻 _Happy Haunting!_ 👻

# Function to explore the DataFrame, providing a summary of its contents
def explore_data_frame():
    """
    Display the first few rows of the DataFrame and print information about the DataFrame's structure.
    """
    print(dataframe.head())
    print(dataframe.info())

# Function that returns useful stats about the DataFrame
def stats():
    stateCount = dataframe['state'].value_counts()
    statePercs = dataframe['state'].value_counts(normalize=True)
    stateStats = pd.concat([stateCount, statePercs * 100], axis=1, keys=['count', 'percentage'])
    with open('hauntingstats.txt', 'w') as f:
        f.write(str(stateStats))
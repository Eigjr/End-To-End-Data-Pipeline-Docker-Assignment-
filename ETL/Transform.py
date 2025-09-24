import os
import pandas as pd
from loading_dataset import movies, items, users_data

# Function to clean and transform the dataset

try:

    # Convert the 'timestamp' column to datetime format
    users_data['timestamp'] = pd.to_datetime(users_data['timestamp'], unit='s')

    #rename timestam to datetime
    users_data.rename(columns={'timestamp': 'datetime'}, inplace=True)

    #covernt release_date to datetime
    items['release_date'] = pd.to_datetime(items['release_date'], format='%Y-%m-%d')  


    # drop  all duplication from the dataset
    movies.drop_duplicates(inplace=True)
    items.drop_duplicates(inplace=True)
    users_data.drop_duplicates(inplace=True)

    # drop all the null values from the dataset
    movies.dropna(inplace=True)
    items.dropna(inplace=True)
    users_data.dropna(inplace=True)

    #print(movies.head())
    #print(items.head())
    #print(users_data.head())

except Exception as e:
    print(f"An error occurred while cleaning and transforming the data: {e}")


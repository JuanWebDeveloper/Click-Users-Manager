import json
import os

# Function to read data from 'users_data.json' file
def read_data_from_json():
    # Check if the file 'users_data.json' exists
    if not os.path.isfile('./data/users_data.json'):
        # If it does not exist, create the file and write an empty list to it
        with open('./data/users_data.json', 'w') as f:
            json.dump([], f)
    # Open the file and load the data of the users
    with open('./data/users_data.json', 'r') as f:
        data = json.load(f)
    return data

# Function to write data to 'users_data.json' file
def write_data_to_json(data):
    # Open the file and write the data to it
    with open('./data/users_data.json', 'w') as f:
        json.dump(data, f)
        
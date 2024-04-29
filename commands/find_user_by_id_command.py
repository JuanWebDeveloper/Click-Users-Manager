# Import necessary modules
import click
from utils.json_data_manager import read_data_from_json

# Define the 'find_user_by_id' command
@click.command('find_user_by_id')
# Add an argument for the command
@click.argument('id')
def find_user_by_id(id):
    # Read the existing data from the JSON file
    users = read_data_from_json()
    # Loop through the users
    for user in users:
        # If the user's id matches the provided id
        if str(user['id']) == id:
            # Print the user's details
            print(f"User {user['name']} {user['lastname']} of age {user['age']} identified with the ID {user['id']}")
            break
    else:
        # If no user was found with the provided id, print a message
        print(f"User with id {id} not found")
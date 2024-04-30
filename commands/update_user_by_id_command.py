# Import necessary modules
import click
from utils.json_data_manager import read_data_from_json, write_data_to_json

# Define the 'update_user_by_id' command
@click.command('update_user_by_id')
# Add an argument and options for the command
@click.argument('id')
@click.option('--name',  help='Name of the user')
@click.option('--lastname',  help='Lastname of the user')
@click.option('--age',  help='Age of the user')
def update_user_by_id(id, name, lastname, age):
    # Read the existing data from the JSON file
    users = read_data_from_json()
    # If no options are provided, print a message
    if name is None and lastname is None and age is None:
        print("Please provide at least one option to update the user.")
        return
    
    # Check if the user with the provided id exists
    if not any(user['id'] == int(id) for user in users):
         # If no user was found with the provided id, print a message
         print(f"User with id {id} not found")
         return
    
    # Loop through the users
    for user in users:
        # If the user's id matches the provided id
        if user['id'] == int(id):
            # If a new name is provided, update the user's name
            if name is not None:
                user['name'] = name
            # If a new lastname is provided, update the user's lastname
            if lastname is not None:
                user['lastname'] = lastname
            # If a new age is provided, update the user's age
            if age is not None:
                user['age'] = age
        # Write the updated data back to the JSON file
        write_data_to_json(users)
        # Print a success message
        print(f"User with id {id} updated successfully")
        return
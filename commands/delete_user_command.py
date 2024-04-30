# Import necessary modules
import click
from utils.json_data_manager import read_data_from_json, write_data_to_json

# Define 'delete_user' command
@click.command('delete_user')
@click.argument('id')
def delete_user(id):
    # Read data from JSON file
    users = read_data_from_json()

    # Iterate over users
    for user in users:
        # Check if user ID matches provided ID
        if str(user['id']) == id:
            # Remove user and update JSON file
            users.remove(user)
            write_data_to_json(users)

            # Print success message and exit loop
            print(f"User with id {id} deleted successfully")
            break
    # If no matching user is found, print error message
    else:
        print(f"User with id {id} not found")
import click
from utils.json_data_manager import read_data_from_json

# Defining a new command 'list-users' using the 'click.command' decorator
@click.command('list-users')
def list_users():
    # Reading user data from the JSON file
    users = read_data_from_json()
    # Looping through each user and printing their details
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']} - {user['age']}")
import click
from utils.json_data_manager import read_data_from_json

@click.command('list-users')
def list_users():
    users = read_data_from_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']} - {user['age']}")
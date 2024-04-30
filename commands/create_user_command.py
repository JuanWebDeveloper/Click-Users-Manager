import click
from utils.json_data_manager import read_data_from_json, write_data_to_json

# Define the 'create_user' command
@click.command("create_user")
# Add options for the command
@click.option('--name', required=True, help='Name of the user')
@click.option('--lastname', required=True, help='Lastname of the user')
@click.option('--age', required=True, help='Age of the user')
def create_user(name, lastname, age):
	 # Read the existing data from the JSON file
    data = read_data_from_json()
    # Append the new user to the data
    data.append({
        'id': len(data) + 1,
        'name': name,
        'lastname': lastname,
        'age': int(age)
    })    
    # Write the updated data back to the JSON file
    write_data_to_json(data)
    # Print a success message
    print(f"User {name} {lastname} added successfully with id {len(data)}")
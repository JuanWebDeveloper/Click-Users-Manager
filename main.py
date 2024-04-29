import click
from commands.list_users_command import list_users
from commands.create_user_command import create_user
from commands.find_user_by_id_command import find_user_by_id

@click.group()
def command_line_interface():
    pass

# Adding commands to the command line interface
command_line_interface.add_command(list_users)
command_line_interface.add_command(create_user)
command_line_interface.add_command(find_user_by_id)

if __name__ == '__main__':
    command_line_interface()
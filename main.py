import click
from commands.list_users_command import list_users
from commands.create_user_command import create_user

@click.group()
def command_line_interface():
    pass

# Adding commands to the command line interface
command_line_interface.add_command(list_users)
command_line_interface.add_command(create_user)

if __name__ == '__main__':
    command_line_interface()
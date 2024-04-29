import click
from commands.list_users_command import list_users

@click.group()
def command_line_interface():
    pass

# Adding the 'list_users' command to the command line interface
command_line_interface.add_command(list_users)

if __name__ == '__main__':
    command_line_interface()
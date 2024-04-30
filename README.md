# User Management Application

This is a command-line application for managing users.

## Installation

1. Clone the repository to your local machine.
2. The repository comes with a virtual environment with all the necessary dependencies. Activate the virtual environment:
   - On Windows, run: `.\venv\Scripts\activate`
   - On Unix or MacOS, run: `source venv/bin/activate`
3. You're all set to use the application!

## Available Commands

- `list_users`: Lists all users.
- `create_user`: Creates a new user.
- `find_user_by_id`: Finds a user by their ID.
- `update_user_by_id`: Updates an existing user by ID.
- `delete_user`: Deletes an existing user by ID.

Each command requires different arguments. For help on a specific command, you can use `--help` after the command name.

## Usage Examples

To list all users:

```python
python main.py list_users
```

To create a new user:

```python
python main.py create_user --name "John" --lastname "Doe" --age "22"
```

To find a user by their ID:

```python
python main.py find_user_by_id 1
```

To update an existing user by ID:

```python
python main.py update_user_by_id 1 --name "John Doe" --lastname "Smith" --age "42"
```

To delete a user:

```python
python main.py delete_user 1
```

## Development

This application is under active development. To contribute, please fork the repository and submit a pull request with your changes.

# Account Project
A simple project that allows you to easily create, save, delete, and edit accounts.

## How to use
To use the project, you can follow these steps:

1. Install the requirements: `pip install -r requirements.txt`
1. Start the server: `python init.py`
2. Open your browser: `http://localhost:5035/`

## Backup and Restore
The project includes a backup feature that allows you to create a backup of your data at regular intervals. You can configure the backup frequency by modifying the `backup_frequency` variable in the `BackupController` class. Also every time you start the server, the backup will be created.

To restore a backup, simply copy the backup directory to the original directory and restart the server.
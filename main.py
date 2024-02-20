import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow

from create_database import create_tables
from ui_main_window import *

def setUp_files():
    # Define the directory path
    data_directory = "data"

    # Define the file names
    files = [
        "general-interview-questions.txt",
        "technical-interview-questions.txt",
        "coding-interview-questions.txt",
    ]

    # Check if the data directory exists, create it if not
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    # Check if each file exists, create it if not
    for file_name in files:
        file_path = os.path.join(data_directory, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                # You can add initial content if needed
                pass
            print(f"File '{file_name}' created in '{data_directory}'.")

def setUp_database():
    # define the SQLite database file name
    db_file = "data/JobApplicationVault_database.db"

    # check if the database exists
    try:
        connection = sqlite3.connect(db_file)
        print(f"Connected to the database: {db_file}")
    except sqlite3.Error:
        print(f"Error connecting to the database: {e}")
        exit()

    create_tables(connection) # create tables if they don't exist
    connection.close() # close the database connection

def setUp_application():
    # create instances
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow) # set up the main window ui
    MainWindow.show() # show the main window
    sys.exit(app.exec_()) # start the application


if __name__ == "__main__":
    setUp_files()
    setUp_database()
    setUp_application()
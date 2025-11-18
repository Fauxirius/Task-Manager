import os

# Secret key for the Flask application.
# This is used for session signing and other security-related purposes.
# In development, it's set to 'dev', but it should be replaced with a strong, random value in production.
SECRET_KEY = 'dev'

# The absolute path to the application's SQLite database file.
# It's constructed dynamically to ensure it works regardless of where the application is run from.
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks.db')

# The absolute path to the directory where user-uploaded files will be stored.
# This is typically used for handling file uploads in the application.
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')


# A dictionary containing configuration for different servers that the application might need to interact with.
# Each server has a URL and a type.
SERVERS = {
    "zomato-mcp-server": {
        "url": "https://mcp-server.zomato.com/mcp",
        "type": "http"
    }
}

# A list of predefined statuses that a task can have within the application.
# This helps in maintaining consistency in task status management.
TASK_STATUSES = ["ToDo", "InProgress", "Completed"]

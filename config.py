import os

SECRET_KEY = 'dev'
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks.db')
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')


SERVERS = {
    "zomato-mcp-server": {
        "url": "https://mcp-server.zomato.com/mcp",
        "type": "http"
    }
}

TASK_STATUSES = ["ToDo", "InProgress", "Completed"]

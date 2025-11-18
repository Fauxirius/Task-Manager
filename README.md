# Task Manager Application

This is a simple Task Manager web application built with Flask. It allows users to create, view, edit, and delete tasks. The application also includes features like task sorting, filtering, status updates, a theme switcher for light and dark modes, and a chat interface.

## Features

- **CRUD Operations:** Create, Read, Update, and Delete tasks.
- **Task Management:** 
    - View a list of all tasks.
    - Add new tasks with a title, description, start date, end date, and status.
    - Edit existing tasks.
    - Delete tasks.
- **Sorting and Filtering:**
    - Sort tasks by ID, start date, end date, or status.
    - Filter tasks by their status (ToDo, InProgress, Completed).
- **Status Updates:** Easily update the status of a task directly from the main task list.
- **Theme Switcher:** Toggle between light and dark themes for better user experience.
- **Dashboard:**
    - View task statistics (total, to-do, in-progress, completed).
    - Get reminders for urgent and approaching deadline tasks.
    - A calendar view of tasks with deadlines.
    - A bar chart showing the distribution of task statuses.
- **API Endpoints:** A RESTful API for managing tasks and interacting with the application programmatically.
- **Chat Interface:** A simple chat interface to interact with an MCP (Master Control Program) server.

## Project Structure

```
.
├── app.py                  # Main Flask application file
├── config.py               # Configuration file for the application
├── schema.sql              # SQL schema for the database
├── tasks.db                # SQLite database file
├── static/
│   ├── css/
│   │   └── style.css       # CSS styles for the application
│   └── js/
│       └── theme.js        # JavaScript for the theme switcher
└── templates/
    ├── 404.html            # 404 error page
    ├── add.html            # Page to add a new task
    ├── base.html           # Base template for all pages
    ├── edit.html           # Page to edit a task
    └── index.html          # Main page with the task list
```

## Getting Started

### Prerequisites

- Python 3
- Flask

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/task-manager.git
    cd task-manager
    ```

2.  **Install the dependencies:**
    ```bash
    pip install Flask
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```

The application will be running at `http://127.0.0.1:5000`.

## API Endpoints

The application provides the following API endpoints:

- `GET /api/tasks`: Get all tasks.
- `GET /api/task/<task_id>`: Get a single task by its ID.
- `POST /api/tasks`: Create a new task.
- `PUT /api/task/<task_id>`: Update an existing task.
- `DELETE /api/task/<task_id>`: Delete a task.
- `POST /api/task/<task_id>/status`: Update the status of a task.
- `GET /api/tasks/events`: Get task events for the calendar.
- `GET /api/tasks/stats`: Get task statistics.
- `GET /api/mcp`: Get MCP servers.
- `POST /api/mcp/chat`: Chat with MCP.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

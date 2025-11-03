# Task Manager Application

A simple and efficient web-based application for managing tasks.

## Description

The Task Manager is a lightweight and user-friendly tool designed to help individuals and teams track their tasks effectively. It provides a clean and intuitive interface for creating, viewing, editing, and deleting tasks. The application also features a theme switcher for light and dark modes, and the ability to update task statuses directly from the main page.

## Features

- **CRUD Operations:** Create, Read, Update, and Delete tasks.
- **Task Sorting and Filtering:** Sort tasks by ID, title, start date, end date, or status. Filter tasks by their status.
- **Theme Switcher:** Toggle between light and dark modes for better user experience.
- **Inline Status Updates:** Update task statuses directly from the main task list.
- **Reminders:** Get reminders for urgent tasks and tasks with approaching deadlines.
- **RESTful API:** A comprehensive API for interacting with the application programmatically.

## Technology Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Fauxirius/cli.git
    cd cli
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install Flask
    ```

## Running the Application

1.  **Initialize the database:**
    The application will automatically create and populate the database (`tasks.db`) when you run it for the first time.

2.  **Run the Flask application:**
    ```bash
    python app.py
    ```

3.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000`.

## Running Tests

To run the tests, execute the following command in your terminal:

```bash
python test_app.py
```

## API Endpoints

The application provides the following API endpoints:

| Method | Endpoint                  | Description                               |
|--------|---------------------------|-------------------------------------------|
| GET    | `/api/tasks`              | Get all tasks.                            |
| GET    | `/api/task/<task_id>`     | Get a specific task by its ID.            |
| POST   | `/api/tasks`              | Create a new task.                        |
| PUT    | `/api/task/<task_id>`     | Update an existing task.                  |
| DELETE | `/api/task/<task_id>`     | Delete a task.                            |
| POST   | `/api/task/<task_id>/status` | Update the status of a specific task.     |
| GET    | `/api/tasks/stats`        | Get statistics about the tasks.           |
| GET    | `/api/tasks/events`       | Get tasks as calendar events.             |
| GET    | `/api/mcp`                | Get MCP server information.               |
| POST   | `/api/mcp/chat`           | Chat with the MCP server.                 |

## Database Schema

The database consists of a single table named `tasks`.

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    start_date TEXT,
    end_date TEXT,
    status TEXT
);
```

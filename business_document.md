# Business Document: Task Manager Application

## Executive Summary

This document outlines the Task Manager, a web-based application designed for efficient task tracking and management. The tool provides core functionalities for creating, viewing, editing, and deleting tasks. This document provides an overview of the application's features, a snapshot of current tasks, and a summary of the underlying technology. The Task Manager is a lightweight and user-friendly solution for improving team productivity and workflow management.

## 1. Introduction

This document provides a business-level overview of the Task Manager web application. The application is a simple, web-based tool designed to help teams track and manage their tasks effectively. It provides a clean and intuitive interface for users to view, add, edit, and delete tasks.

## 2. Functionality

The core functionalities of the Task Manager application are:

*   **View Tasks:** The main page displays a list of all current tasks. Users can sort the tasks by ID, start date, or end date. They can also filter tasks by their status (e.g., "To Do", "In Progress").
*   **Add a New Task:** Users can add new tasks to the system by providing a title, description, start date, end date, and status.
*   **Edit Existing Tasks:** Existing tasks can be modified to update their details.
*   **Delete Tasks:** Tasks that are no longer needed can be removed from the system.

## 3. Current Tasks

Here is a table of the tasks currently in the system:

| ID | Title                     | Description                                                  | Start Date | End Date   | Status      |
|----|---------------------------|--------------------------------------------------------------|------------|------------|-------------|
| 1  | Complete Project Proposal | Write and submit the project proposal for the new client.    | 2025-11-01 | 2025-11-10 | InProgress  |
| 2  | Team Meeting              | Weekly team sync-up meeting.                                 | 2025-10-28 | 2025-10-28 | ToDo        |

## 4. Report Visualization

This section provides a visual representation of the current task status distribution.

**Tasks by Status:**

```
InProgress:  ██████████ (1)
ToDo:        ██████████ (1)
```

This simple bar chart shows the number of tasks in each status category.

## 5. Technology Stack

The application is built using the following technologies:

*   **Backend:** Python with the Flask framework.
*   **Frontend:** HTML with standard form elements.
*   **Database:** A simple in-memory data store (a Python list).

This lightweight and flexible technology stack allows for rapid development and easy maintenance.
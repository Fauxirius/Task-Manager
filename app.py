import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort, flash, g
import config
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(config)

def create_db_and_populate():
    if not os.path.exists(app.config['DATABASE']):
        init_db()
        populate_db()

# Database setup
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def populate_db():
    with app.app_context():
        db = get_db()
        c = db.cursor()
        # Check if tasks table is empty before populating
        c.execute('SELECT COUNT(*) FROM tasks')
        count = c.fetchone()[0]
        if count == 0:
            tasks = [
                {
                    'title': 'Complete Project Proposal',
                    'description': 'Write and submit the project proposal for the new client.',
                    'start_date': '2025-11-01',
                    'end_date': '2025-11-10',
                    'status': 'InProgress'
                },
                {
                    'title': 'Team Meeting',
                    'description': 'Weekly team sync-up meeting.',
                    'start_date': '2025-10-28',
                    'end_date': '2025-10-28',
                    'status': 'ToDo'
                },
                {
                    'title': 'Review Design Mockups',
                    'description': 'Provide feedback on the new UI mockups.',
                    'start_date': '2025-10-29',
                    'end_date': '2025-11-03',
                    'status': 'ToDo'
                },
                {'title': 'Build a scalable framework', 'description': 'Develop a robust and extensible framework for future projects.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'G-T shared documents', 'description': 'Organize and share relevant documents with the G-T team.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'Prepare a reusable rfp/rfi deck', 'description': 'Create a standardized and reusable RFP/RFI presentation deck.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'Google labs', 'description': 'Explore and experiment with new features in Google Labs.', 'start_date': '', 'end_date': '', 'status': 'Completed'},
                {'title': 'Google Cloud lab hands on GCA', 'description': 'Gain practical experience with Google Cloud Platform using GCA.', 'start_date': '', 'end_date': '', 'status': 'Completed'},
                {'title': 'G-T recording', 'description': 'Record and archive G-T team meetings and discussions.', 'start_date': '', 'end_date': '', 'status': 'InProgress'},
                {'title': 'GC framework', 'description': 'Design and implement a framework for Google Cloud services.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'Google Cloud lab hands on CLI', 'description': 'Practice using the Google Cloud command-line interface.', 'start_date': '', 'end_date': '', 'status': 'Completed'},
                {'title': 'Product documentation (GCA)', 'description': 'Create comprehensive product documentation for GCA.', 'start_date': '', 'end_date': '', 'status': 'Completed'},
                {'title': 'Developer in Demo', 'description': 'Participate as a developer in product demonstrations.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'Understand and standardise customer needs structure', 'description': 'Analyze and standardize the structure of customer needs.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'Identify and understand all relevant use cases', 'description': 'Discover and comprehend all pertinent use cases for the product.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'Solution for automating documentation', 'description': 'Develop a solution to automate the documentation process.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'Get hands-on with GCA CLI', 'description': 'Practice and become proficient with the GCA command-line interface.', 'start_date': '', 'end_date': '', 'status': 'InProgress'},
                {'title': 'scope ongoing process', 'description': 'Define the scope and boundaries of the ongoing process.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'POC/ MVP scope', 'description': 'Determine the scope for Proof of Concept and Minimum Viable Product.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'Org constraints/policies scope', 'description': 'Identify and document organizational constraints and policy scope.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'AI/ML GC technical expert', 'description': 'Consult with an AI/ML Google Cloud technical expert.', 'start_date': '', 'end_date': '', 'status': 'InProgress'},
                {'title': 'brd to task/tickets to code', 'description': 'Translate business requirements into technical tasks and code.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'direct pull from atlassian to build and update', 'description': 'Implement direct data synchronization from Atlassian for builds and updates.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'copilot vs claude vs codex vs GCA', 'description': 'Compare and evaluate AI coding assistants: Copilot, Claude, Codex, and GCA.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'Create BRD>tasks>execute>update within GCA', 'description': 'Manage the full lifecycle from Business Requirements Document to task execution and updates within GCA.', 'start_date': '', 'end_date': '', 'status': 'Completed'},
                {'title': 'understand indexing and local code awareness in GCACLI', 'description': 'Gain a deep understanding of indexing and local code awareness features in GCACLI.', 'start_date': '', 'end_date': '', 'status': 'ToDo'},
                {'title': 'context interface in GCA hallucinates & fails with custom commands', 'description': 'Investigate and resolve issues with the GCA context interface when using custom commands.', 'start_date': '', 'end_date': '', 'status': 'ToDo'}
            ]
            for task in tasks:
                c.execute('INSERT INTO tasks (title, description, start_date, end_date, status) VALUES (?, ?, ?, ?, ?)',
                             (task['title'], task['description'], task['start_date'], task['end_date'], task['status']))
            db.commit()

create_db_and_populate()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    sort_by = request.args.get('sort_by', 'id')
    # Whitelist of allowed sort_by columns to prevent SQL injection
    allowed_sort_by = ['id', 'title', 'start_date', 'end_date', 'status']
    if sort_by not in allowed_sort_by:
        sort_by = 'id'

    filter_by_status = request.args.get('filter_by_status', 'all')

    db = get_db()
    
    count_query = "SELECT COUNT(*) FROM tasks"
    params = []
    if filter_by_status != 'all':
        count_query += " WHERE status = ?"
        params.append(filter_by_status)
    total_tasks = db.execute(count_query, params).fetchone()[0]
    total_pages = (total_tasks + per_page - 1) // per_page

    tasks_query = f"SELECT * FROM tasks"
    if filter_by_status != 'all':
        tasks_query += " WHERE status = ?"
    
    tasks_query += f" ORDER BY {sort_by} ASC"
    tasks_query += f" LIMIT {per_page} OFFSET {offset}"

    tasks = db.execute(tasks_query, params).fetchall()

    # Calculate task stats
    stats_query = db.execute("SELECT status, COUNT(*) as count FROM tasks GROUP BY status").fetchall()
    stats = {stat['status']: stat['count'] for stat in stats_query}
    stats['total'] = sum(stats.values())

    # Get reminders
    today = datetime.now().date()
    urgent_tasks = []
    approaching_deadline_tasks = []
    all_tasks_for_reminders = db.execute("SELECT * FROM tasks").fetchall()
    for task in all_tasks_for_reminders:
        if task['status'] not in ['Completed'] and task['end_date']:
            try:
                end_date = datetime.strptime(task['end_date'], '%Y-%m-%d').date()
                if end_date <= today:
                    urgent_tasks.append(task)
                elif today < end_date <= today + timedelta(days=4):
                    approaching_deadline_tasks.append(task)
            except ValueError:
                pass # Ignore tasks with invalid date formats

    return render_template('index.html', 
                           tasks=tasks, 
                           sort_by=sort_by, 
                           filter_by_status=filter_by_status, 
                           stats=stats,
                           urgent_tasks=urgent_tasks,
                           approaching_deadline_tasks=approaching_deadline_tasks,
                           page=page,
                           total_pages=total_pages,
                           task_statuses=app.config['TASK_STATUSES'])

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        if start_date and end_date and end_date < start_date:
            flash('End date cannot be before the start date.', 'danger')
            return render_template('add.html', task_statuses=app.config['TASK_STATUSES'])

        db = get_db()
        db.execute('INSERT INTO tasks (title, description, start_date, end_date, status) VALUES (?, ?, ?, ?, ?)',
                     (request.form['title'], request.form['description'], start_date, end_date, request.form['status']))
        db.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html', task_statuses=app.config['TASK_STATUSES'])

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    db = get_db()
    task = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    
    if not task:
        abort(404)

    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        if start_date and end_date and end_date < start_date:
            flash('End date cannot be before the start date.', 'danger')
            return render_template('edit.html', task=task, task_statuses=app.config['TASK_STATUSES'])

        db.execute('UPDATE tasks SET title = ?, description = ?, start_date = ?, end_date = ?, status = ? WHERE id = ?',
                     (request.form['title'], request.form['description'], start_date, end_date, request.form['status'], task_id))
        db.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit.html', task=task, task_statuses=app.config['TASK_STATUSES'])

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    db = get_db()
    db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    db.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/api/task/<int:task_id>/status', methods=['POST'])
def update_task_status(task_id):
    data = request.get_json()
    if not data or 'status' not in data or data['status'] not in app.config['TASK_STATUSES']:
        return jsonify({'success': False, 'error': 'Missing or invalid status in request'}), 400

    db = get_db()
    db.execute('UPDATE tasks SET status = ? WHERE id = ?', (data['status'], task_id))
    db.commit()
    task = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()

    if not task:
        return jsonify({'success': False, 'error': 'Task not found'}), 404

    return jsonify({'success': True, 'task': dict(task)})

@app.route('/api/tasks/events')
def task_events():
    db = get_db()
    tasks = db.execute('SELECT * FROM tasks WHERE end_date IS NOT NULL').fetchall()
    events = [
        {
            'id': task['id'],
            'title': task['title'],
            'start': task['end_date'],
            'description': task['description']
        } for task in tasks
    ]
    return jsonify(events)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    db = get_db()
    tasks = db.execute('SELECT * FROM tasks').fetchall()
    return jsonify([dict(task) for task in tasks])

@app.route('/api/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    db = get_db()
    task = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(dict(task))

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title in request'}), 400

    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if start_date and end_date and end_date < start_date:
        return jsonify({'error': 'End date cannot be before the start date.'}), 400

    db = get_db()
    c = db.cursor()
    c.execute('INSERT INTO tasks (title, description, start_date, end_date, status) VALUES (?, ?, ?, ?, ?)',
                 (data['title'], data.get('description'), start_date, end_date, data.get('status', 'ToDo')))
    db.commit()
    new_task_id = c.lastrowid

    new_task = db.execute('SELECT * FROM tasks WHERE id = ?', (new_task_id,)).fetchone()

    return jsonify(dict(new_task)), 201

@app.route('/api/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    db = get_db()
    task = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    
    if not task:
        return jsonify({'error': 'Task not found'}), 400

    start_date = data.get('start_date', task['start_date'])
    end_date = data.get('end_date', task['end_date'])

    if start_date and end_date and end_date < start_date:
        return jsonify({'error': 'End date cannot be before the start date.'}), 400

    db.execute('UPDATE tasks SET title = ?, description = ?, start_date = ?, end_date = ?, status = ? WHERE id = ?',
                 (data.get('title', task['title']),
                  data.get('description', task['description']),
                  start_date,
                  end_date,
                  data.get('status', task['status']),
                  task_id))
    db.commit()

    updated_task = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()

    return jsonify(dict(updated_task))

@app.route('/api/task/<int:task_id>', methods=['DELETE'])
def api_delete_task(_id):
    db = get_db()
    task = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    db.commit()
    return jsonify({'success': True, 'message': 'Task deleted successfully'})

@app.route('/api/tasks/stats')
def task_stats():
    db = get_db()
    stats_query = db.execute("SELECT status, COUNT(*) as count FROM tasks GROUP BY status").fetchall()
    stats = {stat['status']: stat['count'] for stat in stats_query}
    return jsonify(stats)

@app.route('/api/mcp', methods=['GET'])
def get_mcp():
    return jsonify(app.config['SERVERS'])

@app.route('/api/mcp/chat', methods=['POST'])
def chat_with_mcp():
    data = request.get_json()
    message = data.get('message')
    # For now, just echo the message back.
    # In the future, this could interact with the Zomato MCP server.
    reply = f"You said: {message}"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
import unittest
import os
import tempfile
import json
from app import app, init_db, populate_db, get_db

class TaskManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            init_db()
            populate_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Task Manager', response.data)

    def test_add_task_page(self):
        response = self.app.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add New Task', response.data)

    def test_add_task(self):
        response = self.app.post('/add', data=dict(
            title='Test Task',
            description='Test Description',
            start_date='2025-01-01',
            end_date='2025-01-02',
            status='ToDo'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)

    def test_add_task_invalid_date(self):
        response = self.app.post('/add', data=dict(
            title='Test Task',
            description='Test Description',
            start_date='2025-01-02',
            end_date='2025-01-01',
            status='ToDo'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'End date cannot be before the start date.', response.data)

    def test_edit_task_page(self):
        response = self.app.get('/edit/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Edit Task', response.data)

    def test_edit_task(self):
        response = self.app.post('/edit/1', data=dict(
            title='Updated Task',
            description='Updated Description',
            start_date='2025-01-01',
            end_date='2025-01-02',
            status='InProgress'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updated Task', response.data)

    def test_delete_task(self):
        response = self.app.get('/delete/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Complete Project Proposal', response.data)

    def test_get_tasks_api(self):
        response = self.app.get('/api/tasks')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_get_task_api(self):
        response = self.app.get('/api/task/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Complete Project Proposal')

    def test_create_task_api(self):
        new_task = {
            'title': 'New API Task',
            'description': 'New API Description',
            'start_date': '2025-01-05',
            'end_date': '2025-01-06',
            'status': 'ToDo'
        }
        response = self.app.post('/api/tasks', data=json.dumps(new_task), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'New API Task')

    def test_update_task_api(self):
        updated_task = {
            'title': 'Updated API Task'
        }
        response = self.app.put('/api/task/1', data=json.dumps(updated_task), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Updated API Task')

    def test_delete_task_api(self):
        response = self.app.delete('/api/task/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])

if __name__ == '__main__':
    unittest.main()
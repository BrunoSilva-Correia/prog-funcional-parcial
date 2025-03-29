import unittest

from src.core.models import Task
from src.core.tasks import (
    add_task,
    complete_task,
    create_task_completer,
    delete_task,
    filter_tasks,
    format_task,
    process_tasks,
    task_statistics,
    update_task_description,
)


class TestTaskFunctions(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            {"id": 1, "description": "Task 1", "completed": False},
            {"id": 2, "description": "Task 2", "completed": False},
        ]

    def test_add_task(self):
        new_tasks = add_task(self.tasks, "New Task")
        self.assertEqual(len(new_tasks), 3)
        self.assertEqual(new_tasks[2]["description"], "New Task")
        self.assertFalse(new_tasks[2]["completed"])

    def test_complete_task(self):
        completed_tasks = complete_task(self.tasks, 1)
        self.assertTrue(completed_tasks[0]["completed"])
        self.assertFalse(completed_tasks[1]["completed"])

    def test_delete_task(self):
        remaining_tasks = delete_task(self.tasks, 1)
        self.assertEqual(len(remaining_tasks), 1)
        self.assertEqual(remaining_tasks[0]["id"], 2)

    def test_update_task_description(self):
        updated_tasks = update_task_description(self.tasks, 1, "Updated")
        self.assertEqual(updated_tasks[0]["description"], "Updated")
        self.assertEqual(updated_tasks[1]["description"], "Task 2")

    def test_filter_tasks(self):
        completed_tasks = complete_task(self.tasks, 1)
        pending = filter_tasks(completed_tasks, False)
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0]["id"], 2)

    def test_task_statistics(self):
        completed_tasks = complete_task(self.tasks, 1)
        stats = task_statistics(completed_tasks)
        self.assertEqual(stats["total_tasks"], 2)
        self.assertEqual(stats["completed_tasks"], 1)
        self.assertEqual(stats["completion_percentage"], 50.0)

    def test_process_tasks_high_order(self):
        def uppercase_desc(task):
            return {**task, "description": task["description"].upper()}

        processed = process_tasks(self.tasks, uppercase_desc)
        self.assertEqual(processed[0]["description"], "TASK 1")

    def test_create_task_completer_closure(self):
        completer = create_task_completer()
        task = {"id": 5, "description": "Test", "completed": False}
        completed_task = completer(task, 5)
        self.assertTrue(completed_task["completed"])

    def test_format_task_lambda(self):
        task = {"id": 1, "description": "Test", "completed": True}
        formatted = format_task(task)
        self.assertEqual(formatted, "1. [X] Test")


if __name__ == "__main__":
    unittest.main()

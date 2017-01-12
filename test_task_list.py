import re

from task import Task
from task_list import TaskList

class TaskListTest:
    def assert_equal(self, a, b):
        if a != b:
            raise ValueError("Expected: {} - Got: {}".format(a, b))

    def run_tests(self):
        for method in dir(self):
            if re.match(r'test_', method):
                getattr(TaskListTest, method)(self)
        print("All tests passed")

    def test_start_with_empty_list(self):
        task_list = TaskList()
        self.assert_equal(0, len(task_list.tasks))

    def test_add_a_task(self):
        task_list = TaskList()
        task = Task()
        self.assert_equal(True, task_list.add_task(task))
        self.assert_equal(1, len(task_list.tasks))







if __name__ == '__main__':

    task_list_tester = TaskListTest()
    task_list_tester.run_tests()

import os.path
import re

from glob import glob
from task import Task
from task_list import TaskList

class TaskListTest:

    def __init__(self):
    
        self.testing_dir = 'test_output'
        
        self.testing_files = [
            '{}/test-a.csv'.format(self.testing_dir) 
        ]


    def assert_equal(self, a, b):
        if a != b:
            raise ValueError("Expected: {} - Got: {}".format(a, b))

    def run_tests(self):
        for method in dir(self):
            if re.match(r'test_', method):
                for testing_file in self.testing_files:
                    if os.path.isfile(testing_file):
                        os.remove(testing_file)
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

    def test_save_list_to_file(self):
        """This is where the output is written. 
        The checks for the valididity of the data are being done manually
        """
        task_list = TaskList()
        task1 = Task()
        output_file_path = self.testing_files[0] 
        task1.set_name('Test Task One')
        task1.set_minutes(30)
        task1.set_notes('This is a great test task')
        task_list.add_task(task1)

        self.assert_equal(True, task_list.save_to_file(output_file_path))
        self.assert_equal(True, os.path.isfile(output_file_path))
        
    def test_read_from_file(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('tests/fixture-1.csv'))
        self.assert_equal(7, len(task_list.tasks))
        self.assert_equal('2017-01-02', str(task_list.tasks[0].date))



if __name__ == '__main__':

    task_list_tester = TaskListTest()
    task_list_tester.run_tests()
    task_list_tester.test_save_list_to_file()


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

    def test_add_a_task(self):
        task_list = TaskList()
        task = Task()
        self.assert_equal(True, task_list.add_task(task))
        self.assert_equal(1, len(task_list.tasks))

    def test_date_list(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('tests/fixture-2.csv'))
        target_date_list = ["2016-01-03", "2016-02-07", "2016-11-12", "2017-01-01", "2017-01-02", "2017-01-03","2017-01-07"]
        self.assert_equal(target_date_list, task_list.date_list())

    def test_durations(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('tests/fixture-2.csv'))
        target_durations = [5, 30, 90, 120]
        self.assert_equal(target_durations, task_list.durations())

    def test_read_from_file(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('tests/fixture-1.csv'))
        self.assert_equal(7, len(task_list.tasks))
        task = task_list.tasks[0]
        self.assert_equal('2017-01-02', str(task.date))
        self.assert_equal('Test Task One', task.name)
        self.assert_equal(30, task.minutes)
        self.assert_equal('This is a wonderful test task', task.notes)

    def test_read_from_file_that_does_not_exist(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('file-that-does-not-exist.csv'))
        self.assert_equal(0, len(task_list.tasks))

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
        
    def test_start_with_empty_list(self):
        task_list = TaskList()
        self.assert_equal(0, len(task_list.tasks))

    def test_read_from_file(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('tests/fixture-1.csv'))
        self.assert_equal(7, len(task_list.tasks))
        task = task_list.tasks[0]
        self.assert_equal('2017-01-02', str(task.date))
        self.assert_equal('Test Task One', task.name)
        self.assert_equal(30, task.minutes)
        self.assert_equal('This is a wonderful test task', task.notes)

    def test_read_from_file_that_does_not_exist(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('file-that-does-not-exist.csv'))
        self.assert_equal(0, len(task_list.tasks))

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
        
    def test_start_with_empty_list(self):
        task_list = TaskList()
        self.assert_equal(0, len(task_list.tasks))

    def test_tasks_for_date(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('tests/fixture-1.csv'))
        self.assert_equal(1, len(task_list.tasks_for_date('2017-01-02')))
        self.assert_equal(3, len(task_list.tasks_for_date('2017-01-03')))

    def test_tasks_for_duration(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('tests/fixture-2.csv'))
        self.assert_equal(2, len(task_list.tasks_for_duration(30)))

    def test_tasks_with_regex(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('tests/fixture-2.csv'))
        self.assert_equal(3, len(task_list.tasks_with_regex('s\w\wG')))

    def test_tasks_with_string(self):
        task_list = TaskList()
        self.assert_equal(True, task_list.read_from_file('tests/fixture-2.csv'))
        self.assert_equal(3, len(task_list.tasks_with_string('slug')))


if __name__ == '__main__':

    task_list_tester = TaskListTest()
    task_list_tester.run_tests()


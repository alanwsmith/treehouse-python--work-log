import re
import datetime

from task import Task

class TaskTest:

    def assert_equal(self, a, b):
        if a != b:
            raise ValueError("Expected: {} - Got: {}".format(a, b))

    def run_tests(self):
        for method in dir(self):
            if re.match(r'test_', method):
                getattr(TaskTest, method)(self)
        print("All tests passed")

    def test_initial_date_is_set_properly(self):
        task = Task()
        test_date = datetime.datetime.now()
        self.assert_equal(test_date.year, task.created.year)
        self.assert_equal(test_date.month, task.created.month)
        self.assert_equal(test_date.day, task.created.day)

    def test_initial_values_are_empty(self):
        task = Task()
        self.assert_equal(None, task.name)
        self.assert_equal(None, task.minutes)
        self.assert_equal(None, task.notes)

    def test_set_name(self):
        task = Task()
        self.assert_equal(True, task.set_name("New Task"))
        self.assert_equal("New Task", task.name)



if __name__ == '__main__':

    task_test = TaskTest()
    task_test.run_tests()



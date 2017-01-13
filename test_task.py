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
        test_date = datetime.date.today()
        self.assert_equal(test_date.year, task.date.year)
        self.assert_equal(test_date.month, task.date.month)
        self.assert_equal(test_date.day, task.date.day)

    def test_initial_values_are_empty(self):
        task = Task()
        self.assert_equal(None, task.name)
        self.assert_equal(None, task.minutes)
        self.assert_equal(None, task.notes)

    def test_set_name(self):
        task = Task()
        self.assert_equal(True, task.set_name("New Task"))
        self.assert_equal("New Task", task.name)

    def test_return_false_for_empty_name(self):
        task = Task()
        self.assert_equal(False, task.set_name(""))

    def test_set_minutes(self):
        task = Task()
        self.assert_equal(True, task.set_minutes(15))
        self.assert_equal(15, task.minutes)

    def test_reject_invalid_minutes(self):
        task = Task()
        self.assert_equal(False, task.set_minutes(""))
        self.assert_equal(False, task.set_minutes(0))

    def test_set_notes(self):
        task = Task()
        self.assert_equal(True, task.set_notes("Quick brown fox"))
        self.assert_equal("Quick brown fox", task.notes)

    def test_skip_empty_notes(self):
        task = Task()
        self.assert_equal(True, task.set_notes(""))
        self.assert_equal(None, task.notes)



if __name__ == '__main__':

    task_test = TaskTest()
    task_test.run_tests()



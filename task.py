import datetime


class Task:

    def __init__(self):
        self.created = datetime.datetime.now()
        self.minutes = None
        self.name = None
        self.notes = None


if __name__ == '__main__':

    from test_task import TaskTest

    task_tester = TaskTest()
    task_tester.run_tests()

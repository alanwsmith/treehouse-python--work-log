class TaskList:

    def __init__(self):
        
        self.tasks = []


if __name__ == '__main__':

    from test_task_list import TaskListTest

    task_list_tester = TaskListTest()
    task_list_tester.run_tests()

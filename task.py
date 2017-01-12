import datetime

class Task:

    def __init__(self):
        self.created = datetime.datetime.now()
        self.minutes = None
        self.name = None
        self.notes = None

    def input_name(self):
        while True:
            if self.set_name(input("> ")):
                break
            else:
                print("That wasn't a valid name. Try again.")



    def set_name(self, name):
        if name == "":
            return False
        else:
            self.name = name
            return True 




if __name__ == '__main__':

    from test_task import TaskTest

    task_tester = TaskTest()
    task_tester.run_tests()

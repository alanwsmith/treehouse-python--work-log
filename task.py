import datetime

class Task:

    def __init__(self):
        self.date = datetime.date.today()
        self.minutes = None
        self.name = None
        self.notes = None

    def display(self):
        print("#" * 70)
        print("Task: {}".format(self.name))
        print("Date: {}".format(str(self.date)))
        print("Duration: {} minutes".format(self.minutes))
        if self.notes:
            print("Notes: {}".format(self.notes))
        print()

    def input_minutes(self):
        while True:
            if self.set_minutes(input("> ")):
                break
            else:
                print("That was an invalid number of minutes. Try again.")

    def input_name(self):
        while True:
            if self.set_name(input("> ")):
                break
            else:
                print("That wasn't a valid name. Try again.")

    def input_notes(self):
        self.set_notes(input("> "))

    def set_date(self, date):
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return True


    def set_minutes(self, minutes):
        """Takes a requested number of minutes. 

        If it's a positive integer, the minutes instance
        varaible is updated and the method returns True. 

        Otherwise, it returns False. 
        """
        try:
            minutes_as_int = int(minutes)
        except ValueError:
            return False
        else:
            if minutes_as_int <= 0:
                return False
            else: 
                self.minutes = minutes_as_int
                return True

    def set_name(self, name):
        """Updates the `name` instance variable
        if a non empty name is passed. 
        """
        if name == "":
            return False
        else:
            self.name = name
            return True 

    def set_notes(self, notes):
        """Sets notes if something is passed.

        Otherwise, leaves them as is
        """
        if not notes == "":
            self.notes = notes
        return True 



if __name__ == '__main__':

    from test_task import TaskTest

    task_tester = TaskTest()
    task_tester.run_tests()

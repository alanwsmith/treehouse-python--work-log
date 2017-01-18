from task import Task
from task_list import TaskList

class Worklog:

    def __init__(self):
        
        self.task_list = TaskList()
        self.data_file = 'data.csv'
        self.task_list.read_from_file(self.data_file)


    def add_item(self):
        task = Task()
        print("What should the name of this task be?")
        task.input_name()
        print("How many minutes did you spend on it?")
        task.input_minutes()
        print("Add any other notes you want here (or just hit Enter/Return if you don't want any).")
        task.input_notes()
        self.task_list.add_task(task)
        self.task_list.save_to_file(self.data_file)
        print("\033c", end="")
        print("Your task has been added!")

    def initial_prompt(self):
        print("\033c", end="")
        print("### Welcome to Worklogger ###")

        while True:
            print()
            print("Choose an option:\n")
            print("  1. Add a new item")
            print("  2. Lookup an item")
            print("  3. Quit\n")
            get_input = input("Enter the number of your selection: ").strip().lower()
            if get_input == '1':
                print("\033c", end="")
                self.add_item()
            elif get_input == '2':
                print("TKTKTKTK: Lookup")
            elif get_input == '3':
                print("Thanks for using Worklogger!")
                break
            else:
                print("\033c", end="")
                print("That wasn't a valid number. Try again.")


    def run_test(self):
        import sys
        system_input = sys.stdin
        test_input = open('tests/basic.txt', 'r')
        sys.stdin = test_input
        self.initial_prompt()
        test_input.close()
        sys.stdin = system_input


if __name__ == '__main__':
    
    wl = Worklog()
    wl.initial_prompt()
    # wl.run_test()



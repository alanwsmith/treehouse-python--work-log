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
                self.lookup_menu()
            elif get_input == '3':
                print("Thanks for using Worklogger!")
                break
            else:
                print("\033c", end="")
                print("That wasn't a valid number. Try again.")

    def lookup_menu(self):
        print("\033c", end="")
        
        while True:

            print("Lookup task by:\n")
            print("  1. Date")
            print("  2. Time spent")
            print("  3. Exact text search")
            print("  4. Pattern text search")
        
            get_input = input("Enter the number of your selection: ").strip().lower()

            if get_input == '1':
                self.search_by_date()
                break
            elif get_input == '2':
                print("Search by time spent")
                break
            elif get_input == '3': 
                print("Search by exact text string")
                break
            elif get_input == '4':
                print("Search by RegEx Pattern")
                break
            else:
                print("\033c", end="")
                print("That wasn't a valid number. Try again")

    def search_by_date(self):
        print("\033c", end="")
        print("Choose from one of the following dates: ")
        for date_index, date_string in enumerate(self.task_list.date_list()):
            print("  {}. {}".format(date_index + 1, date_string))
        while True:
            print()
            get_input = input("Enter the number for the date you wish to see: ").strip().lower()
            try:
                input_as_int = int(get_input)
            except ValueError:
                print("That isn't a valid number. Try again.")
                continue
            else:
                if input_as_int >= 0 and input_as_int < len(self.task_list.date_list()):
                    print("Got it!")
                    break
                else:
                    print("That isn't a valid option. Try again.")
                    continue




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



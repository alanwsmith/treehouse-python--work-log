from task import Task
from task_list import TaskList

class Worklog:

    def __init__(self):
        
        self.task_list = TaskList()
        self.data_file = 'data.csv'
        self.task_list.read_from_file(self.data_file)


    def initial_prompt(self):
        which_number = None
        while which_number == None :
            print("Enter '1' to add a new item or '2' to look one up")
            get_input = input("> ").strip().lower()
            if get_input == '1' or get_input == '2':
                which_number = int(get_input)
            else:
                print("That wasn't a valid number. Try again")

        if which_number == 1:
            task = Task()
            print("What should the name of this task be?")
            task.input_name()
            print("How many minutes did you spend on it?")
            task.input_minutes()
            print("Add any other notes you want here (or just hit Enter/Return if you don't want any).")
            task.input_notes()

            self.task_list.add_task(task)
            self.task_list.save_to_file(self.data_file)

            print(self.task_list)

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
    #wl.initial_prompt()
    wl.run_test()



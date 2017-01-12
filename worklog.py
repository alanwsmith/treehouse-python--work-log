from task import Task

class Worklog:

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


if __name__ == '__main__':
    
    wl = Worklog()
    wl.initial_prompt()



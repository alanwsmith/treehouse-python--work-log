
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
            name_of_task = input("What's the name of the new task? ")
            minutes_spent = input("How many minutes did you spend on it? ")
            other_notes = input("Enter any other notes you'd like to keep about the task: ")




if __name__ == '__main__':
    
    wl = Worklog()
    wl.initial_prompt()



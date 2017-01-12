import logging

class Interface:

    def __init__(self):
        self.test_input = []
        self.state = 'start'
        self.last_input = None
         

    def prompt_for_add_or_lookup(self):
        self._add_or_lookup = False
        while not self._add_or_lookup:
            print(self.output_display())
            check_input = input("Enter number for you choice: ").strip().lower()
            if check_input == 1 or check_input == 2:
                self._add_or_lookup

    def output_display(self):
        template_file = open("templates/{}.txt".format(self.state))
        data = template_file.read()
        template_file.close()
        return data 

    def run(self):
        while self.last_input == None:
            test_number = input(self.output_display())
            if self.is_number_in_range(number=test_number, lower_bound=1, upper_bound=2):
                self.last_input = test_number

         input(self.output_display())
        if not self.is_number_in_range(number = choice, lower_bound = 1, upper_bound = 2):
            print("Invalid")
        else:
            print("Valid")



    def is_number_in_range(self, **kwargs):
        """Checks to see if a given number is in a range of 
        numbers.

        This will also return false if something other than
        a number is passed as the first parameter so it works
        as error checking as well.
        """
        try:
            number_as_int = int(kwargs['number'])
        except ValueError:
            return False
        else:
            if number_as_int in range(kwargs['lower_bound'], kwargs['upper_bound'] + 1):
                return True
            else:
                return False

            



if __name__ == '__main__':
    
    from test_interface import InterfaceTest
    interface_test = InterfaceTest()
    interface_test.run_tests()

    interface = Interface()
    interface.run()


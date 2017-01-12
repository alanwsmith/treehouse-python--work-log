import logging


class Interface:
    
    def state(self):
        return 'start'

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



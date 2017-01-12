import re

from interface import Interface 

class InterfaceTest:

    def run_tests(self):
        for method in dir(self):
            if re.match(r'test_', method):
                getattr(InterfaceTest, method)(self)

        print("All tests passed")

    def assert_equal(self, a, b):
        if a != b:
            raise ValueError("Expected: {} - Got: {}".format(a, b))
        

    def test_initial_display(self):
        interface = Interface()
        self.assert_equal('start', interface.state())

    def test_is_number_in_range(self):
        interface = Interface()
        self.assert_equal(True, interface.is_number_in_range(number=1, lower_bound=1, upper_bound=2))
        self.assert_equal(True, interface.is_number_in_range(number=2, lower_bound=1, upper_bound=2))
        self.assert_equal(True, interface.is_number_in_range(number=5, lower_bound=4, upper_bound=5))
        self.assert_equal(True, interface.is_number_in_range(number=5, lower_bound=4, upper_bound=7))
        self.assert_equal(False, interface.is_number_in_range(number=5, lower_bound=1, upper_bound=4))
        self.assert_equal(False, interface.is_number_in_range(number=0, lower_bound=1, upper_bound=4))
        self.assert_equal(False, interface.is_number_in_range(number='', lower_bound=1, upper_bound=4))
        self.assert_equal(False, interface.is_number_in_range(number='a', lower_bound=1, upper_bound=4))



if __name__ == '__main__':

    tester = InterfaceTest()
    tester.run_tests()



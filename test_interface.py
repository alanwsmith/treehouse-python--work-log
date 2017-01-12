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


if __name__ == '__main__':

    tester = InterfaceTest()
    tester.run_tests()



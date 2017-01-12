from interface import Interface

class Worklog:
    
    def run(self):
        interface = Interface()
        print(interface.state())


if __name__ == '__main__':
    
    wl = Worklog()
    wl.run()


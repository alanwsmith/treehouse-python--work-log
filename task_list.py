import csv
import os.path

from task import Task

class TaskList:

    def __init__(self):
        
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return True

    def date_list(self):
        date_list = []
        for task in self.tasks:
            check_date = str(task.date)
            if check_date not in date_list:
                date_list.append(check_date)
        return date_list 

    def read_from_file(self, file_path):
        """Turns a CSV file into a set of tasks. 

        If the file does not exist, the tasks
        instance variable simple remains empty.
        """
        if not os.path.isfile(file_path):
            return True
        with open(file_path, 'r') as csvfile:
            task_reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
            for row in task_reader:
                task = Task()
                task.set_date(row[0])
                task.set_name(row[1])
                task.set_minutes(int(row[2]))
                task.set_notes(row[3])
                self.tasks.append(task)
        return True 

    def save_to_file(self, file_path):
        with open(file_path, 'w') as csvfile:
            taskwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for task in self.tasks:
                taskwriter.writerow([task.date, task.name, task.minutes, task.notes])
        return True




if __name__ == '__main__':

    from test_task_list import TaskListTest

    task_list_tester = TaskListTest()
    task_list_tester.run_tests()
    task_list_tester.test_save_list_to_file()

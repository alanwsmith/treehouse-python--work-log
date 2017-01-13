import csv

class TaskList:

    def __init__(self):
        
        self.tasks = []

    def add_task(self, task):
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

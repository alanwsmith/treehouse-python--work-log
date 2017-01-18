import csv
import os.path
import re

from task import Task


class TaskList:

    def __init__(self):

        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return True

    def date_list(self):
        """TODO: This should be refacoted to be called `dates`
        """
        date_list = []
        for task in self.tasks:
            check_date = str(task.date)
            if check_date not in date_list:
                date_list.append(check_date)
        return sorted(date_list)

    def durations(self):
        durations = []
        for task in self.tasks:
            check_duration = task.minutes
            if check_duration not in durations:
                durations.append(check_duration)
        return sorted(durations)

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
            taskwriter = csv.writer(
                csvfile,
                delimiter='\t',
                quotechar='|',
                quoting=csv.QUOTE_MINIMAL)
            for task in self.tasks:
                taskwriter.writerow(
                    [task.date, task.name, task.minutes, task.notes])
        return True

    def tasks_for_date(self, date_string):
        matching_tasks = []
        for task in self.tasks:
            if date_string == str(task.date):
                matching_tasks.append(task)
        return matching_tasks

    def tasks_for_duration(self, duration):
        tasks = []
        for task in self.tasks:
            if int(duration) == int(task.minutes):
                tasks.append(task)
        return tasks

    def tasks_with_regex(self, regex):
        tasks = []
        notes_as_string = ""
        for task in self.tasks:
            # Load in the actual notes if they exist so you can do
            # the elif later
            if task.notes:
                notes_as_string = task.notes
            if re.search(r'%s' % regex, task.name, re.IGNORECASE):
                tasks.append(task)
            elif re.search(r'%s' % regex, notes_as_string, re.IGNORECASE):
                tasks.append(task)
        return tasks

    def tasks_with_string(self, string):
        tasks = []
        notes_as_string = ""
        for task in self.tasks:
            # Load in the actual notes if they exist so you can do
            # the elif later
            if task.notes:
                notes_as_string = task.notes
            if re.search(string, task.name, re.IGNORECASE):
                tasks.append(task)
            elif re.search(string, notes_as_string, re.IGNORECASE):
                tasks.append(task)
        return tasks


if __name__ == '__main__':

    from test_task_list import TaskListTest

    task_list_tester = TaskListTest()
    task_list_tester.run_tests()

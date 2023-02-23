from task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {self.name.task.details()} is added to the section"

    def complete_task(self, task_name):
        if task_name in self.tasks:
            pass

    def clean_section(self):
        cleared_tasks = len(self.tasks)
        self.tasks = []
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        output = [f'Section {self.name}:']
        for current_task in self.tasks:
            output.append(current_task)
        return '\n'.join(output)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

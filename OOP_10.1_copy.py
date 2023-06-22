'''The code defines classes and uses them to create instances of QA (Quality Assurance) and Manager objects. These objects represent users with specific roles and behaviors. After creating instances of these objects, the code performs some actions and prints out the results.

We are collecting user input for various attributes such as test names, expected actions, and tasks. Then, you create a QA object using the input values for the QA user and a Manager object for the manager.

Here's a breakdown of the code:

User class: This serves as the base class for both QA and Manager. It has attributes for username and expected_action. The perform_action() method prints out the username and the expected action.
QA class: This is a subclass of User with an additional attribute, tasks, which is initialized as an empty list. It also has a method set_task() to add tasks to the tasks list.

Manager class: This is a subclass of User. It overrides the perform_action() method to print a specific message indicating the manager is busy and suggests writing an email with any questions.
The code collects user input for the QA and Manager details.
It creates a QA object qa using the input values for the QA user.

The qa.get_username() method is called to retrieve and print the QA user's username.
The qa.set_username() method is called to update the QA user's username based on the input value, capitalizing it.
The qa.perform_action() method is called to print the QA user's username and expected action.
The qa.set_task() method is called to add the input task to the QA user's tasks list.

The tasks list of the QA user is printed.
A Manager object pm is created using the input values for the manager.
The pm.get_username() method is called to retrieve and print the manager's username.
The pm.set_username() method is called to update the manager's username based on the input value, capitalizing it.
The pm.perform_action() method is called to print the message indicating the manager is busy.'''

input_qa_name= input("Введіть ім'я тестувальника: ")
input_pm_name = input("Введіть нове ім'я менеджера: ")
input_qa_expected_action = input("Введіть очікувану дію для тестувальника: ")
input_pm_expected_action = input("Введіть очікувану дію для менеджера: ")
input_qa_task = input("Введіть поставлену задачу тестувальнику: ")


class User:
    def __init__(self, username, expected_action):
        self._username = username
        self._expected_action = expected_action

    def perform_action(self):
        print(f'{self._username} виконує дію: \'{self._expected_action}\'')

    def get_username(self):
        return self._username

    def set_username(self, value):
        self._username = value
        self._username = self._username.split(" ")[0].capitalize() + ' ' + self._username.split(" ")[1].capitalize()

class QA(User):
    def __init__(self,_username, expected_action,tasks = []):
        super().__init__(_username, expected_action)
        self.tasks = tasks

    def set_task(self, task):
        self.tasks.append(task)

class Manager(User):
    def __init__(self,username, expected_action):
        super().__init__(username, expected_action)

    def perform_action(self):
        print('Зайнятий. Напишіть мені листа з Вашим питанням')

qa = QA(input_qa_name, input_qa_expected_action)
print(qa.get_username())
qa.set_username(input_qa_name)
print(qa.get_username())
qa.perform_action()
print(qa.tasks)
qa.set_task(input_qa_task)
print(qa.tasks)

pm = Manager(input_pm_name, input_pm_expected_action)
print(pm.get_username())
pm.set_username(input_pm_name)
print(pm.get_username())
pm.perform_action()
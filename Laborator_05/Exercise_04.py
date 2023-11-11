'''
Build an employee hierarchy with a base class Employee.
Create subclasses for different types of employees like Manager, Engineer, and Salesperson.
Each subclass should have attributes like salary and methods related to their roles.
'''
from datetime import datetime


class Employee:
    existing_id = set()
    def __init__(self, id, name, age, start_date, free_days):
        if id in Employee.existing_id:
            raise ValueError(f"The id {id} is already used.")
        self.id = id
        Employee.existing_id.add(id)
        self.name = name
        self.age = age
        self.start_date = start_date
        self.free_days = free_days

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_start_date(self):
        return self.start_date

    def use_free_day(self, days=1):
        if self.free_days >= days:
            self.free_days -= days
        else:
            raise ValueError("Insufficient free days")

    def add_free_days(self, days):
        self.free_days += days

    def get_free_day_balance(self):
        return self.free_days

    def estimate_salary(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def increase_salary(self, amount):
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_years_of_experience(self):
        return datetime.now().year - self.start_date.year



class Manager(Employee):
    def __init__(self, id, name, age, start_date, free_days, salary, bonus, department_managed, budget_authority):
        super().__init__(id, name, age, start_date, free_days)
        self.__salary = salary
        self.__bonus = bonus
        self.department_managed = department_managed
        self.budget_authority = budget_authority
        self.subordinates = []  # List of Employee objects
        self.performance_reviews = {}  # Dictionary to hold performance reviews
        self.decision_making_authority = []  # List of areas with decision-making authority
        self.managerial_training = []  # List of completed managerial training sessions
        self.meeting_schedule = []  # List of scheduled meetings

    def estimate_salary(self):
        return self.get_years_of_experience() * 1000 + len(self.subordinates) * 100 + len(self.decision_making_authority) * 100 + len(self.managerial_training) * 100

    def increase_salary(self):
        if self.get_years_of_experience() < 5 and len(self.subordinates) < 10 and len(self.decision_making_authority) < 3 and len(self.managerial_training) < 5:
            self.__salary += 1000
        else:
            self.__salary += 2000

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def remove_subordinate(self, employee_id):
        self.subordinates = [e for e in self.subordinates if e.get_id() != employee_id]

    def add_performance_review(self, employee_id, review):
        self.performance_reviews[employee_id] = review

    def make_decision(self, decision_area):
        self.decision_making_authority.append(decision_area)

    def add_training_session(self, training_session):
        self.managerial_training.append(training_session)

    def schedule_meeting(self, meeting_details):
        self.meeting_schedule.append(meeting_details)


class Engineer(Employee):
    def __init__(self, id, name, age, start_date, free_days, salary, engineering_field, certifications, current_project, work_hours_per_week):
        super().__init__(id, name, age, start_date, free_days)
        self.__salary = salary
        self.engineering_field = engineering_field
        self.certifications = certifications
        self.current_project = current_project
        self.work_hours_per_week = work_hours_per_week  # Average number of work hours per week
        self.tasks = []  # Initialize with an empty list of tasks

    def estimate_salary(self):
        self.get_years_of_experience() * 1000 + self.work_hours_per_week * 10

    def increase_salary(self):
        if self.work_hours_per_week < 40 and self.get_years_of_experience() < 5 and len(self.certifications) < 3:
            self.__salary += 500
        else:
            self.__salary += 1000

    def add_certification(self, certification):
        self.certifications.append(certification)

    def assign_project(self, project):
        self.current_project = project

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found.")

    def get_project_details(self):
        return self.current_project

    def get_work_hours(self):
        return self.work_hours_per_week

    def get_pending_tasks(self):
        return self.tasks


class Salesperson(Employee):
    def __init__(self, id, name, age, start_date, free_days, salary, sales_target, commission_rate):
        super().__init__(id, name, age, start_date, free_days)
        self.__salary = salary
        self.sales_target = sales_target  # The sales target for the salesperson
        self.commission_rate = commission_rate  # Commission rate as a percentage
        self.current_sales = 0  # Total sales amount made by the salesperson
        self.clients = []  # List of clients

    def estimate_salary(self):
        self.get_years_of_experience() * 1000 + self.current_sales * self.commission_rate / 100

    def increase_salary(self):
        if self.get_years_of_experience() < 5 and self.current_sales > self.sales_target:
            self.__salary += 500
        else:
            self.__salary += 1000

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, client):
        if client in self.clients:
            self.clients.remove(client)

    def record_sale(self, sale_amount):
        self.current_sales += sale_amount

    def calculate_commission(self):
        return (self.current_sales * self.commission_rate) / 100

    def check_sales_target(self):
        return self.current_sales >= self.sales_target

    def get_client_list(self):
        return self.clients



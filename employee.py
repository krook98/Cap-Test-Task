from datetime import datetime

class Employee:
    def __init__(self, first_name, last_name, age, job, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.total_salary = salary
        self.department = ""

    def __repr__(self):
        return f'-> {self.last_name} {self.first_name} | {self.age} | {self.job} | {self.salary} | {self.total_salary} | {self.department}'

    def apply_bonus(self, bonus):
        self.total_salary = self.salary + bonus
        return self.total_salary

    def assign_to_department(self, department_name):
        self.department = department_name

    def remove_from_department(self):
        self.department = ''

    def get_department(self):
        return self.department

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def identify_by_name(self, full_name):
        my_full_name = f'{self.first_name} {self.last_name}'
        if my_full_name == full_name:
            return self
        else:
            return None

    def get_invoice(self):
        invoice_title = f'{self.last_name}_invoice.txt'
        with open(invoice_title, 'w') as f:
            f.write(f'First Name: {self.first_name} | ')
            f.write(f'Last Name: {self.last_name}\n')
            f.write(f'Job Title: {self.job}\n')
            f.write(f'Invoice Date: {datetime.now()}\n')
            f.write(f'Salary: {self.salary}\n')
            f.write(f'Salary with bonuses: {self.total_salary}\n')
            f.write('\n')

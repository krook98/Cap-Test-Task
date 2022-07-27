from employee import Employee
from department import Department


class Company:
    def __init__(self):
        self.departments = []
        self.employees = []

    def add_department(self, name):
        department = Department(name)
        self.departments.append(department)

    def remove_department(self, name):
        dep = self.find_department_by_name(name)
        if dep is None:
            print('No such department')
        else:
            dep.remove_all_employees()
            self.departments.remove(dep)

    def find_department_by_name(self, name):
        for dep in self.departments:
            if dep.get_name() == name:
                return dep
        return None

    def add_new_employee(self, first_name, last_name, age, job, salary):
        employee = Employee(first_name, last_name, age, job, salary)
        self.employees.append(employee)

    def remove_employee(self, first_name, last_name):
        e = self.find_employee_by_name(first_name, last_name)
        if e is None:
            print('No such employee')
        else:
            dep_name = e.get_department()
            if dep_name != "":
                dep = self.find_department_by_name(dep_name)
                dep.remove_employee(e)
            self.employees.remove(e)

    def find_employee_by_name(self, first_name, last_name):
        full_name = f'{first_name} {last_name}'
        for e in self.employees:
            if e.get_full_name() == full_name:
                return e
        return None

    def assign_employee_to_department(self, department_name, first_name, last_name):
        dep = self.find_department_by_name(department_name)
        if dep is None:
            print('No such department')
        else:
            e = self.find_employee_by_name(first_name, last_name)
            if e is None:
                print('No such employee')
            else:
                dep.add_employee(e)

    def remove_employee_from_department(self, department_name, first_name, last_name):
        dep = self.find_department_by_name(department_name)
        if dep is None:
            print('No such department')
        else:
            e = self.find_employee_by_name(first_name, last_name)
            if e is None:
                print('No such employee')
            else:
                dep.remove_employee(e)

    def apply_bonus_for_department(self, department_name, bonus):
        dep = self.find_department_by_name(department_name)
        dep.apply_bonus_for_all(bonus)

    def apply_bonus_for_employee(self, first_name, last_name, bonus):
        e = self.find_employee_by_name(first_name, last_name)
        e.apply_bonus(bonus)

    def print_all_departments(self):
        print('The list of all departments: ')
        for dep in self.departments:
            print(dep)

    def print_all_employees(self):
        print('The list of all employees in the company: ')
        for e in self.employees:
            print(e)

    def print_all_employees_in_department(self, dep_name):
        print(f'The list of all employees in {dep_name}: ')
        dep = self.find_department_by_name(dep_name)
        if dep is None:
            print(f'The name {dep_name} hasn\'t been found')
        else:
            dep.display_employees()

    def find_employee_location(self, first_name, last_name):
        full_name = f'{first_name} {last_name}'
        for dep in self.departments:
            e = dep[full_name]
            if e is not None:
                print(f'Found in department: {dep.get_name()}')
                return True
        for e in self.employees:
            if e.identify_by_name(full_name) is not None:
                print(f'Found as unassigned.')
                return True
        print('The employee has not been found.')
        return False

    def get_invoice(self, first_name, last_name):
        try:
            e = self.find_employee_by_name(first_name, last_name)
        except AttributeError:
            print('No such employee')
        else:
            e.get_invoice()

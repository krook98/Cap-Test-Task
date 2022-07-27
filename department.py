from employee import Employee


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def __repr__(self):
        return f'-> {self.name}'

    def __getitem__(self, full_name):
        for e in self.employees:
            result = e.identify_by_name(full_name)
            if result is not None:
                return result
        return None

    def display_employees(self):
        print(self.employees)

    def add_employee(self, employee):
        employee.assign_to_department(self.name)
        self.employees.append(employee)

    def remove_employee(self, employee):
        employee.remove_from_department()
        self.employees.remove(employee)

    def remove_all_employees(self):
        for e in self.employees:
            self.remove_employee(e)

    def apply_bonus_for_all(self, bonus):
        for employee in self.employees:
            employee.apply_bonus(bonus)

    def get_name(self):
        return self.name




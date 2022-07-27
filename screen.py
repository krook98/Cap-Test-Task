from company import Company


class Screen:
    def __init__(self):
        self.company = Company()
        self.choice = 0
        self.active = True

    def start(self):
        print('Welcome to Company Manager app.')
        while self.active:
            self.show_menu()
            self.manage_choice()

    def show_menu(self):
        print('\nChoose one of the options below:')
        options_msg = '1. print all departments\n'
        options_msg += '2. add new department\n'
        options_msg += '3. remove department\n'
        options_msg += '4. add new employee\n'
        options_msg += '5. remove employee\n'
        options_msg += '6. assign employee to department\n'
        options_msg += '7. remove employee from department\n'
        options_msg += '8. apply bonus for all employees in department\n'
        options_msg += '9. apply bonus for particular employee\n'
        options_msg += '10. print all employees\n'
        options_msg += '11. print all employees in particular department\n'
        options_msg += '12. find employee\n'
        options_msg += '13. print invoice\n'
        options_msg += '14. show all options again\n'
        options_msg += '15. exit\n'
        try:
            self.choice = int(input(options_msg))
        except ValueError:
            print('Enter number in 1 to 15 range.')
            self.show_menu()

    def manage_choice(self):
        if self.choice == 1:
            self.company.print_all_departments()
        elif self.choice == 2:
            name = input('Enter department name: ')
            self.company.add_department(name)
        elif self.choice == 3:
            name = input('Enter department name: ')
            self.company.remove_department(name)
        elif self.choice == 4:
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            age = int(input('Enter age: '))
            job = input('Enter job: ')
            salary = float(input('Enter salary: '))
            self.company.add_new_employee(first_name, last_name, age, job, salary)
        elif self.choice == 5:
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            self.company.remove_employee(first_name, last_name)
        elif self.choice == 6:
            department_name = input('Enter department name: ')
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            self.company.assign_employee_to_department(department_name, first_name, last_name)
        elif self.choice == 7:
            department_name = input('Enter department name: ')
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            self.company.remove_employee_from_department(department_name, first_name, last_name)
        elif self.choice == 8:
            department_name = input('Enter department name: ')
            bonus = float(input("Enter bonus: "))
            self.company.apply_bonus_for_department(department_name, bonus)
        elif self.choice == 9:
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            bonus = float(input("Enter bonus: "))
            self.company.apply_bonus_for_employee(first_name, last_name, bonus)
        elif self.choice == 10:
            self.company.print_all_employees()
        elif self.choice == 11:
            department_name = input('Enter department name: ')
            self.company.print_all_employees_in_department(department_name)
        elif self.choice == 12:
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            self.company.find_employee_location(first_name, last_name)
        elif self.choice == 13:
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            self.company.get_invoice(first_name, last_name)
        elif self.choice == 14:
            pass
        elif self.choice == 15:
            self.active = False
        else:
            print('Enter number in 1 to 15 range.')
            self.show_menu()

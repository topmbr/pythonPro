import json

class Employee:
    def __init__(self, first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.age}, {self.position})"

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "position": self.position
        }

    @staticmethod
    def from_dict(data):
        return Employee(data['first_name'], data['last_name'], data['age'], data['position'])

class EmployeeManager:
    def __init__(self, filename):
        self.filename = filename
        self.employees = self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Employee.from_dict(emp) for emp in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump([emp.to_dict() for emp in self.employees], file, indent=4)

    def add_employee(self, employee):
        self.employees.append(employee)

    def edit_employee(self, last_name, updated_employee):
        for i, emp in enumerate(self.employees):
            if emp.last_name == last_name:
                self.employees[i] = updated_employee
                return True
        return False

    def delete_employee(self, last_name):
        self.employees = [emp for emp in self.employees if emp.last_name != last_name]

    def find_by_last_name(self, last_name):
        return [emp for emp in self.employees if emp.last_name == last_name]

    def find_by_age(self, age):
        return [emp for emp in self.employees if emp.age == age]

    def find_by_last_name_starting_with(self, letter):
        return [emp for emp in self.employees if emp.last_name.startswith(letter)]

def main():
    filename = input("Enter the filename to load/save employee data: ")
    manager = EmployeeManager(filename)

    while True:
        print("\nOptions:")
        print("1. Add Employee")
        print("2. Edit Employee")
        print("3. Delete Employee")
        print("4. Find Employee by Last Name")
        print("5. Find Employees by Age")
        print("6. Find Employees by Last Name Starting with a Letter")
        print("7. Save Data")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = int(input("Age: "))
            position = input("Position: ")
            manager.add_employee(Employee(first_name, last_name, age, position))

        elif choice == '2':
            last_name = input("Enter the last name of the employee to edit: ")
            first_name = input("New First Name: ")
            age = int(input("New Age: "))
            position = input("New Position: ")
            updated_employee = Employee(first_name, last_name, age, position)
            if not manager.edit_employee(last_name, updated_employee):
                print("Employee not found.")

        elif choice == '3':
            last_name = input("Enter the last name of the employee to delete: ")
            manager.delete_employee(last_name)

        elif choice == '4':
            last_name = input("Enter the last name to search: ")
            results = manager.find_by_last_name(last_name)
            for emp in results:
                print(emp)

        elif choice == '5':
            age = int(input("Enter the age to search: "))
            results = manager.find_by_age(age)
            for emp in results:
                print(emp)

        elif choice == '6':
            letter = input("Enter the starting letter of last names to search: ")
            results = manager.find_by_last_name_starting_with(letter)
            for emp in results:
                print(emp)

        elif choice == '7':
            manager.save_to_file()

        elif choice == '8':
            manager.save_to_file()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

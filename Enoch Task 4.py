class Employee:
    def __init__(self, name, emp_id, department, job_title):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.job_title = job_title

    def display_info(self):
        print("Name:", self.name)
        print("ID Number:", self.emp_id)
        print("Department:", self.department)
        print("Job Title:", self.job_title)
        print("-" * 30)

def main():
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    employee1.display_info()
    employee2.display_info()
    employee3.display_info()
main()

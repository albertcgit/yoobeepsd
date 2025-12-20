#Purpose:
#The purpose of this project is to demonstrate usage of class inheritance.

#Overall Design:
#The program uses a parent class called Person. Other classes like Student
#and Staff inherit from Person. The Staff class also has two child classes,
#General and Academic. Each class adds its own data. I implemented in a single
#python file to exclude importing.

#Defining Superclass
class Person:
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}"

#Defining Child classes
class Student(Person):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name) #Inherit/initialize Person class' attributes
        self.student_id = student_id

    def display_info(self):
        return f"{super().display_info()}, Student ID: {self.student_id}"

class Staff(Person):
    def __init__(self, person_id, name, staff_id, tax_num):
        super().__init__(person_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_info(self):
        return (
            f"{super().display_info()}, "
            f"Staff ID: {self.staff_id}, Tax Number: {self.tax_num}"
        )

class General(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, rate_of_pay):
        super().__init__(person_id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay

    def display_info(self):
        return f"{super().display_info()}, Rate of Pay: {self.rate_of_pay}"

class Academic(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, publications):
        super().__init__(person_id, name, staff_id, tax_num)
        self.publications = publications

    def display_info(self):
        return f"{super().display_info()}, Publications: {self.publications}"

if __name__ == "__main__":

    #Create 1 object for each class
    person = Person(1, "MJ")
    student = Student(2, "Kobe", "S1")
    staff = Staff(3, "Lebron", "ST1", "TAXST1")
    general_staff = General(4, "Carmelo", "GST1", "TAXGST1", 28.75)
    academic_staff = Academic(5, "Luka", "AST1", "TAXAST1", 15)

    # Display all objects
    print(person.display_info())
    print(student.display_info())
    print(staff.display_info())
    print(general_staff.display_info())
    print(academic_staff.display_info())
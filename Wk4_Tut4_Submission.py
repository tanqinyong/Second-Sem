# class Person:
#     def __init__(self,nric,name):
#         self.__nric = nric
#         self.__name = name
#
#     def set_name(self,name):
#         self.__name = name
#
#     def set_nric(self,nric):
#         self.__nric = nric
#
#     def get_name(self):
#         return self.__name
#
#     def get_nric(self):
#         return self.__nric
#
#     def __str__(self):
#         s = "Name:{} NRIC:{}".format(self.__name,self.__nric)
#         return s
#
#
# class Student(Person):
#
#     def __init__(self,nric,name,gpa):
#         Person.__init__(self,nric,name)
#         self.__gpa = gpa
#
#     def set_gpa(self,gpa):
#         self.__gpa = gpa
#
#     def get_gpa(self):
#         return self.__gpa
#
#     def __str__(self):
#         s = "Name:{} NRIC:{} GPA:{}".format(self.get_name(),self.get_nric(),self.__gpa)
#         return s
#
#
# class Employee(Person):
#
#     def __init__(self,nric,name,salary):
#         Person.__init__(self,nric,name)
#         self.__salary = salary
#
#     def set_salary(self,salary):
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#     def __str__(self):
#         s = "Name:{} NRIC:{} Salary:{}".format(self.get_name(),self.get_nric(),self.__salary)
#         return s
#
#
# E1 = Employee("S222344J", "Leatherface", 4000)
# S1 = Student("S123949G", "Bayushka", 4.0)
# students = []
# employees = []
#
# print(E1)
# condition = "Y"
# while condition.upper() == "Y":
#     nric = input("Enter NRIC: ")
#     name = input("Enter Name: ")
#     type = input("Student or Employee? (S or E): ")
#     if type.upper() == "E":
#         salary = float(input('Enter Salary: '))
#         E = Employee(nric,name,salary)
#         employees.append(E)
#     elif type.upper() == "S":
#         gpa = float(input('Enter GPA: '))
#         S = Student(nric,name,gpa)
#         students.append(S)
#     condition = input("Do you want to continue to enter another student or employee? (Y or N)")
#
# print("===== Student =====")
# for student in students:
#     print(student)
# print("===== Employee =====")
# for employee in employees:
#     print(employee)

studentList = []
employeeList = []


def is_nric_valid(s):
    valid = False
    if len(s)== 9:
        if s[0].upper() == 'S' or s[0].upper() == 'T':
            if s[-1].isalpha():
                if s[1:-1].isdigit():
                    valid = True

    return valid


def is_gpa_valid(gpa):
    valid = False
    if 0 <= gpa <= 4:
        valid = True
    return valid

while True:
    while True:
        nric = input('Enter NRIC: ')
        nric_valid = is_nric_valid(nric)
        if nric_valid == False:
            print("Invalid NRIC")
        else:
            break

    name = input('Enter Name: ')
    type = input('Student or Employee? (S or E): ')

    if type.lower() == 'e':
        salary = float(input('Enter salary: $'))

        while salary <= 0:
            print('Salary must be greater than $0')
            salary = float(input('Enter Salary: $'))

        e2 = Employee(nric, name, salary)
        employeeList.append(e2)

    elif type.lower() == 's':
        while True:
            gpa = float(input('Enter GPA: '))



        s1 = Student(nric, name, gpa)

    con = input('Do you want to continue to enter another Student or Employee? (Y or N): ')

    if con.lower() == 'n':
        break

print('===== Student =====')
for i in studentList:
    print(i)

print('===== Employee =====')
for e in employeeList:
    print(e)

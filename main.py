class Student:
    def __init__(self,student_id,name,age,course,marks):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.course=course
        self.marks=marks

    
    def display(self):
        print("ID :",self.student_id)
        print("name :",self.name)
        print("age :",self.age)
        print("course :",self.course)
        print("marks :",self.marks)
        
        
    def grade(self):
        if self.marks>=90:
            print("A+")
        elif self.marks>=80:
            print("A")
        elif self.marks>=70:
            print("B")
        elif self.marks>=60:
            print("C")
        elif 33<=self.marks<=59:
            print("D")
        else:
            print("Fail")
            
    def is_pass(self):
        if self.marks>=33:
            print("Student is pass")
        else:
            print("Student is fail")
    
    students = []

    def add_student(self):
        student_id = int(input("Enter ID of student: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter student course: ")
        marks = float(input("Enter student marks: "))

        student = Student(student_id, name, age, course, marks)

        students.append(student)
        print("Student added successfully")
        print("tudent added successfully that is not norml for you it can we us")
    
    def display_students():

     if len(students) == 0:
        print("No students available")
        return student 

    for student in students:
        student.display()
        student.grade()
        student.is_pass() #that is mainly important for learning taht is not for me and you 
        
        
#     def search_student():
# s1=Student(1,"rohan",16,"mathamtics",89)
# s2=Student(2,"gagan",32,"physics",53)
# s3=Student(3,"moha",18,"machine learning",23)

# s1.display()
# s1.grade()
# s1.is_pass()
# add_student()




#thai tis mainly it nthe part of the main ldea in the featuren in ti i 
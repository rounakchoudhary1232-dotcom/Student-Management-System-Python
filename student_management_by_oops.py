class Student:
    def __init__(self, roll, name, father, mother, chemistry, physics, maths):
        self.roll = roll
        self.name = name
        self.father = father
        self.mother = mother
        self.chemistry = chemistry
        self.physics = physics
        self.maths = maths

    def avg(self):
        return (self.chemistry + self.physics + self.maths) / 3

    def grade(self):
        average = self.avg()
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 45:
            return "C"
        else:
            return "D"

    def display_info(self):
        print("roll: ", self.roll)
        print("name: ", self.name)
        print("father: ", self.father)
        print("mother: ", self.mother)
        print("chemistry: ", self.chemistry)
        print("physics: ", self.physics)
        print("maths: ", self.maths)
        print("avg: ", self.avg())
        print("grade: ", self.grade())
        print()


    def update(self):
        choice = input("what do you want to update in the in the student (name/father/mother/chemistry/physics/maths: )").lower()
        if choice == "name":
            new_name = input("Enter Name: ")
            self.name = new_name

        elif choice == "father":
            father_name = input("Enter Name: ")
            self.father = father_name

        elif choice == "mother": 
            mother_name = input("Enter Name: ")
            self.mother = mother_name

        elif choice == "chemistry":
            chemistry_marks = int(input("Enter Chemistry marks: "))
            self.chemistry = chemistry_marks

        elif choice == "physics":
            physics_marks = int(input("Enter Physics marks: "))
            self.physics = physics_marks

        elif choice == "maths":
            maths_marks = int(input("Enter maths marks: "))
            self.maths = maths_marks

        else:
            print("please enter wcorrect value")    

        self.display_info()
        


student1 = Student(101, "John", "Robert", "Mary", 85, 90, 90)
student2 = Student(102, "Alice", "David", "Sarah", 78, 82, 88)
student3 = Student(103, "Bob", "Michael", "Emma", 92, 88, 91)
student4 = Student(104, "Eve", "William", "Olivia", 80, 85, 87)
student5 = Student(105, "Charlie", "James", "Sophia", 75, 80, 82)
student6 = Student(106, "Grace", "Daniel", "Ava", 98, 92, 90)
student7 = Student(107, "Henry", "Matthew", "Isabella", 55, 35, 42)



students = [student1, student2, student3, student4, student5, student6, student7]


#.........................................Display student Code.......................................................

def display_student(students):
    for student in students:
        student.display_info()

# ........................................Rank Student (code).......................................................

def print_rank(students):
    ranked_student = sorted(students, key=lambda student: student.avg(), reverse=True)
    for rank, student in enumerate(ranked_student, start=1):
        print("rank: ", rank)
        print("name: ", student.name)
        print("roll: ", student.roll)
        print("father: ", student.father)
        print("mother: ", student.mother)
        print("avg: ", student.avg())    
        print("grade: ", student.grade())
        print()


#,................................................. add student..................................................

def add_student(students):
    while True:
        roll = int(input("Enter roll number to add :"))
        Found = False
        for student in students:
            if roll == student.roll:
                Found = True
                print("student already exist")
                break

        else:
            print("adding the student")

            name = input("Enter Student Name: " )
            father = input("Enter Father Name: " )
            mother = input("Enter Mother Name: " )
            chemistry = int(input("Enter chemistry marks: "))
            physics = int(input("Enter physics marks: "))
            maths = int(input("Enter maths marks: "))

            student = Student(roll, name, father, mother, chemistry, physics, maths)

            students.append(student)
            print("student added successful")

            choice = input("did you want to add more student(yes/no): ").lower()
            if choice == "no":
                break
            

# add_student(students)



#................................................ student search student (code).............................................

def search_student(students, roll_number):
    for student in students:
        if student.roll == roll_number:
            return student
    return None

def student_search_menu(students):

    while True:

        start = input("Do you want to search a student? (yes/no): ").lower()

        if start == "no":
            print("skied")
            break
        if start != "yes":
            print("please enter yes or no")
            continue

        roll_number = int(input("Enter Roll Number: "))

        student = search_student(students, roll_number)
        if student:
            student.display_info()

        else:
            print("student not found")

            while True:
                choice = input("do you want to search more student res or no: ").lower()

                if choice == "no":
                    return

                if choice == "yes":
                    break

                else:
                    print("enter yes or no: ")
                    
# student_search_menu(students)

# ..........................................update student (code)...................................................
def update_student(students):
    while True:
        roll = int(input("Enter roll number to update student: "))
        student = search_student(students, roll)
        if student:
            student.update()

        else:
            print("object not found")
            

        choice = input("did you want to edit more (yes or no): ").lower()

        if choice == "no":
            break    

        if choice == "yes":
            continue

# ...............................................delete student (code)...............................................
def delete_student(students):
    while True:
        delete = input("do you want to delete the student (yes or no): ").lower()
        if delete == "no":
            break

        if delete == "yes":
            roll = int(input("Enter roll number to delete student from the list: "))
            student = search_student(students, roll)
            if student:
                student.display_info()
                students.remove(student)
                print("student was deleted succesful")

            else:
                print("Roll not exist in the list")
                continue


            choice = input("did you want to print list (yes/no): ").lower()
            if choice == "yes":
                for student in students:
                    student.display_info()

            if choice == "no":
                print("skip")


# .............................................main menu (code).........................................................

def main_menu():

    while True:
        print(" Student Management system")
        print("1, Add student")
        print("2, search student")
        print("3, Update student")
        print("4, delete student")
        print("5, display all student")
        print("6, print the rank of the students")
        print("7, exit")

        choice = int(input("Enter the serial number to use the proces: "))

        if choice == 1:
            add_student(students)

        elif choice == 2:
            student_search_menu(students)

        elif choice == 3:
            update_student(students)

        elif choice == 4:
            delete_student(students)

        elif choice == 5:
            display_student(students)

        elif choice == 6:
            print_rank(students)

        elif choice == 7:
            print("exit")
            print("Thanks for using the Program")
            break

        else:
            print("Enter correst series number")

main_menu()
student = {
    ("101") : {
        "name" : "Rouank Choudhary",
        "physics" : 90,
        "chemistry" : 79,
        "maths" : 96,
         },

    ("102") : {
        "name" : "Nitin Choudhary",
        "physics" : 82,
        "chemistry" : 79,
        "maths" : 67,
         },

    ("103") : {
        "name" : "Anmol choudhary",
        "physics" : 99,
        "chemistry" : 98,
        "maths" : 97,
         },

    ("104") : {
        "name" : "Sujal choudhary",
        "physics" : 67,
        "chemistry" : 74,
        "maths" : 88,
         },

    ("105") : {
        "name" : "Savan choudhary",
        "physics" : 67,
        "chemistry" : 74,
        "maths" : 88,
         },   

}

roll = input("Enter roll number to find student  : ")
if roll in student:
    print(student[roll])
else:
    print("student not found")    



choice = input("add another student (yes/no) : ")

if choice.lower() == "yes":
    while True:
    
        roll = str(input("Enter roll number : "))
        name = str(input("Enter student name : "))
        physics = int(input("enter physics marks : "))
        chemistry  = int(input("enter chemistry marks : "))
        maths = int(input("enter maths marks : "))

        student.update({
            roll: {
                "name" : name,
                "physics" : physics,
                "chemistry" : chemistry,
                "maths" : maths,

            }
        })
        again = input("do you want to add more student (yes/no) : ")

        if again.lower() == "no":
            break


print(student)

choice = input("To view the student data (yes/no): ")
if choice.lower == "yes":
    for roll, data in student.items():
        print("student")
        print("Roll: ", roll)
        print("name: ", data["name"])
        print("physics :", data["physics"])
        print("chemistry: ", data["chemistry"])
        print("maths: ", data["maths"])

while True:
    
    roll = input("enter roll no to update student info : ")
    if roll in student:
        print("student found")    
        update = input("do you want to update student (yes/no) : ")
        if update == "yes":
                change = (input("choose what do you want to update name/physics/chemistry/maths : "))
        
                if change == "physics":
                    new_marks = int(input("write updated marks : "))
                    student[roll]["physics"] =  new_marks
                    print(student[roll])
        
                if change == "name":
                    new_name = str(input("write updated name : "))
                    student[roll]["name"] =  new_name
                    print(student[roll])

                if change == "chemistry":
                    new_marks2 = int(input("write updated marks : "))
                    student[roll]["chemistry"] =  new_marks2
                    print(student[roll])

                if change == "maths":
                    new_marks3 = int(input("write updated marks : "))
                    student[roll]["maths"] =  new_marks3
                    print(student[roll])
        if update == "no":
            print("nothing change")
            break

        more = input("do you want to update more student (yes/no) : ")
        if more.lower() == "no":
            break

    else:
        print("student not found")

print(student)

while True:
    delete = input("did you want to delete student (yes/no) : ")
    if delete == "yes":
        roll = input("Enter roll number to delete student : ")
        if roll in student:
            print("student found (roll number is deleted)")
            del student[roll]
            print(student)
        else:
            print("student not found")
        

                             
    if delete == "no":
        print("skipped")
        break

    more = input("delete more student (yes/no) : ")
    if more.lower() == "no":
        break

while True:

    calculate_average_marks = input("did you want to calculate average marks (yes/no) : ")
    if calculate_average_marks == "yes":
        roll = input("enter roll number to calculate average marks of the student : ")
        if roll in student:
            print("student found (calculating average marks)")
            
            physics = student[roll]["physics"]
            chemistry = student[roll]["chemistry"]
            maths = student[roll]["maths"]
            avg = (physics+chemistry+maths)/3
            print(avg)

            if avg >= 90:
                print("grade = A")
            elif avg >= 70:
                print("grade = B")
            elif avg >= 60:
                print("grade = C")
            else:
                print("no grade found (fail)")            
            
        else:
            print("student not found")

    more = input("calculate more (yes/no) : ")
    if more.lower() == "no":
        break
        

    if calculate_average_marks == "no":
        print("skipped.....")
        break



topper = input("find the topper in the student (yes/no) : ")
if topper == "yes":
    highest = 0
    topper = ""
    roll = ""
    for roll, data in student.items():
        physics = data["physics"]
        chemistry = data["chemistry"]
        maths = data["maths"]

        avg = (physics+chemistry+maths)/3
        if avg > highest:
            highest = avg
            topper = data["name"]
            topper_roll = roll
    print("Topper = ", topper, topper_roll)
    info = input("do you want to print topper info (yes/no) : ")
    info =  student[topper_roll]
    a = student[topper_roll]["physics"]
    b = student[topper_roll]["chemistry"]
    c = student[topper_roll]["maths"]

    percent = (a+b+c)/3

    if info == "yes":
        print(topper, info, "Average : ", percent)
if topper == "no":
    print("skiped...")



rank = input("press enter to print ranks ")
if rank == "":
    rank_list = []
    
    for roll, data in student.items():
        physics = data["physics"]
        chemistry = data["chemistry"]
        maths = data["maths"]
        name = data["name"]


        avg = (physics+chemistry+maths)/3
        rank_list.append([roll, name, avg])
        

    rank_list.sort(key = lambda x: x[2], reverse=True)
    
    for index, student in enumerate(rank_list, start = 1):
        print(index, student)
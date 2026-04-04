print("STUDENT RECORD SYSTEM")
student = {}
print("1. Add Student")
print("2. Show Student")
print("3. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    student["name"] = name
    student["age"] = age
    student["course"] = course
elif choice == 2:
    print(student)
elif choice == 3:
    print("Thank you")
else:
    print("invalid number !!!")

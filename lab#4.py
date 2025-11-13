newDict = {"brand": "Ford","model": "Mustang","year": 1964}
print(newDict)
print(len(newDict))
print("Printing values according to its keys")
print(newDict["brand"])
print(newDict["model"])
print(newDict["year"])
print("Lets see what dict does with duplicate keys")
newDict = {"brand": "Ford","model": "Mustang","year": 1964,"year": 2025}
print(newDict)
print("Storing tuples in dictionary")
tuple1 = (1,2,3,"HELLO")
tuple2 = (4,5,6,"WORLD")
tuple3 = (7,8,9,"AI")
newDict = {"tuple1": tuple1, "tuple2": tuple2, "tuple3": tuple3}


students = [
    {"name": "Ali", "age": 19, "grade": "A", "subject": "Math"},
    {"name": "Shoaib", "age": 20, "grade": "B+", "subject": "Physics"},
    {"name": "Hamza", "age": 18, "grade": "A-", "subject": "Computer"}
]

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    subject = input("Enter subject: ")
    students.append({"name": name, "age": age, "grade": grade, "subject": subject})
    print(" Student added successfully!")

def remove_student(name):
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            print(" Student removed successfully!")
            return
    print(" Student not found!")

def update_student(name, age, grade, subject):
    for s in students:
        if s["name"].lower() == name.lower():
            s["age"] = age
            s["grade"] = grade
            s["subject"] = subject
            print(" Student updated successfully!")
            return
    print(" Student not found!")

def display_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}, Subject: {s['subject']}")
    print("--------------------")

def search_student(name):
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Found: Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}, Subject: {s['subject']}")
            return
    print(" Student not found!")

while True:
    print("\nChoose an option:")
    print("1. Add new student")
    print("2. Remove student")
    print("3. Update student information")
    print("4. Display all students")
    print("5. Search student by name")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_student()
    elif choice == "2":
        name = input("Enter name to remove: ")
        remove_student(name)
    elif choice == "3":
        name = input("Enter name to update: ")
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")
        subject = input("Enter new subject: ")
        update_student(name, age, grade, subject)
    elif choice == "4":
        display_students()
    elif choice == "5":
        name = input("Enter name to search: ")
        search_student(name)

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("⚠ Invalid choice! Please try again.")
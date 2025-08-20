stu_grad = {}

def add_user(name, grade):
    stu_grad[name] = grade
    print(f"{name} added with grade {grade}")

def update_user(name, grade):
    if name in stu_grad:
        stu_grad[name] = grade
        print(f"{name}'s grade updated to {grade}")
    else:
        print(f"{name} not found! Adding as new entry.")
        stu_grad[name] = grade

def get_dict():
    if not stu_grad:
        print("No students available.")
    else:
        print("Student Grades:")
        for name, grade in stu_grad.items():
            print(f"- {name}: {grade}")

# Main loop
while True:
    inp = input("\nEnter operation (add/update/view/exit): ").lower()

    if inp == "add":
        name = input("Enter the name: ")
        grade = input("Enter the grade: ")
        add_user(name, grade)
    elif inp == "update":
        name = input("Enter the name: ")
        grade = input("Enter the grade: ")
        update_user(name, grade)
    elif inp == "view":
        get_dict()
    elif inp == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid operation. Try again.")

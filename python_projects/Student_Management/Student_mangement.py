class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def add_student(self):
        with open(self.filename, "a") as file:
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            file.write(f"{student_id},{name},{age},{grade}\n")
            print("Student added successfully.\n")

    def view_students(self):
        try:
            with open(self.filename, "r") as file:
                print("\n--- Student Records ---")
                for line in file:
                    student = line.strip().split(",")
                    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        except FileNotFoundError:
            print("No student records found.\n")

    def search_student(self):
        student_id = input("Enter Student ID to search: ")
        found = False

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    student = line.strip().split(",")
                    if student[0] == student_id:
                        print(f"\nStudent Found:")
                        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
                        found = True
                        break
            if not found:
                print("Student not found.")
        except FileNotFoundError:
            print("No student records found.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        updated = False

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            with open(self.filename, "w") as file:
                for line in lines:
                    student = line.strip().split(",")
                    if student[0] == student_id:
                        print(f"Current Info - ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
                        name = input("Enter new name: ")
                        age = input("Enter new age: ")
                        grade = input("Enter new grade: ")
                        file.write(f"{student_id},{name},{age},{grade}\n")
                        updated = True
                    else:
                        file.write(line)

            if updated:
                print("Student record updated successfully.")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No student records found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        deleted = False

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            with open(self.filename, "w") as file:
                for line in lines:
                    student = line.strip().split(",")
                    if student[0] != student_id:
                        file.write(line)
                    else:
                        deleted = True

            if deleted:
                print("Student record deleted successfully.")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No student records found.")

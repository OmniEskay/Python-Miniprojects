class Student:
    def __init__(self, name, adm_number, marks1, marks2):
        self.name = name
        self.adm_number = adm_number
        self.marks1 = marks1
        self.marks2 = marks2

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept(self):
        name = input("Enter student name: ")
        adm_number = input("Enter admission number: ")
        marks1 = float(input("Enter marks for subject 1: "))
        marks2 = float(input("Enter marks for subject 2: "))
        student = Student(name, adm_number, marks1, marks2)
        self.students.append(student)
        print("Student added successfully!")

    def display(self):
        if not self.students:
            print("No students in the system.")
            return
        for student in self.students:
            print(f"Name: {student.name}, Admission Number: {student.adm_number}, "
                  f"Marks1: {student.marks1}, Marks2: {student.marks2}")

    def search(self):
        adm_number = input("Enter admission number to search: ")
        for student in self.students:
            if student.adm_number == adm_number:
                print(f"Student found: Name: {student.name}, Admission Number: {student.adm_number}, "
                      f"Marks1: {student.marks1}, Marks2: {student.marks2}")
                return
        print("Student not found.")

    def delete(self):
        adm_number = input("Enter admission number to delete: ")
        for student in self.students:
            if student.adm_number == adm_number:
                self.students.remove(student)
                print("Student record deleted successfully!")
                return
        print("Student not found.")

    def update(self):
        old_adm = input("Enter the old admission number: ")
        new_adm = input("Enter the new admission number: ")
        for student in self.students:
            if student.adm_number == old_adm:
                student.adm_number = new_adm
                print("Admission number updated successfully!")
                return
        print("Student not found.")

def main():
    sms = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Accept Student details")
        print("2. Display all students")
        print("3. Search for a student")
        print("4. Delete a student record")
        print("5. Update a student's admission number")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            sms.accept()
        elif choice == '2':
            sms.display()
        elif choice == '3':
            sms.search()
        elif choice == '4':
            sms.delete()
        elif choice == '5':
            sms.update()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
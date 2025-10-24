# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 16:21:46 2025

@author: Admin
"""

from result_system import ResultSystem
from student import Student  # Make sure your Student class is imported

def main():
    result_system = ResultSystem()

    while True:
        print("\n--- Student Result Management ---")
        print("1. Add Student")
        print("2. Add Subject Marks")
        print("3. View Student Report")
        print("4. View All Students")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            # Add a new student
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            student = Student(student_id, name)
            result_system.add_student(student)
            print(f"Student {name} added successfully.")

        elif choice == "2":
            # Add subject marks
            student_id = int(input("Enter Student ID: "))
            subject_name = input("Enter Subject Name: ")
            marks = float(input("Enter Marks: "))
            result_system.add_subject_marks(student_id, subject_name, marks)

        elif choice == "3":
            # View individual student report
            student_id = int(input("Enter Student ID: "))
            result_system.generate_student_report(student_id)

        elif choice == "4":
            result_system.list_all_students()

        elif choice == "5":
            break
        else:
             print("Invalid choice.")
if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 16:19:42 2025

@author: Admin
"""

class ResultSystem:
    def __init__(self):
        self.students = {}
        
    def add_student(self, student):
        self.students[student.student_id] = student
        
    def add_subject_marks(self, student_id, subject_name, marks):
        # Find the student by ID
        student = self.students.get(student_id)
        if student:
            # Call the student's add_subject method
            student.add_subject(subject_name, marks)
        else:
            print(f"Student with ID {student_id} not found.")
    
    def generate_student_report(self, student_id):
        student = self.students.get(student_id)
        if student:
            student.generate_report()
        else:
            print(f"Student with ID {student_id} not found.")
    
    def list_all_students(self):
        print("All Students Summary:")
        print("-" * 40)
        for student_id, student in self.students.items():
            total_subjects = len(student.subjects)
            average = student.calculate_average() if total_subjects > 0 else 0
            print(f"ID: {student_id}, Name: {student.name}, Subjects: {total_subjects}, Average: {average:.2f}")

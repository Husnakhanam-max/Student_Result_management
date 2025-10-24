# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 15:35:32 2025

@author: Admin
"""

from subject import Subject
import utils

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = {}
        

    def add_subject(self, subject_name, marks):
        subject = Subject(subject_name, marks)
        self.subjects[subject_name] = subject

    def calculate_average(self):
        total = sum(subject.marks for subject in self.subjects.values())
        average = total / len(self.subjects)
        return average

    def generate_report(self):
        print(f"\nReport for {self.name} (ID: {self.student_id})")
        print("-" * 40)

        # Print all subjects and marks
        for subject_name, subject in self.subjects.items():
            print(f"{subject_name}: {subject.marks}")

        # Calculate total and average
        total = sum(subject.marks for subject in self.subjects.values())
        average = self.calculate_average()

        # Get grade from utils
        grade = utils.get_grade(average)

        print("-" * 40)
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print(f"Grade: {grade}")

    def __str__(self):
       total_subjects = len(self.subjects)
       return f"Student ID: {self.student_id}, Name: {self.name}, Total Subjects: {total_subjects}"

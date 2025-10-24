# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 15:31:48 2025

@author: Admin
"""

class Subject:
    def __init__(self, name, marks):
        self.name = name
        # Validate marks to be between 0 and 100
        if 0 <= marks <= 100:
            self.marks = marks
        else:
            raise ValueError("Marks should be between 0 and 100")
        self.marks = marks
        
        

    def __str__(self):
        return f"{self.name}: {self.marks}"
        

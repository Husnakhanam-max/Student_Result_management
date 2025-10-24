# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 16:00:08 2025

@author: Admin
"""

# utils.py

def get_grade(average):
    if 90 <= average <= 100:
        return "A"
    elif 75 <= average < 90:
        return "B"
    elif 50 <= average < 75:
        return "C"
    else:
        return "Fail"

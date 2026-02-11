# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:31:00 2026

@author: adith
"""

import pandas as pd
grades=pd.Series([85, None, 92, 45, None, 78, 55],index=['Student A','Student B','Student C','Student D','Student E','Student F','Student G'])
print(f"Original Series:\n{grades}")
print(f"\nMissing Grades :\n{grades.isnull()}")

print(f"\nFilled Series:\n{grades.fillna(0)}")

print("\nFiltered Series:\nStudents with scores greater than 60:\n",grades[grades>60])
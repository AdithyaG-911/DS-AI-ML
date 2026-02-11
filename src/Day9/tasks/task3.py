# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:40:32 2026

@author: adith
"""

import pandas as pd
usernames=pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print(usernames)

print(usernames.str.strip())
print(f"\nCleaned Series :\n{usernames.str.lower()}")

print(f"\nName with 'a' Found ?\n{usernames.str.contains('a')}")
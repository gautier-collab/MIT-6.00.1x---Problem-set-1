# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s = input('enter s: ')
counter = 0
iterate = 0
for i in s:
    if iterate <= len(s)-3:
        if (i == 'b' and s[iterate +1] == 'o' and s[iterate +2]=='b'):
            counter += 1
    iterate += 1
print(counter)
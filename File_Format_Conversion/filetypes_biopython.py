# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:28:16 2024

@author: kanmani
"""

var = 'BioPython'
with open ("filebiopy.txt", 'a+') as file: #w+ command rewrite the file everytime, a+, appends every input
    file.write("\n"+ var+"_Bioinfomage")
    
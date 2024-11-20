# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:23:35 2024

@author: kanmani
"""

from Bio import Entrez
Entrez.email = 'kanmanimr.biotech@gmail.com'
record = Entrez.read(Entrez.esearch(db = 'pmc', term ='biopython', retmax=2000)) #retmax comment is for setting retriving limit
print(type(record))                                                                                                                                                                 
print(record.keys())
for key in record.keys():
    print(key, ":", record [key])
biopythonID = record ["IdList"]
print(biopythonID)
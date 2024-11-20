# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:11:22 2024

@author: kanmani
"""

from Bio import Entrez
Entrez.email='kanmanimr.biotech@gmail.com'
record=Entrez.read(Entrez.espell(db='pmc', term='biobython'))
print(type(record))
print(record.keys())
for key in record.keys():
    print(key,':',record[key])
    
    
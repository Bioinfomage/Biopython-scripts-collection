# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:54:59 2024

@author: kanmani
"""

from Bio import Entrez
Entrez.email = "kanmanimr.biotech@gmail.com"
'''record = Entrez.read(Entrez.egquery(term = 'biopython'))
print(type(record))
print(record.keys())
print(type(record['eGQueryResult']))
for element in record['eGQueryResult']:
    print(element)
    for key in element.keys():
        print(key, ":", element[key])'''
        

#biopython quizHow many PubMed records?

""" term-Cancer
2- What is the number of MeSH records?

3- How many books?

4- How many nucleotide records?"""

record = Entrez.read(Entrez.egquery(term = 'Cancer'))
print(type(record))
print(record.keys())
print(type(record['eGQueryResult']))
for element in record['eGQueryResult']:
    print(element)
    for key in element.keys():
        print(key, ":", element[key])

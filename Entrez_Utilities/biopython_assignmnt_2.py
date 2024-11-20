# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 00:03:26 2024

@author: kanmani
"""

from Bio import Entrez
Entrez.email = "kanmanimr94@gmail.com"
terms = ['homo sapiens AND Lung Cancer AND Marker',

         'Human AND homo sapiens AND Lung Cancer AND Marker',

         '(Human[Title] OR homo sapiens[Title]) AND Lung Cancer AND Marker',

         '(Human[Title] OR homo sapiens[Title]) OR (Lung Cancer[Title] AND Marker[Title])',

         '(Human[Title] OR homo sapiens[Title] OR Lung Cancer[Title] OR Marker[Title]',

         '(Human[Title] OR homo sapiens[Title]) AND (Lung Cancer[Title] AND Marker[Title])']
for termIndex, term in enumerate(terms):
    record = Entrez.read(Entrez.esearch(db='pmc',
                                        term=term,
                                        retmax=5))
    print(termIndex+1, ":", term)
    #print(type(record))
    #print(record.keys())
    print('Count:', record['Count'])
    IdList = record['IdList']
    print(IdList)
    for ID in IdList:
        summary = Entrez.read(Entrez.esummary(db='pmc', id=ID))
        for doc in summary:
            print(doc['Title'])
    print('-------------------------')
    
  #option   (Human[Title] OR homo sapiens[Title]) AND (Lung Cancer[Title] AND Marker[Title])' is 
  #the most effective search method since it has ensured all the keywords in the title and filter only relevent titles.
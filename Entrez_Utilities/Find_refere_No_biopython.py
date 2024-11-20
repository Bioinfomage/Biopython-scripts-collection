# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 03:45:18 2024

@author: kanmani
"""

from Bio import Entrez
Entrez.email = 'kanmanimr.biotech@gmail.com'
terms = ['Rice[Organism] AND RefSeq[Keyword] AND Plastid[Title]']
for termIndex, term in enumerate(terms):
    record = Entrez.read(Entrez.esearch(db='nucleotide',
                                        term=term,
                                        retmax=2000,
                                        idtype='acc'))
    print(termIndex+1, ":", term)
    print('Count:', record['Count'])
    IdList = record['IdList']

for ID in IdList:
      if 'NC' in ID:
          summary = Entrez.read(Entrez.esummary(db = 'nucleotide', id = ID))
          print(type(summary))
          for doc in summary:
                print(doc.items())
                print('-------------------------')
    
  
  

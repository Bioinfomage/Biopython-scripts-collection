# ' -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:59:00 2024

@author: kanmani
"""

from Bio import Entrez
Entrez.email = "kanmanimr94@gmail.com"
record = Entrez.read(Entrez.esearch(db ='nucleotide', term = 'INS[gene] AND RefSeq[Keyword]', retmax=2000, idtype = 'acc'))
print(record)
fetchlist=[]
count=0
for ID in record['IdList']:
 
   fetchlist.append(ID[0:2])
   NoDubs = set(fetchlist)
#print(fetchlist)   
#print(NoDubs)     #to check
#to get the number of acc in each type, for loop and if condition
for i in NoDubs:
    for j in fetchlist:
        if i in j:
            count +=1
    print (i, count)
    count = 0  
     

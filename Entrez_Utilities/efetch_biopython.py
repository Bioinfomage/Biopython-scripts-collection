# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:44:12 2024

@author: kanmani
"""

from Bio import Entrez
Entrez.email = "kanmanimr94@gmail.com"
#Example of three Homo sapiens genes
#HBB:Hemoglobin subunit beta
#DNASE1L3:deoxyrebonuclease 1 like 3
#OCA2: OCA2 melanosomal transmembrane protein (eye color gene) #retmax for increase the result limit
#adding-->[genename] AND Refseq[Keyword] to filter the exact data
#if we want only human RefSeq, add Homo sapiens [Organism]
record = Entrez.read(Entrez.esearch(db ='nucleotide', term = 'HBB[gene] AND Rattus norvegicus [Organism] AND RefSeq[Keyword]', retmax=2000, idtype = 'acc'))


print(record)
count = 0 # to make a count of RefSeq
FetchList = []#to store fetched seq info into list
#filter the ref seq with 'NM' keyword with for loop and if condition
for ID in record["IdList"]:
    if 'NM' in ID:
        count += 1
        fetch = Entrez.efetch(db = 'nucleotide', id = ID, rettype= 'fasta', retmode = 'text')#rettype='gb', for genbank data
        #read() for whole seq. readline for a single line
        readFetch = fetch.read()# to show only first line, or no of line should be specified inside ().
        FetchList.append(readFetch)
        #print(readFetch)
#print(count)        
print(FetchList)
print(len(FetchList))#alternative for print count
#to look into each fetched RefSeq by sending them into forloop function
for files in FetchList:
    with open ("HBB_rat.fasta", 'a+') as savedFile: #a+ receving the data and saving file with given name(appending),
     savedFile.write(files)#write function for download files and store in the files variable and write it in the savedfile variable

#HBB.fasta
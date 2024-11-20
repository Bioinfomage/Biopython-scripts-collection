# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:00:27 2024

@author: kanmani
"""

'''
EcoRI = "gaattc"
The enzyme cuts the sequences as "g|aattc"

addCutter = "g|aattc"

You have to remember that python is case-sensitive.

Questions for this assignment
Can you cut the sequences in the HBB.fasta file and print the number of fragments for each sequence after the cut and the length of each fragment?

'''


from Bio import SeqIO
from Bio.SeqUtils import*
from Bio.Seq import*
record = SeqIO.parse(r'C:\Users\kanmani\Biopython\HBB.fasta', 'fasta')

EcoRI = "gaattc".upper()
addCutter = "g|aattc".upper()

for element in record:
    #converting lowercase
    print(element.name)
   
    Seq = str(element.seq)
    print('GC_content->', GC(Seq))
    print('EcoRI Location-->', nt_search(Seq, 'GAATTC'))
    #replacing
    Rep = Seq.replace(EcoRI, addCutter)
    #print(Rep)
    #splitting
    Split = Rep.split('|')
    #print(Split)
    #fragments count
    print('Fragment count-', len(Split))
    Count=1
    for fragment in Split:
        print('Length of fragment_No-', Count, len(fragment))
        Count += 1
    print("<=====================>", "\n")     
    
    
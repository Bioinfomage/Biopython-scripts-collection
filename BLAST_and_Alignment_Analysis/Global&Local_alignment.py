# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:46:26 2024

@author: kanmani
"""

from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import*

record_human = SeqIO.parse(r'C:\Users\kanmani\HBB_Human1.fasta', 'fasta')
record_rat = SeqIO.parse(r'C:\Users\kanmani\HBB_rat.fasta', 'fasta')


#Pairwaise alignment, to find extnded simlrty btwn sam typ of files
for element in record_human:
    #print(element.seq)
    Human_HBB = str(element.seq)
for element in record_rat:
   # print(element.seq)
   Rat_HBB = str(element.seq)
#Global alignment
#print(help(pairwise2))

# the xx-default parameters, match and gap parameter
#print(help(pairwise2.align.globalxx))

globalalignment = pairwise2.align.globalxx(Human_HBB, Rat_HBB)
#print(globalalignment)
#print(len(globalalignment))
#print(globalalignment[0])
#print(format_alignment(*globalalignment[0])) 
#or we can iterate through the globalalignment liat   
#for ind, pair in enumerate(globalalignment):
   # print(format_alignment(*globalalignment[ind]))
#Local alignment
localalignment = pairwise2.align.localxx(Human_HBB, Rat_HBB)
#print(help(pairwise2.align.localmx()))
#print(help(pairwise2.align.localxs()))
#print(localalignment) 
#print(len(localalignment)) 
localalignment1 = pairwise2.align.localmx(Human_HBB, Rat_HBB,2,0)#mx, match-2, mismatch-0 -to give match value
#print(len(localalignment1))
localalignment2 = pairwise2.align.localxs(Human_HBB, Rat_HBB, -10, -0.1)
print(len(localalignment2))

for ind, pair in enumerate (localalignment2):
    print(format_alignment(*localalignment2[ind]))
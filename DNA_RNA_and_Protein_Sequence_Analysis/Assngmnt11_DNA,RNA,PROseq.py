# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:42:31 2024

@author: kanmani
"""
'''
First, to determine the human HBB gene, you just have to check for a unique word in the fasta description line so you can choose its sequence.

You can then transcribe, reverse and reverse complement

Then you can keep the sequence as the forward and reverse complement as the reverse.

Then to extract the ORFs or the open reading frame

In order to translate the mRNA, the translation must start from the first nucleotide, then from the second, then from the third, and these are the first, second, and third frames. To get the other three frames, we use the reverse complement to translate the complement strand in the direction of 5 prime.

You can make a range of 0:3 to be 0, 1, and 2.

An empty list can be made to store the orfs

This range can be entered in a 'for loop' since the elements in the range will determine the beginning of the translation in the forward and reverse.

Then cut the translated sequence based on the asterisk.

Then put them all in the empty list and print them out at the end.

Questions for this assignment
Write the codes that do transcription, reverse and reverse complement and save each of them separately in a file.

Can you write the code that translates for 6 frames of the human HBB gene only?

Course content
Play
25. Working with DNA, RNA, and Protein Sequences
4min
Start
Assignment 11: Working with DNA, RNA, and Protein Sequences


'''

from Bio import SeqIO
from Bio.Seq import*

record = SeqIO.parse (r'C:\Users\kanmani\Biopython\HBB.fasta', 'fasta')

for element in record:
    if 'Homo sapiens' in element.description:
        print(element.seq)
        Forward = str(element.seq)
        rev= Forward [::-1]
        print(rev)
        Reverse = reverse_complement(Forward)
        print(Reverse)
        count = range(0,3)
        ORFs = []
        for i in count:
            F_ORFs = translate(Forward[i:], table=1, stop_symbol = '***')
            R_ORFs = translate(Reverse[i:], table=1, stop_symbol = '***')
            Split_F_ORFs = F_ORFs.split('***')
            Split_R_ORFs = R_ORFs.split('***')
            ORFs += Split_F_ORFs
            ORFs += Split_R_ORFs
            print(ORFs)
ReSpa = filter(None, ORFs)        
for ind, j in enumerate(ReSpa):
    print(ind+1, j, sep='\t')    
                
            
        
        
        
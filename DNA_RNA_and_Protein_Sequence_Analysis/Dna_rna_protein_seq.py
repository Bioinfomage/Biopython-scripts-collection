# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:15:16 2024

@author: kanmani
"""

from Bio import SeqIO
from Bio.Seq import*
record = SeqIO.parse(r'C:\Users\kanmani\HBB_Human1.fasta', 'fasta')
for element in record:
    print(str(element.seq))
    dnaSeq = str(element.seq)
    #transcribe function convert dna seq to rna seq
    #replaces 'T' with 'U' 
    rnaSeq = transcribe(dnaSeq)
    #print(rnaSeq)
    #back_transcribe for reverse transcribtion
    #print(back_transcribe(rnaSeq))
    #complement funtion is to get complementary starnd
    com_seq = complement(dnaSeq)
    #print(com_seq)
    #5" to 3' is a forward strand, any seq in the database is a forward starnd
    #to get a reverse strand (3" to 5")
    #'seq_name'[::-1] --> to get a reverse strand
    reverse_seq = dnaSeq [::-1]
    #print(reverse_seq)
    
    #to get reverse complement seq--> reverse_complement (compnt to reverse_seq)
    #print(reverse_complement(dnaSeq))
    
    #translate dna to protein
    #the seq should be a multiple of 3
    #genetic code table no 1 is normally used
    #if the seq is from mitochondrial or invertabrate ise no 2
    #there are some difference btwn 1 & 2 in protein and stop codon
    protein1 = translate(dnaSeq[10:100], stop_symbol='***', table=1) 
    protein2 = translate(dnaSeq[10:100], stop_symbol='***', table=2) 
    print(protein1)
    print(protein2)
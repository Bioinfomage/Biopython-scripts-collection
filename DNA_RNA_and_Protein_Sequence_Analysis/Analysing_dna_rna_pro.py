# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 13:55:26 2024

@author: kanmani
"""

from Bio import SeqIO
from Bio.SeqUtils import*
from Bio.Seq import*
record = SeqIO.parse (r'C:\Users\kanmani\HBB_Human1.fasta', 'fasta')
for element in record:
    print(str(element.seq))
    dnaSeq = str(element.seq)
    rnaSeq = transcribe(dnaSeq)
    protein_seq = translate(dnaSeq[10:100], stop_symbol="")
    #GC content
    print(GC(dnaSeq))
    #nt_search function returns all the locations of query query seq
    print(nt_search(dnaSeq, 'ATG'))
    #to calculate the mol_weig-->molecular_weight
    print(molecular_weight(dnaSeq, 'DNA'))
    print(molecular_weight(rnaSeq,'RNA'))
    print(molecular_weight(protein_seq,'protein')) # before this step make sure to remove "*" from the seq to avoid error
    # to get all the possible 6 frame ORFs
    print(six_frame_translations(dnaSeq))
    #to get 3 letter codes of protein seq
    print(seq3(protein_seq))
    #to get one letter code of protein seq
    print(seq1(seq3(protein_seq)))
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:01:48 2024

@author: kanmani
"""
from Bio import SeqIO
with open ('sample_abi.fasta', 'w+') as convertedfastafile:
    SeqIO.convert(r'C:\Users\kanmani\Biopython\sample.abi','abi', convertedfastafile, 'fasta')
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:45:48 2024

@author: kanmani
"""

from Bio import SeqIO
#coverting fasta to fasta2line
with open ('HBB_Human.fasta2line', 'w+') as convertedfile:
    SeqIO.convert(r'C:\Users\kanmani\HBB_Human1.fasta', 'fasta', convertedfile, 'fasta-2line')
#  the"r" before the path is to convert normal string to raw string
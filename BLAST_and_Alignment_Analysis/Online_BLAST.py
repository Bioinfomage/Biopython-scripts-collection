# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:04:10 2024

@author: kanmani
"""

from Bio import SeqIO
record = SeqIO.read(r'C:\Users\kanmani\HBB_Human1.fasta', 'fasta')
from Bio.Blast import NCBIWWW
#help(NCBIWWW)
blastcommand = NCBIWWW.qblast(program = 'blastn', database ='nt', sequence = record.seq)

with open('blastResults.xml', 'w+') as w:
    w.write(blastcommand.read())
    
   
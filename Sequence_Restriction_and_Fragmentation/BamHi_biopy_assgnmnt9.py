# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:56:17 2024

@author: kanmani
"""

'''HBB.fasta file (you will find it in udemybiopython.zip)

BamHI = "GGATCC"

Produce the result in the following format

"sequenceName\tcount"

Like this:

NM_001168847.1 1'''

from Bio import SeqIO
record = SeqIO.parse(r'C:\Users\kanmani\Biopython\HBB.fasta', 'fasta')
BamHI = "GGATCC"
for element in record:
    print(element.id,"\t", str(element.seq).count(BamHI))
    
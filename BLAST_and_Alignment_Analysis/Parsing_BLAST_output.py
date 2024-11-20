# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:30:19 2024

@author: kanmani
"""

from Bio.Blast import NCBIXML

record = NCBIXML.read(open(r'C:\Users\kanmani\Biopython\blastResults.xml'))

for ind, align in enumerate (record.descriptions):
    
    print('Alignment_Index',ind)
    print('Title',align.title)
    print('Score',align.score)
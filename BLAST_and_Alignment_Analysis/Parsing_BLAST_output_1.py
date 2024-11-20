# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:09:11 2024

@author: kanmani
"""

from Bio.Blast import NCBIXML

record = NCBIXML.read(open(r'C:\Users\kanmani\Biopython\blastResults.xml'))

for ind, align in enumerate (record.alignments):
    
    print("....")
    print('Alignment_Index',ind)
    print('1.Title',align.title)
    print('2.length',align.length)
    print('3.HSP', align.hsps)
    for hsp in align.hsps:
        print('3.1Score', hsp.score)
        print('3.2bits', hsp.bits)
        print('3.3E_value', hsp.expect)
        print('3.4identities', hsp.identities)
        print('3.5Gaps', hsp.gaps)
        print('3.6Strand', hsp.strand)
        print('3.7Frame', hsp.frame)
        print('3.8Query Start', hsp.query_start)
        print('3.9Subject Start', hsp.sbjct_start)
        print('3.10 Alignment Length', hsp.align_length)
        print(hsp.query[50:100])
        print(hsp.match[50:100])
        print(hsp.sbjct[50:100])
        
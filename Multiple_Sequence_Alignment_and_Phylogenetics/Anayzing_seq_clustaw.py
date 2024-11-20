# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:47:32 2024

@author: kanmani
"""
#import os
from Bio.Align.Applications import ClustalwCommandline
print(help(ClustalwCommandline))
clustalw2 = r'C:\Program Files (x86)\ClustalW2\clustalw2'
#cmd = ClustalwCommandline(clustalw2, infile = r'C:\Users\kanmani\Biopython\HBB.fasta', type = 'DNA', clustering = 'NJ', tree = True, outputtree = 'phylip', output = 'FASTA')
cmd = ClustalwCommandline(clustalw2, infile = r'C:\Users\kanmani\Biopython\HBB.fasta', type = 'DNA',output = 'FASTA', outfile = 'HBB.fa')
#assert os.path.isfile(clustalw2), "Clustal W executable missing"
std_out, std_err = cmd()

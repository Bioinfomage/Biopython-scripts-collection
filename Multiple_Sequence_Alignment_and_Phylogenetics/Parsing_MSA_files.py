# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:21:33 2024

@author: kanmani
"""

#from Bio.Align.Applications import ClustalwCommandline
#print(help(ClustalwCommandline))
#clustalw2 = r'C:\Program Files (x86)\ClustalW2\clustalw2'
#cmd = ClustalwCommandline(clustalw2, infile = r'C:\Users\kanmani\Biopython\HBB.fasta', type = 'DNA',output = 'phylip', outfile = 'HBB.phy')
#std_out, std_err = cmd()"""

from Bio import AlignIO
filename = r'C:\Users\kanmani\Biopython\HBB.phy'
formatFIle = 'phylip'
readFile = AlignIO.read(open(filename), formatFIle)
print(readFile)
for seq in readFile:
    print(seq)
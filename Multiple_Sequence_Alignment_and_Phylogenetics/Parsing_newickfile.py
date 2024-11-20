# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:36:39 2024

@author: kanmani
"""

#phylo module is responsible for reading dendrogram files
#most famous method is newick method
from Bio import Phylo
readTree = Phylo.read (r'C:\Users\kanmani\Biopython\HBB.ph', 'newick')
print (readTree)
Phylo.draw_ascii(readTree)

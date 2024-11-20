# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:03:20 2024

@author: kanmani
"""
#to get all the reference database
from Bio.Blast.Applications import*
#help(NcbimakeblastdbCommandline())
#MakeDB = NcbimakeblastdbCommandline(cmd =r'C:\Program Files\NCBI\blast-2.15.0+\bin\makeblastdb.exe',
                                    #input_file = r'C:\Users\kanmani\Biopython\HBB.fasta',
                                   # dbtype = 'nucl',
                                   # out = 'HBBdb')
#std_out, std_err =MakeDB()'''

#to align DNA against the data base, use blastn program

#help(NcbiblastnCommandline())

#Makeblastn = NcbiblastnCommandline(cmd = r'C:\Program Files\NCBI\blast-2.15.0+\bin\blastn.exe',
 #                                  out = 'unknownHBB.xml', 
#                                   outfmt =5, 
#                                   query = r'C:\Users\kanmani\Downloads\UdemyBiopython\unknownHBB.fasta', 
 #                                  db ='HBBdb', evalue = 0.001, strand = 'plus')
#std_out, std_err =Makeblastn()

# reading unknownHBB.xml file to confirm the gene
from Bio.Blast import NCBIXML

record = NCBIXML.read(open(r'C:\Users\kanmani\Biopython\unknownHBB.xml'))

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
        
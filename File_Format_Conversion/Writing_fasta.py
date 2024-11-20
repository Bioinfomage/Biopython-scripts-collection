# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:24:49 2024

@author: kanmani
"""
#writing fasta file from gb file
from Bio import SeqIO
from Bio.Seq import* # call all that is in the module
#from Bio.Alphabet import DNAAlphabet #defining nucleotide bases as DNA but this module has been rmvd from biopy
from Bio.SeqRecord import* # Creating FASTA file
record = SeqIO.parse(r'C:\Users\kanmani\HBB_human.gb', 'gb')
for element in record:
    #print(element)
   # new_record = SeqRecord(Seq(str(element.seq)), id= 'NM_000518.5', name='HBB', description='Homo sapiens hemoglobin subunit beta (HBB), mRNA.') # alphabet = DNAAlphabet()
   #alternative method
   new_record = SeqRecord(Seq(str(element.seq)), id= element.id, name=element.name, description= element.description)
   print(new_record.format("fasta"))
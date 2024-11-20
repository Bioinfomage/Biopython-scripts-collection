# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:41:04 2024

@author: kanmani
"""

#writing gb file from fasta file
from Bio import SeqIO
from Bio.Seq import* # call all that is in the module
#from Bio.Alphabet import DNAAlphabet #defining nucleotide bases as DNA but this module has been rmvd from biopy
from Bio.SeqRecord import* # Creating FASTA/gb file
from Bio.SeqFeature import*
record = SeqIO.parse(r'C:\Users\kanmani\HBB_Human1.fasta', 'fasta')
for element in record:
    #print(element)
    f1= SeqFeature(FeatureLocation(0, 628, strand =1), type = 'gene')
    f2= SeqFeature(FeatureLocation(50, 494, strand =1), type = 'CDS', qualifiers={'product':'hemoglobin subunit beta','protein_id':'NP_000509.1', 'translation':translate(element.seq[50:494])})
    r1= Reference()
    r1.authors='KANMANI'
    r1.journal='Nature'
        
   # new_record = SeqRecord(Seq(str(element.seq)), id= 'NM_000518.5', name='HBB', description='Homo sapiens hemoglobin subunit beta (HBB), mRNA.') # alphabet = DNAAlphabet()
   #alternative method
    new_record = SeqRecord(Seq(str(element.seq)),id= element.id, name=element.name, description= element.description, features=[f1,f2],
                          annotations={'molecule_type':'DNA','organism':'Homo sapiens', 'source':'Homo sapiens (human)', 'references':[r1]})
   
    print(new_record.format("genbank"))
    

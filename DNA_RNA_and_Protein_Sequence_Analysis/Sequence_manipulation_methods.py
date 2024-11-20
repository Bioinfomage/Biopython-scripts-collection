# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:15:07 2024

@author: kanmani
"""

from Bio import SeqIO
record = SeqIO.parse(r'C:\Users\kanmani\HBB_Human1.fasta', 'fasta')
for element in record:
   # print(element.seq)
    print(str(element.seq))
    #Slicing
    ##print(str(element.seq)[:10])
    #print(str(element.seq)[10:110])
    print(str(element.seq)[:-2])
    #Counting amino acids / bases /group of strings
    print(str(element.seq).count('ATG'))
    #find function takes 'letter' or seq of letters and returns its location.
    #find function returns the results only once so we have to set the for loop to find all the locations of particular seq in the sequence
    print(str(element.seq).find('ATG'))
    #to find no of letters in the seq
    print(len(str(element.seq)))
    #to convert the seq in lower case letters
    Lower =str(element.seq).lower()
    print(Lower)
    #to convert the seq into upper case
    Upper =str(element.seq).upper()
    print(Upper)
    #to replace a letter or seq by another letter or sequence
    print(str(element.seq).replace('T', 'U'))
    #split function cuts or deletes charecter or seq of chrctr and convrt strng into list
    split = str(element.seq).split('ATG')
    print(split)
    print(len(split))
    #join
    Join = '\n'.join(split)   #or ''.join(split) or  #or '*'.join(split)
    print(Join)
    #stip() function removes character or seq from both end of the string.
    AddTab = '   ' + str(element.seq) +'****'
    print(AddTab)
    str1= AddTab.strip()#removibg tab
    str2 = str1.strip('*')#removing '*'
    print(str2)
  
    
    
   
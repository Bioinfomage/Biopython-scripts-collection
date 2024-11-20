# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:16:12 2024

@author: kanmani
"""

from Bio import Entrez
Entrez.email='kanmanimr.biotech@gmail.com'
sciNames=['Bos gaurus', 'Antelope cervicapra', 'Gazella bennettii', 'Boselaphus tragocamelus', 'Canis lupus', 'Panthera leo', 'Elephas maximus', 'Equus africanus', 'Panthera pardus', 'Cervus canadensis', 'Pavo cristatus', 'Grus leucogeranus', 'Vulpes vulpes', 'Rhinoceros unicornis', 'Panthera Tigris', 'Crocodylus palustris', 'Gavialis gangeticus', 'Equus caballus', 'Equus quagga', 'Babalus bubalis', 'Sus scrofa', 'Camelus dromedaries', 'Giraffa camelopardalis ', 'Hemidactylus flaviviridis', 'Hippopotamus amphibius', 'Macaca mulatta', 'Canis lupus', 'Felis domesticus', 'Acinonyx jubatus', 'Rattus rattus', 'Mus musculus', 'Oryctolagus cuniculus', 'Bubo virginianus', 'Passer domesticus', 'Corvus splendens', 'Acridotheres tristis', 'Psittacula eupatria', 'Molpastes cafer', 'Eudynamis scolopaccus', 'Columba livia', 'Naja naja', 'Ophiophagus hannah', 'Hydrophiinae ', 'Python molurus', 'Ptyas mucosa'] 
for SNIND, SN in enumerate(sciNames):
 record = Entrez.read(Entrez.espell(db='taxonomy', term=SN))
 print('Index:',SNIND)
 print("Original Sci name:", record['Query'])
 print("Corrected Sci name:", record['CorrectedQuery'].capitalize())
 print("--------------------")
 #if you want only the corrected terms add the below code
if record['Query'] != record['CorrectedQuery'].capitalize():
     print("Original Sci name:", record['Query'])
     print("Corrected Sci name:", record['CorrectedQuery'].capitalize())
     
    

from Bio import Entrez
Entrez.email = 'kanmanimr.biotech@gmail.com'
'''record = Entrez.read(Entrez.einfo())
print(type(record))
print(record.keys())
print(record['DbList'])
print("\n".join(sorted(record['DbList'])))'''

record_1 = Entrez.read(Entrez.einfo(db='genome'))#parameter(db=)
print(type(record_1))
print(record_1.keys())
print(record_1['DbInfo'])
for key in record_1['DbInfo'].keys():
    print(key, ":", record_1['DbInfo'][key])
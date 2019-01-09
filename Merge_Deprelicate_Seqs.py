# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:01:45 2019

@author: jufeng
"""

file_name1 = 'all_complete_Genome_Arc_cds.ABMM.default.ublast_ID80.0_FR0.7_EV1e-10.fna'
file_name2 = 'all_complete_Genome_Arc_protein.domain.tlout.ABMM.fna'


fileoutput = open('all_complete_Genome_Arc_protein.ABMM.merged.fna','w')


a = {}
Num = 0
for line in open(file_name1,'r'):

    if line.startswith('>'):
        Num+=1
        n = 0
        ID = str(line.rstrip().split(' ')[0].replace('>',''))
        a[ID] = line
        n += 1
    else:
        if n == 1:
            a[ID] = a[ID] + line
        else:
            continue

    if Num%1000000==0:
        print(Num, 'seqs searched!')
        

        
L1 = len(a)
print(str(L1) + ' seqs in the '+file_name1)

m = 0
for line in open(file_name2,'r'):
        
    if line.startswith('>'):
        m += 1
        ID = str(line.rstrip().split(' ')[0][1:])
        try:
            SEQ = a[ID]
            del a[ID]
        except KeyError:
            continue
    else:
      continue
        
    fileoutput.write(line)
    if m%1000000==0:
        print(m, 'seqs searched!')


L2 = len(a)
print(str(L2) + ' seqs are unique in the '+file_name1)

print(str(m)+' seqs in the '+file_name2)
L3 = L1-L2
print(str(m-L3)+' seqs are unique in the '+file_name2)

for key in a.keys():
    fileoutput.write(a[key])
    
fileoutput.close()
print('Done!')
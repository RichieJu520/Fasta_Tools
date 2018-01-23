#N50 Program By Feng Ju
import sys
from Bio import SeqIO
import os

print 'Python and Biopython needed for running this script!'
print "Script for calculating N50 of assembly"
#fasta = raw_input('Enter the foldername containing fastas: ')

### N50 calculation
f=open(sys.argv[1]+'.statistics.csv','w')
f.write(','.join(["","no.of.seq","N50","Max.len","Avg.len","Min.len","no.of.bases","A%","T%","C%","G%","N%"]) + '\n')

#for root,dirs,files in os.walk(fasta):
for root,dirs,files in os.walk(sys.argv[1]):
    for file in files:
        #print '------','Processing',file,'in prograss','------'
        BaseSum,Length= 0,[]
        ValueSum,N50 = 0,0
        no_c,no_g,no_a,no_t,no_n = 0,0,0,0,0
        
        for record in SeqIO.parse(os.path.join(root, file), 'fasta'):    
            BaseSum += len(record.seq)
            Length.append(len(record.seq))
            seq =record.seq.lower()
            no_c+=seq.count('c')
            no_g+=seq.count('g')
            no_a+=seq.count('a')
            no_t+=seq.count('t')
            no_n+=seq.count('n')

        #N50 calcuation
        N50_pos = float(BaseSum / 2.0)
        Length.sort()   
        Length.reverse()
        average=sum(Length)/len(Length)

        for value in Length:
            ValueSum += value
            if N50_pos <= float(ValueSum):
                N50 = value
                break

        per_A = float(no_a*100)/BaseSum
        per_T = float(no_t*100)/BaseSum
        per_C = float(no_c*100)/BaseSum
        per_G = float(no_g*100)/BaseSum
        per_N = float(no_n*100)/BaseSum

        f.write(','.join([file, str(len(Length)),str(N50),str(max(Length)),str(average),str(min(Length)),str(BaseSum),str(per_A),str(per_T),str(per_C),str(per_G),str(per_N)]) + '\n')
        print '------','Processing',file,'finished!','------'

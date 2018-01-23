#N50 Program By Feng Ju
print 'Python and Biopython needed for running this script!'
print "Script for calculating N50 of assembly"
fasta = raw_input('Enter your fasta/fa name: ')

# N50 calculation
BaseSum,Length= 0,[]
ValueSum,N50 = 0,0
no_c,no_g,no_a,no_t,no_n = 0,0,0,0,0

from Bio import SeqIO
for record in SeqIO.parse(open(fasta), "fasta"):
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
N80_pos = float(BaseSum / 1.25)
Length.sort()   
Length.reverse()
average=sum(Length)/len(Length)

for value in Length:
    ValueSum += value
    if N50_pos <= float(ValueSum):
        N50 = value
        break

print 'Sequences-NO.:',str(len(Length))
print 'N50:', str(N50)
print 'Sequences-Max.:',str(max(Length))
print 'Sequences-Mean:',str(average)
print 'Sequences-Min.:',str(min(Length))


#GC calcuation	
print "Total-bases:", BaseSum
print "percentage of A in given sequences","%.1f"%((float(no_a*100))/BaseSum),'%'
print "percentage of T in given sequences","%.1f"%((float(no_t*100))/BaseSum),'%'
print "percentage of C in given sequences","%.1f"%((float(no_c*100))/BaseSum),'%'
print "percentage of G in given sequences","%.1f"%((float(no_g*100))/BaseSum),'%'
print "percentage of N in given sequences","%.1f"%((float(no_n*100))/BaseSum),'%'



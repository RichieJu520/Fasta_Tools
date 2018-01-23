#GC calucation by Feng Ju
print 'Python and Biopython needed for running this script!'
print "Script for calculating N50 of assembly"
from Bio import SeqIO
fasta = raw_input('Enter the filename of the fasta/fa: ')

BaseSum = 0
no_c = 0
no_g = 0
no_a = 0
no_t = 0
no_n = 0

for record in SeqIO.parse(open(fasta), "fasta"):
    BaseSum += len(record.seq)
    seq =record.seq.lower()
    no_c+=seq.count('c')
    no_g+=seq.count('g')
    no_a+=seq.count('a')
    no_t+=seq.count('t')
    no_n+=seq.count('n')
	
print "Total number of bases:", BaseSum
print "percentage of A in given sequences","%.1f"%((float(no_a*100))/BaseSum),'%'
print "percentage of T in given sequences","%.1f"%((float(no_t*100))/BaseSum),'%'
print "percentage of C in given sequences","%.1f"%((float(no_c*100))/BaseSum),'%'
print "percentage of G in given sequences","%.1f"%((float(no_g*100))/BaseSum),'%'
print "percentage of N in given sequences","%.1f"%((float(no_n*100))/BaseSum),'%'

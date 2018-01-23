import os
import time, sys
from Bio import SeqIO

print 'Functions: This script is used to convert FQ file into FA file!'
while True:
    try:
        filename=raw_input("Enter the full name of the FQ file: ")
        start=time.time()
        wrerr = sys.stderr.write

        filename1=filename.replace('.fq','.fasta')
        filename2=filename1.replace('.fastq','.fasta')

        print "Coverting FQ files to FA files...pls wait!"

        count = SeqIO.convert(filename, "fastq", filename2, "fasta")
        print "Converted %i records" % count

        end=time.time()
        wrerr("OK, Converting Finished in %3.2f secs\n" % (end-start))
        break
    except:
        print 'File not found in working directory!'
        filename=raw_input("Enter the full name of the FQ file: ")

print "OK, Work finished!"+'\n'
raw_input('Press <Enter> to close this window!')

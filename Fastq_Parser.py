print 'This script is written for parsing Large Fasta file into small sub-fastas!'
import os
import time, sys
Parameters=raw_input("Enter two parameters: [Fastaname],[NUM](*10000)(number of sequences in each sub-fasta), sepeated by Space: ")

while True:
    try:
        filename=Parameters.split(' ')[0]
        Num=Parameters.split(' ')[1]
        num=int(float(Num)*10000)
        break
    except:
        Parameters=raw_input("Enter two parameters: [Fastaname],[NUM](*10000)(number of sequences in each sub-fasta), sepeated by Space: ")

start=time.time() # Timing begins
wrerr = sys.stderr.write

if os.path.exists(filename+'_divided'):
    for root, dirs, files in os.walk(filename+'_divided'):
        for name in files:
            os.remove(os.path.join(root,name))
else:
    os.mkdir(filename+'_divided')

j=-1

f=open(filename+'_divided\\'+filename.replace('.fasta','')+'-1.fasta','w')

for line in open(filename,'r'):
    if '@' in line:
        j+=1
        if j%int(num)==0 and j!=0:
            f=open(filename+'_divided\\'+filename.replace('.fasta','')+'-'+str(1+j/int(num))+'.fasta','a')
        f.write(line)
    else:
        f.write(line)


f.close()
          
end=time.time()   # Timing ends
wrerr("OK, work finished in %3.2f secs\n" % (end-start))
f.close()
raw_input('Press <Enter> to close this window!')





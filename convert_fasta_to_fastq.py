import random
import string

fasta = open('SRR10003462_1.fasta', 'r')
fastq = open('SRR10003462_1_new.fastq', 'a')

for index, line in enumerate(fasta):
    if (index + 1) % 2 == 0:
        fastq.write(line)
        fastq.write('+')
        fastq.write('\n')
        fastq.write(''.join(random.choice(string.ascii_letters)
                    for _ in range(len(line) - 1)))
        fastq.write('\n')
    else:
        fastq.write(line.replace('>', '@'))

fasta.close()
fastq.close()

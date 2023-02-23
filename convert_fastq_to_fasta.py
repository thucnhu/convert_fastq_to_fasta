fastq = open('SRR10003462_1.fastq', 'r')
fasta = open('SRR10003462_1.fasta', 'a')

for index, line in enumerate(fastq):
    if (index + 1) % 4 == 3 or (index + 1) % 4 == 0:
        continue

    fasta.write(line.replace('@', '>') if (index + 1) % 4 == 1 else line)

fastq.close()
fasta.close()

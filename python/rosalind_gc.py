from Bio import SeqIO

sequences = SeqIO.parse(open(r'../data/rosalind_gc.txt'), 'fasta')

'''
    get ID and percent of highest GC content sequence
'''

max_gc = 0
max_id = ''
for seq in sequences:
  current_gc = (seq.seq.count('G') + seq.seq.count('C')) / float(len(seq.seq))
  if current_gc > max_gc:
    max_gc = current_gc
    max_id = seq.id

print max_id, '\n', max_gc * 100



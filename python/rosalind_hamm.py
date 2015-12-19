# with open(r'../data/rosalind_hamm.txt','r') as my_file:
#     hamm_distance = 0
#     s = my_file.readline()
#     t = my_file.readline()
#     for base1, base2 in zip(s,t):
#         if base1 != base2:
#             hamm_distance += 1
#     print hamm_distance

with open(r'../data/rosalind_hamm.txt', 'r') as my_file:
  hamm_distance = 0
  seqs = my_file.read().split()
  seq1 = seqs[0]
  seq2 = seqs[1]

  for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
      hamm_distance += 1

  print hamm_distance

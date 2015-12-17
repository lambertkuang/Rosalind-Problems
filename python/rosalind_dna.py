'''
  open takes a file to open and mode (r for read, w for write, a for append, add + for reading and writing)
'''

with open(r'/Users/lambertkuang/Rosalind/data/rosalind_dna.txt', 'r') as file:
  dna_dict = {
  'a': 0,
  'c': 0,
  'g': 0,
  't': 0
  }
  '''
    file is a file object
    .read() makes it a string
    .strip() takes out whitespaces from beginning and end of string
    .lower() makes it lowercase
  '''
  nucleotides = file.read().strip().lower()
  for nt in nucleotides:
    dna_dict[nt] = dna_dict[nt] + 1

  print dna_dict['a'], dna_dict['c'], dna_dict['g'], dna_dict['t']
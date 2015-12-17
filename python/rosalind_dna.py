with open(r'/Users/lambertkuang/Rosalind/data/rosalind_dna.txt', 'r') as file:
  dna_dict = {
  'a': 0,
  'c': 0,
  'g': 0,
  't': 0
  }
  nucleotides = file.read().strip().lower()
  for nt in nucleotides:
    dna_dict[nt] = dna_dict[nt] + 1

  print dna_dict['a'], dna_dict['c'], dna_dict['g'], dna_dict['t']
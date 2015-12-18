with open(r'../data/rosalind_revc.txt', 'r') as file:
	reverse = file.read().strip().lower()[::-1]
	reverse_complement = ''
	complement = {
		'a': 't',
		'c': 'g',
		'g': 'c',
		't': 'a'
	}

	for nt in reverse:
		reverse_complement += complement[nt]

	print reverse_complement.upper()

with open(r'../data/rosalind_fib.txt', 'r') as file:
  params = file.read().split()
  def pair_count(n, k):
    if n == 1 or n == 2:
      return 1
    return pair_count(n - 1, k) + k * pair_count(n - 2, k)

  print pair_count(int(params[0]), int(params[1]))

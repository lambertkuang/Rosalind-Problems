import math

def binomial_fxn(n, k):
    numerator = math.factorial(n)
    denominator = math.factorial(k) * math.factorial(n-k)
    return numerator / denominator

with open(r'../data/rosalind_iprb.txt','r') as my_file:
    store = my_file.readline().split()
    k = int(store[0])
    m = int(store[1])
    n = int(store[2])

    total_p = k + m + n
    pk = k * m + k * n + binomial_fxn(k, 2)
    pm = 0.75 * binomial_fxn(m, 2) + 0.5 * m * n
    num = pk + pm
    denom = binomial_fxn(total_p, 2)
    print num / denom

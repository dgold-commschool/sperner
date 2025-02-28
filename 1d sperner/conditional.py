from one_d import *

n = 20
one_counts = {i : 0 for i in range(1, n + 2)}
sums = {i : 0 for i in range(1, n + 2)}
sq_sums = {i : 0 for i in range(1, n + 2)}

niters = 1000000

for iter_no in range(niters):
    t = generate_line(n)
    count = count_flips(t)
    ones = sum(t)
    one_counts[ones] += 1
    sums[ones] += count
    sq_sums[ones] += count * count

means = {i : sums[i] / one_counts[i] if one_counts[i] > 0 else "NA" for i in range(3, n)}
variances = {i : sq_sums[i] / one_counts[i] - means[i] * means[i] if one_counts[i] > 0 else "NA" for i in range(3, n)}
print(list(range(3, n)))
print(list(means.values()))
print(list(variances.values()))
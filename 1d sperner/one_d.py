import random
import plotly.express as px

def count_flips(s):
    c = 0
    for index in range(len(s) - 1):
        if s[index] != s[index + 1]: c += 1
    return(c)

def generate_line(n):
    return([0] + [random.choice([0, 1]) for i in range(n)] + [1])

niters = 10000
max_n = 15
means = [0 for i in range(2, max_n)]
variances = [0 for i in range(2, max_n)]

for n in range(2, max_n):
    s = 0
    sq = 0
    for iter_no in range(niters):
        t = generate_line(n)
        count = count_flips(t)
        s += count
        sq += count * count

    means[n - 2] = s / niters
    variances[n - 2] = sq / niters - (means[n - 2]) * (means[n - 2])

print(means)
print(variances)
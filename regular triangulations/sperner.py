from util import *
import plotly.express as px

niters = 10000

max_n = 15
means = [0 for i in range(2, max_n)]
variances = [0 for i in range(2, max_n)]

for n in range(2, max_n):
    s = 0
    sq = 0
    for iter_no in range(niters):
        t = random_triangle(n)
        count = count_polychrome(t)
        s += count
        sq += count * count

    means[n - 2] = s / niters
    variances[n - 2] = sq / niters - (means[n - 2]) * (means[n - 2])

print(means)
print(variances)

fig = px.scatter(x=list(range(2, max_n)), y=means)
fig.show()
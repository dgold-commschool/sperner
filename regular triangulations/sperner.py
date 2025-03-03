from util import *
import plotly.express as px
import math

niters = 10000
min_n = 2
max_n = 25
means = [0 for i in range(min_n, max_n)]
variances = [0 for i in range(min_n, max_n)]
values = [[0 for i in range(niters)] for n in range(min_n, max_n)]

for n in range(min_n, max_n):
    s = 0
    sq = 0
    for iter_no in range(niters):
        t = random_triangle(n)
        count = count_polychrome(t)
        s += count
        sq += count * count
        values[n - min_n][iter_no] = count

    means[n - min_n] = s / niters

    variances[n - min_n] = sq / niters - (means[n - min_n]) * (means[n - min_n])
    m = means[n - min_n]
    s = math.sqrt(variances[n - min_n])
    # if s != 0:
    #     shift_scale = [(v - m) / s for v in values[n - min_n]]
    #     px.histogram(x=shift_scale).show()

print(means)
print(variances)

fig = px.scatter(x=list(range(min_n, max_n)), y=means)
fig.show()
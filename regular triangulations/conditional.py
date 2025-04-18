from util import *
import plotly.express as px
import pandas as pd

niters = 500000

n = 10

reds = [0 for i in range(niters)]
greens = [0 for i in range(niters)]
blues = [0 for i in range(niters)]
polychromes = [0 for i in range(niters)]

for iter_no in range(niters):
    t = random_triangle(n)
    reds[iter_no] = count_color(t, "R")
    greens[iter_no] = count_color(t, "G")
    blues[iter_no] = count_color(t, "B")
    polychromes[iter_no] = count_polychrome(t)

d = {"n": list(range(niters)), "reds": reds, "blues": blues, "greens": greens, "poly": polychromes}
df = pd.DataFrame(data=d)

print(pd.DataFrame.head(df))
new_df = df.groupby(["reds", "greens"])["poly"].mean(numeric_only=True).reset_index()
new_df = new_df.pivot(index='reds', columns='greens')['poly'].fillna(0)
fig = px.imshow(new_df, x=new_df.columns, y=new_df.index)
fig.show()
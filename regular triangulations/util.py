import random

def random_triangle(n):
    l = []
    for row_no in range(n):
        row_len = row_no + 1
        if row_no == 0:
            row = ["R"]
        elif row_no == n - 1:
            row = ["B"] + [random.choice(["B", "G"]) for k in range(row_len-2)] + ["G"]
        else: 
            row = [random.choice(["R", "B"])] + [random.choice(["R", "G", "B"]) for k in range(row_len-2)] + [random.choice(["R", "G"])]
        l.append(row)
    return(l)

def print_triangle(triangle):
    for row in triangle:
        print(row)
    return()

def count_polychrome(triangle):
    count = 0

    # Count bottom-left-cornered triangles.
    y = 1
    x = 0
    while y < len(triangle):
        while x < y:
            c1 = triangle[y-1][x]           # Top Left
            c2 = triangle[y][x]             # Bottom Left
            c3 = triangle[y][x+1]           # Bottom Right
            if c1 != c2 and c2 != c3 and c1 != c3:
                count += 1
            x += 1
        x = 0
        y += 1

    # Count top-right-cornered triangles
        
    y = 1
    x = 1

    count2 = 0

    while y < len(triangle) - 1:
        while x <= y:
            c1 = triangle[y][x]                 # Top Right
            c2 = triangle[y][x-1]               # Top Left
            c3 = triangle[y+1][x]               # Bottom Right
            if c1 != c2 and c2 != c3 and c1 != c3: 
                count2 += 1

            x += 1
        x = 1

        y += 1
    return(count + count2)

def count_color(triangle, color):
    count = 0
    for row in triangle:
        count += sum([1 if c == color else 0 for c in row])
    return(count)

t = random_triangle(4)
print_triangle(t)
for color in "RGB":
    print(color, count_color(t, color))
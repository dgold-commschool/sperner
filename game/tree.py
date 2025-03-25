def replace(s, index, new):
    return(s[:index] + new + s[index + 1:])

def get_moves(position):
    l = []
    for index in range(len(position)):
        if position[index] == ".":
            l += [replace(position, index, "1")]
            l += [replace(position, index, "0")]

    return(l) 

print(get_moves("11...0"))

def count_flips(s):
    c = 0
    for index in range(len(s) - 1):
        if s[index] != s[index + 1]: c += 1
    return(c)

class Node:
    def __init__(self, board, children, value):
        self.board = board
        self.children = children
        self.value = value

    def pretty_print(self, depth, max_depth):
        print("\t" * depth + self.board + " " + str(self.value))
        if depth < max_depth:
            for child in self.children:
                child.pretty_print(depth + 1, max_depth)
    
    def populate(self):
        all_moves = get_moves(self.board)
        l = []
        if len(all_moves) == 0:
            self.value = count_flips(self.board)
        else:
            for move in all_moves:
                child = Node(move, [], 0)
                child.populate()
                l += [child]
            self.children = l

    def maximin(self, mode):
        if len(self.children) == 0:
            return(self.value)
        if mode == "max":
            l = []
            for child in self.children:
                child.value = child.maximin("min")
                l.append(child.value)
            self.value = max(l)
        if mode == "min":
            l = []
            for child in self.children:
                child.value = child.maximin("max")
                l.append(child.value)
            self.value = min(l)
        return(self.value)
                
    def best_move(self, mode):
        if len(self.children) == 0: return(None)
        l = []
        for child in self.children:
            l.append(child.value)
        if mode == "max":
            m = max(l)
        else: m = min(l)
        for child in self.children:
            if child.value == m:
                return(child.board)





start = Node("1...0", [], -1)
start.populate()
start.maximin("min")
start.pretty_print(0, 2)
print(start.best_move("min"))
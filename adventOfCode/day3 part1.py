import math as m
import re

board = list(open('dataday3 1-2'))
chars = {(r, c): [] for r in range(140) for c in range(140)
         if r < len(board) and c < len(board[r]) and board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p) for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p) > 1))

n, m = map(int, input().split())
puzzle_pieces = list(map(int, input().split()))

puzzle_pieces.sort()

min_difference = float('inf')
for i in range(n - 1, m):
    difference = puzzle_pieces[i] - puzzle_pieces[i - n + 1]
    min_difference = min(min_difference, difference)

print(min_difference)

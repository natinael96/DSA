n = int(input())
bar_lengths = list(map(int, input().split()))
bar_count = {}

for length in bar_lengths:
    if length in bar_count:
        bar_count[length] += 1
    else:
        bar_count[length] = 1

max_height = max(bar_count.values())
total_towers = len(bar_count)

print(max_height, total_towers)

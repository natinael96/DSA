people = int(input())
claw_length = list(map(int, input().split()))

survivors = 0
furthest_claw = 0

for i in range(people - 1, -1, -1):  # start from the last person
    if furthest_claw <= 0:
        survivors += 1
    furthest_claw = max(furthest_claw - 1, claw_length[i])

print(survivors)
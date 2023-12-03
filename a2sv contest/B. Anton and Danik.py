n = int(input())
results = input()

anton_wins = results.count('A')
danik_wins = results.count('D')

if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")

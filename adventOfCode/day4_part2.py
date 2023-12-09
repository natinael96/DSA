import sys

m = {}

for i, x in enumerate(sys.stdin):
    if i not in m:
        m[i] = 1

    # Add a check for the colon in the line
    if ":" in x:
        x = x.split(":")[1].strip()
        a, b = [list(map(int, k.split())) for k in x.split(" | ")]
        j = sum(q in a for q in b)

        for n in range(i + 1, i + j + 1):
            m[n] = m.get(n, 1) + m[i]

print(sum(m.values()))

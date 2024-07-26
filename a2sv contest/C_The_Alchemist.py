from collections import deque, defaultdict

for _ in range(int(input())):
    n, k = map(int, input().strip().split())
    costs = list(map(int, input().strip().split()))
    potion = list(map(int, input().strip().split()))
    mix = []

    for _ in range(n):
        mi, *rules = map(int, input().strip().split())
        mix.append([mi] + rules)

    mncost = costs[:]
    for p in potion:
        mncost[p - 1] = 0

    graph = defaultdict(list)
    deg = [0] * n

    for i in range(n):
        if mix[i][0] > 0:
            for j in mix[i][1:]:
                graph[j - 1].append(i)
                deg[i] += 1

    order = []
    q = deque()

    for i in range(n):
        if deg[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph[node]:
            deg[nei] -= 1
            if deg[nei] == 0:
                q.append(nei)

    for node in order:
        if mix[node][0] > 0:
            mix_cost = sum(mncost[dep - 1] for dep in mix[node][1:])
            mncost[node] = min(mncost[node], mix_cost)

    print(' '.join(map(str, mncost)))
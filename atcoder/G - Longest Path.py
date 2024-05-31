from collections import defaultdict, deque

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    
deg = [0] * (n + 1)
for node in graph:
    for nei in graph[node]:
        deg[nei] += 1

q = deque([node for node in range(1, n + 1) if deg[node] == 0])
ordr = []

while q:
    node = q.popleft()
    ordr.append(node)
    for nei in graph[node]:
        deg[nei] -= 1
        if deg[nei] == 0:
            q.append(nei)

dist = [0] * (n + 1)
print(ordr)
for node in reversed(ordr):
    # print(node)
    for nei in graph[node]:
        print(node, dist, nei)
        dist[node] = max(dist[node], 1 + dist[nei])

print(max(dist))



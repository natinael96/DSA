n, m = map(int, input().split())

answer_counts = [{answer: 0 for answer in "ABCDE"} for _ in range(m)]


for _ in range(n):
    student_answer = input().strip()
    for j in range(m):
        answer_counts[j][student_answer[j]] += 1


points = list(map(int, input().split()))


max_total_score = 0
for j in range(m):
    max_answer_count = max(answer_counts[j].values())
    max_total_score += max_answer_count * points[j]

print(max_total_score)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
courses = list(map(int, input().split()))

start = max(courses)
end = sum(courses)

result = 0

while start <= end:
    mid = (start + end) // 2

    sum = 0
    cnt = 1
    for course in reversed(courses):
        sum += course
        if sum > mid:
            cnt += 1
            sum = course

    if cnt <= M:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
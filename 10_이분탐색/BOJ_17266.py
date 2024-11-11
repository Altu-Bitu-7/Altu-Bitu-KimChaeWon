import sys
input = sys.stdin.readline

N = int(input()) 
M = int(input())  
location = list(map(int, input().split())) 

start = 1  
end = N  

while start <= end:
    mid = (start + end) // 2  
    
    can_illuminate = True
    previous_end = 0  
    
    for pos in location:
        # 현재 가로등이 비출 수 있는 범위가 이전 구간 끝을 덮지 못하면 실패
        if pos - mid > previous_end:
            can_illuminate = False
            break
        # 현재 가로등이 비출 수 있는 범위 끝 갱신
        previous_end = pos + mid
    
    # 마지막 구간까지 비출 수 있는지 확인
    if previous_end < N:
        can_illuminate = False
    
    if can_illuminate:
        end = mid - 1
    else:
        start = mid + 1

print(start)
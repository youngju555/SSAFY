# 그냥 완전탐색해서 최솟값을 찾자. 그냥 dfs 쓰면 될거같은데 굳이 재귀 안쓰고. 지금까지의 경로의 합이 최소합을 넘었다면 그만두기.
# 아근데 재귀 안쓰면 방문표시를 리셋못하니까 재귀써야될듯. 기존의 stack 방식을 써도 될거같은데.(방문표시땜에 안되나)
def move_sum(num,total,sti,stj):
    global min_total
    if num ==move:
        if sti == n-1 and stj == n-1:
            min_total = min(min_total,total)
            return
        else:
            return
    if total > min_total:
        return
    for di,dj in [(1,0),(0,1)]:
        ni = di + sti
        nj = dj + stj
        if 0<=ni<n and 0<=nj<n:
            move_sum(num+1,total+aj[ni][nj],ni,nj)

T = int(input())
for t in range(1,T+1):
    n = int(input())
    aj = [list(map(int,input().split())) for _ in range(n)]
    move = n*2 -1 # 이동 횟수
    m = aj[0][0]
    min_total = 270
    move_sum(1,m,0,0)
    print(f'#{t} {min_total}')
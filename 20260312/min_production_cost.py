T = int(input())
for t in range(1,T+1):
    n = int(input()) # 제품 수
    vj = [list(map(int,input().split())) for _ in range(n)]
    min_cost = 1500
    visited = [-1] * n

    def cost(depth,sum_cost):
        global min_cost
        if sum_cost > min_cost:
            return
        if depth == n:
            min_cost = min(min_cost,sum_cost)
            return
        for j in range(n):
            if visited[j] == -1:
                visited[j] = 0
                cost(depth + 1, sum_cost + vj[depth][j])
                visited[j] = -1
    cost(0,0)
    print(f'#{t} {min_cost}')
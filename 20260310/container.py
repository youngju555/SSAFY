#트럭의 적재용량을 초과하지 않는 선에 최대한 무거운 컨테이너를 운반.
T = int(input())
for t in range(1,T+1):
    n,m = map(int,input().split())
    wj = list(map(int,input().split()))
    mj = list(map(int,input().split()))
    wj.sort(reverse=True)
    mj.sort(reverse=True)
    sum_w = 0
    for w in range(len(wj)):
        for tr in range(len(mj)):
            if mj[tr] >= wj[w]:
                sum_w += wj[w]
                wj[w] = 0
                mj[tr] = 0
                break
    print(f'#{t} {sum_w}')
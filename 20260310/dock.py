#가자 도크. 24시간 False리스트 만들고 종료시간/시작시간부터 진행하면서 종료시간을 포함해 화물된 시간이 젤 작은 시간을
# 24시간 리스트를 True로 바꾸면서 이미 채워진 애들은 패스하고 없는 부분만 채우기
T = int(input())
for t in range(1,T+1):
    n = int(input())
    aj = [list(map(int,input().split())) for _ in range(n)]
    aj.sort(reverse=True)
    time = 24
    cnt = 0
    for a in aj:
        if a[1] <= time:
            cnt +=1
            time = a[0]
    print(f'#{t} {cnt}')
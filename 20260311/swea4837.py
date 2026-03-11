def subset(depth, sub_l, n, k):
    last = []
    if depth == 12:
        for j in range(12):
            if sub_l[j] == 1:
                last.append(j + 1)
        find(last, n, k)
        return
    subset(depth + 1, sub_l + [0], n, k)
    subset(depth + 1, sub_l + [1], n, k)


def find(list, n, k):
    sum_l = 0
    global cnt
    for l in list:
        sum_l += l
    if sum_l == k and len(list) == n:
        cnt += 1
        return


T = int(input())
for t in range(1,T+1):
    n, k = map(int,input().split())
    cnt = 0

    subset(0,[],n,k)
    print(f'#{t} {cnt}')

    ##ai가 써준 비트마스킹 방법
    # T = int(input())
    # for t in range(1, T + 1):
    #     n, k = map(int, input().split())
    #     cnt = 0
    #
    #     # 1 << 12는 4096. 즉, 0부터 4095까지 모든 부분집합 확인
    #     for i in range(1 << 12):
    #         sum_val = 0
    #         len_val = 0
    #
    #         # 12개의 비트(원소) 자리 확인
    #         for j in range(12):
    #             if i & (1 << j):
    #                 sum_val += (j + 1)
    #                 len_val += 1
    #
    #         # 조건 일치 시 카운트 증가
    #         if len_val == n and sum_val == k:
    #             cnt += 1
    #
    #     print(f'#{t} {cnt}')
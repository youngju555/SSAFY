# def bus(depth, check, num):
#     charge = mj[1]
#     global min_num
#     if depth == mj[0]:
#         for i in range(1,len(check)):
#             if check[i] != 0 and check[i] >= check[i-1]:
#                 charge = check[i]
#             if charge <= 0:
#                 return
#             charge -= 1
#         min_num = min(min_num, num)
#         return
#     if num > min_num:
#         return
#     bus(depth+1, check + [mj[depth]], num + 1)
#     bus(depth+1, check + [0], num)
#     depth += 1
#
#
# T = int(input())
# for t in range(1,T+1):
#     mj = list(map(int,input().split()))
#     check = []
#     min_num = 100
#     bus(0,[],0)
#     print(f'#{t} {min_num}')

# 문제점 > depth 에 1 안더하는 실수, 배터리 교체 로직 오류(charge += check[i]),
## 이렇게 for문 돌리지말고 인자로 들고다니게 하기.
# 인자로 보내줄 것 : 충전 횟수, 현재 배터리 상태,
def bus(depth, charge, num):

    global min_num
    if num >= min_num:
        return
    if depth ==mj[0]:
        min_num = num
        return

    bus(depth+1, mj[depth]-1, num + 1)
    if charge > 0:
        bus(depth+1, charge -1, num)


T = int(input())
for t in range(1,T+1):
    mj = list(map(int,input().split()))
    min_num = 100
    bus(2,mj[1]-1,0)
    print(f'#{t} {min_num}')
## 다시 풀어봐야 될듯. 이렇게는.
def permutation(depth):
    if depth == len(c):
        baby_gin(p)
        return
    for s in range(len(c)):
        if not used[s]:
            used[s] = True
            p[depth] = c[s]
            permutation(depth + 1)
            used[s] = False
            if is_baby_gin: return


def baby_gin(card):
    global is_baby_gin
    if card[0] == card[1] == card[2]:
        is_baby_gin = True
    elif card[0] + 2 == card[1] + 1 == card[2] + 0:
        is_baby_gin = True
    return is_baby_gin

T = int(input())
for t in range(1,T+1):
    # 순열써서 3장부터 추가될때마다 새로 순열조합 짜서 검사.
    cards = list(map(int,input().split()))
    card1 = []
    card2 = []
    for ca in range(len(cards)):
        if ca % 2 ==0:
            card1.append(cards[ca])
        elif ca % 2 ==1:
            card2.append(cards[ca])

    is_baby_gin =False
    for i in range(4):
        is_baby_gin = False
        c = card1[:3+i]
        used = [False]*len(c)
        p = [0]*len(c)
        permutation(0)
        if is_baby_gin:
            print(f'#{t} 1')
            break
        c = card2[:3+i]
        used = [0]*len(c)
        p = [0]*len(c)
        permutation(0)
        if is_baby_gin:
            print(f'#{t} 2')
            break
    else:
        print(f'#{t} 0')


## 주사위 눈의 합. 중복 순열에 대해 합이 10이하가 나오는 경우의 수.

def dice(num,total):
    global cnt
    if total > 10:
        return
    if num == 4:
        print(result)
        print(total)
        cnt += 1
        return

    for i in range(1,7):
        result.append(i)
        dice(num +1,total+i)
        result.pop()
result = []
cnt = 0

dice(1,0)
print(cnt)
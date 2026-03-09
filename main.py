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
def quick(list, left, right):
    pivot = list[left]
    i = left
    j = right
    while i <= j:
        while i <= j and list[i] <= pivot:
            i += 1
        while i <= j and list[j] >= pivot:
            j -= 1
        if i < j:
            list[i], list[j] = list[j], list[i]
    list[left], list[j] = list[j], list[left]
    return j


def swab(list, left, right):
    if left < right:
        s = quick(list, left, right)
        swab(list, left, s - 1)
        swab(list, s + 1, right)

T = int(input())
for t in range(1,T+1):
    n = int(input())
    aj = list(map(int,input().split()))
    swab(aj,0,len(aj)-1)
    print(f'#{t} {aj[n//2]}')



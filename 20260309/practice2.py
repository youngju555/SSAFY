def baby_gin(result):
    cards1 = list(result[:3])
    cards2 = list(result[3:])
    check1 = False
    check2 = False
    if cards1[0]+2 == cards1[1]+1 == cards1[2]:
        check1 = True
    elif cards1[0] == cards1[1] == cards1[2]:
        check1 = True

    if cards2[0]+2 == cards2[1]+1 == cards2[2]:
        check2 = True
    elif cards2[0] == cards2[1] == cards2[2]:
        check2 = True

    return check1 and check2


def get_p(depth):
    global found
    if found:
        return
    if depth ==6:
        if baby_gin(result):
            found = True
            print(result)
        return

    for i in range(6):
        if not used[i]:
            used[i] = True
            result.append(data[i])
            get_p(depth+1)
            result.pop()
            used[i] = False

result = []
data = [1,3,2,6,6,6]
used = [False]*6
found = False
get_p(0)

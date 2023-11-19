def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        a = i
        pre = ''
        idx = 0
        while(idx < len(baby)):
            b = baby[idx]
            if b == a[:len(b)] and b is not pre:
                pre = b
                a = a.replace(b, "", 1)
                idx = 0
                if len(a) == 0:
                    answer += 1
                    break
            else:
                idx += 1
    return answer

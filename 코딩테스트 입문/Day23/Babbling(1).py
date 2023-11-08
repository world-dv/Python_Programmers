def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in baby:
            if j in i:
                i = i.replace(j, "!")
        i = i.replace("!", "")
        answer += 1 if len(i) == 0 else 0
    
    return answer

def solution(priorities, location):
    answer = 1
    while True:
        a = priorities.pop(0)
        if not priorities:
            break
        if a < max(priorities):
            priorities.append(a)
            location -= 1
            if location == -1:
                location = len(priorities) - 1
        else:
            if location == 0:
                break
            else:
                answer += 1
                location -= 1
    return answer

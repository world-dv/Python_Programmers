def solution(lottos, win_nums):
    answer = []
    count = 1
    for i in lottos:
        if i not in win_nums and i != 0:
            count += 1
    answer.append(6 if count >= 6 else count)
    answer.append(6 if count + lottos.count(0) >= 6 else count + lottos.count(0))
    return answer

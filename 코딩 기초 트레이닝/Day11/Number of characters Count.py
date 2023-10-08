def solution(my_string):
    answer = [0] * 52
    for i in my_string :
        if i.islower() :
            index = ord(i) - ord('a') + 26   
        else :
            index = ord(i) - ord('A')
        answer[index] += 1
    return answer

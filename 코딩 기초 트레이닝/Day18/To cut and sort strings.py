def solution(myString):
    answer = [i for i in myString.split('x') if i != '']
    return sorted(answer)

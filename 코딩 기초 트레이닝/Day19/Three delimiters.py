def solution(myStr):
    answer = []
    answer = myStr.replace('a', '!').replace('b', '!').replace('c', '!')
    answer = [i for i in answer.split('!') if i != '']
    return answer if len(answer) != 0 else ['EMPTY']

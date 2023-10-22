def solution(quiz):
    answer = []
    for i in quiz :
        i = i.split(" ")
        if i[1] == "+" :
            answer.append("O" if int(i[4]) == int(i[0]) + int(i[2]) else "X")
        else :
            answer.append("O" if int(i[4]) == int(i[0]) - int(i[2]) else "X")
    return answer

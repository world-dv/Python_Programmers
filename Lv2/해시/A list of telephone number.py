def solution(phone_book):
    answer = True
    dic = dict()
    
    for i in phone_book:
        dic[i] = 1
    for i in phone_book:
        for j in range(len(i)):
            if i[:j] in dic.keys():
                answer = False
                break
    
    return answer

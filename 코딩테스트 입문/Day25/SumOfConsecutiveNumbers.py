def solution(num, total):
    a = (total - sum([i for i in range(1,num+1)])) // num
    answer = [i for i in range(a+1,a+num+1)]
    return answer

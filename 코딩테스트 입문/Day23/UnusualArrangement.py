def solution(numlist, n):
    answer = sorted(numlist, key = lambda a : (abs(n-a),n-a))
    #첫 번째 인자 기준 오름차순 먼저 정렬, 그 안에서 두 번째 인자를 기준으로 오름차순 정렬
    return answer

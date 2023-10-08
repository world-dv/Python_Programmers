def solution(s):
    answer = [0, 0]
    while(s != "1") : 
        l = len(s) #문자열 길이
        s = s.replace("0", "") #0제거한 문자열
        r = len(s) #0제거 문자열 길이 
        l -= r #문자열 길이 - 0제거 문자열 길이 = 제거한 0의 갯수
        answer[0] += 1
        answer[1] += l #제거한 0의 갯수 저장
        s = format(r, 'b') #0제거한 문자열 길이를 바이너리로 변환
    
    return answer

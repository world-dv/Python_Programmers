def solution(sticker):
    answer = 0
    if len(sticker) == 1: #처리 안할 경우 런타임 에러
        return sticker[0]
    dp = [0 for _ in range(len(sticker))]
    dp2 = [0 for _ in range(len(sticker))]
    
    #ex) 1, 2, 3, 4, 5, 6 -> 1부터 5까지 탐색
    dp[0], dp[1] = sticker[0], max(sticker[0], sticker[1]) #1번째 선택할 경우
    for i in range(2, len(sticker)-1): 
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    
    #ex) 1, 2, 3, 4, 5, 6 -> 2부터 6까지 탐색
    dp2[0], dp2[1] = 0, sticker[1] #2번째 선택할 경우
    for i in range(2, len(sticker)): 
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
        
    answer = max(max(dp), max(dp2)) #가장 큰 값 찾음
    return answer

def solution(money):
    answer = 0
    n = len(money)
    if n == 1:
        return money[0]
    dp = [0 for i in range(n)]
    dp[0], dp[1] = money[0], max(money[0], money[1])
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    answer = max(dp)
    
    dp = [0 for i in range(n)]
    dp[0], dp[1] = 0, money[1]
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    answer = max(answer, max(dp))
    
    return answer

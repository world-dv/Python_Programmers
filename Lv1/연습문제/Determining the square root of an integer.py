def solution(n):
    answer = -1
    for i in range(1, n+1):
        if i ** 2 == n:
            answer = i
            break
    return (answer+1)**2 if answer != -1 else answer

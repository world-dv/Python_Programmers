def solution(people, limit):
    answer = 0
    n = len(people) - 1
    people.sort()
    
    start = 0
    end = n
    while True:
        if start >= end:
            break
        if people[start] + people[end] <= limit:
            answer += 1
            start += 1
        end -= 1
    return len(people) - answer

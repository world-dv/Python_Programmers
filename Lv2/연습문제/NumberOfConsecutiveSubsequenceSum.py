def solution(elements):
    answer = set()
    n = 1
    while(n <= len(elements)):
        for i in range(len(elements)):
            a = sum(elements[i:i+n])
            if i+n > len(elements):
                a += sum(elements[:(i+n) % len(elements)])
            answer.add(a)
        n += 1
        
    return len(answer)

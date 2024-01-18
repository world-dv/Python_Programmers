def solution(cacheSize, cities):
    answer = 0
    arr = []
    if cacheSize == 0:
        return 5 * len(cities)
    
    for i in cities:
        a = i.lower()
        if not arr:
            arr.append(a)
            answer += 5
            continue
        if a in arr:
            answer += 1
            arr.remove(a)
            arr.append(a)
            continue
        else:
            arr.append(a)
            answer += 5
            if len(arr) > cacheSize:
                arr.pop(0)
    return answer

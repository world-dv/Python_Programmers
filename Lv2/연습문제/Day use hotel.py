def solution(book_time):
    answer = 0
    room = []
    visited = [0] * len(book_time)
    book_time = sorted(book_time, key = lambda x : x[0])
    
    room.append(book_time[0][1])
    visited[0] = 1
    for i, j in enumerate(book_time):
        start, end = j[0], j[1]
        for ridx, r in enumerate(room):
            if calculate(start) < calculate(r) + 10 and not visited[i]:
                room.append(end)
                visited[i] = 1
                break
            if calculate(start) >= calculate(r) + 10 and not visited[i]:
                room[ridx] = end
                visited[i] = 1
                break
        room = sorted(room)
    answer = len(room)
    return answer

def calculate(x):
    x = x.split(':')
    return int(x[0]) * 60 + int(x[1])

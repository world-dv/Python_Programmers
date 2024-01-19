def solution(dirs):
    step_x = { 'U' : 0, 'D' : 0, 'R' : 1, 'L' : -1}
    step_y = { 'U' : 1, 'D' : -1, 'R' : 0, 'L' : 0 }
    x, y = 0, 0
    arr = []
    for i in dirs:
        dx = x + step_x[i]
        dy = y + step_y[i]
        if abs(dx) < 6 and abs(dy) < 6:
            if [dx, dy, x, y] not in arr and [x, y, dx, dy] not in arr:
                arr.append([dx, dy, x, y])
            x, y = dx, dy
    return len(arr)

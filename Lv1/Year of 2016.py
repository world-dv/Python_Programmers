def solution(a, b):
    answer = b
    d_name = ["FRI", "SAT","SUN","MON","TUE","WED","THU"]
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer += sum(day[:a-1])
    return d_name[answer % 7 - 1]

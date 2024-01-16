def solution(s):
    answer = 0
    idx = 0
    while idx < len(s):
        arr = []
        check = 0
        for i in s:
            if i in '({[':
                arr.append(i)
                check = 1
            if i == ')':
                if '(' in arr and arr[-1] == '(':
                    arr.pop(-1)
            if i == ']':
                if '[' in arr and arr[-1] == '[':
                    arr.pop(-1)
            if i == '}':
                if '{' in arr and arr[-1] == '{':
                    arr.pop(-1)
        answer += 1 if len(arr) == 0 and check else 0
        idx += 1
        s = s[1:] + s[0]
    return answer

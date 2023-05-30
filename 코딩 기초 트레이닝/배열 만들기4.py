def solution(arr):
    stk = []
    i = 0
    while True :
        if i == len(arr) :
            break
        if not stk :
            stk.append(arr[i])
            i += 1
        else :
            if stk[-1] < arr[i] :
                stk.append(arr[i])
                i += 1
            else :
                stk.remove(stk[-1])
        
    return stk

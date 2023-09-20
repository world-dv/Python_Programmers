def solution(nums):
    answer = 0
    arr = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for z in range(j+1, len(nums)):
                if countNumber(nums[i] + nums[j] + nums[z]):
                    answer += 1
    return answer

def countNumber(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

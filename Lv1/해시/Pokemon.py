def solution(nums):
    hash_arr = {}
    for i in nums:
        hash_arr[i] = nums.count(i)
    answer = min(len(hash_arr), len(nums) // 2) 
    return answer

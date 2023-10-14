def solution(numbers):
    arr = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    for i, j in enumerate(arr) :
        numbers = numbers.replace(j, str(i))
    answer = int(numbers)
    return answer

def solution(begin, target, words):
    answer = []
    visited = [False] * len(words)
    if target not in words:
        return 0
    stack = [begin]
    
    def dsp(words, target, begin, stack):
        count = sum([1 for x, y, in zip(begin, target) if x!=y])
        if count == 1:
            return stack
        elif count == 0:
            stack.append(begin)
            return stack
        
        for j, i in enumerate(words):
            count = sum([1 for x, y in zip(i, begin) if x != y])        
            if count <= 1 and not visited[j]:
                stack.append(i)
                visited[j] = True
                result = dsp(words, target, i, stack)
                if result is not None:
                    return result
                
    answer = dsp(words, target, begin, stack)
    return len(answer)

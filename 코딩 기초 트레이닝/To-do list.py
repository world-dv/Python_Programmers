def solution(todo_list, finished):
    answer = [i for j,i in enumerate(todo_list) if not finished[j]]
    return answer

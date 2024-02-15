def solution(plans):
    answer = []
    plans = sorted(plans, key = lambda x : x[1]) #과제 시작 순서대로 정렬
    study = [] #stack
    
    for name, start, time in plans:
        if study:
            last = study.pop() 
            time_diff = calculate(start) - last[1] #과제 시작 시간 차
            
            if time_diff < last[2]: #이전 과제를 덜 했을 경우
                study.append([last[0], last[1], last[2] - time_diff]) #stack에 추가 -> stop
            else: #과제를 다 했을 경우
                answer.append(last[0]) #과제 이름 추가 -> 과제 진행 완료
                time_diff -= last[2] #이전 과제 진행 후 남은 시간
                
                while study and time_diff: #stack이 비지 않았고 시간이 남았을 때 -> stop한 과제 이어서 진행해야함
                    last = study.pop()
                    if time_diff < last[2]: #남은 시간보다 경과되는 시간이 많다면
                        study.append([last[0], last[1], last[2] - time_diff]) #과제 stop
                        break
                    else: #남은 시간보다 경과되는 시간이 적다면
                        answer.append(last[0])
                        time_diff -= last[2]
        study.append([name, calculate(start), int(time)])
    for i in range(len(study)-1, -1, -1):
        answer.append(study[i][0])
    
    return answer

def calculate(x):
    hour, minute = map(int, x.split(':'))
    return hour * 60 + minute

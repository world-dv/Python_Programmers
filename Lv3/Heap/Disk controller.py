def solution(jobs):
    answer = 0
    jobs = sorted(jobs, key = lambda x : (x[1], x[0]))
    job_len = len(jobs)
    
    count = 0
    idx = 0
    while True:
        if len(jobs) == 0:
                break
        if jobs[idx][0] > count:
            idx += 1
            if idx == len(jobs):
                idx = 0
                count += 1
            continue
        else:
            answer += (count - jobs[idx][0]) + jobs[idx][1]
            count += jobs[idx][1]
            jobs.pop(idx)
            idx = 0
    
    return answer // job_len

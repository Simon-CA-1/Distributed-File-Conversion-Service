import threading
lock=threading.Lock()
jobs = []
def add_job(job_size, connectionSocket, message):
    with lock:
        jobs.append([job_size, connectionSocket, message])
        jobs.sort(key=lambda x: x[0])

def get_next_job():
    with lock:
        if not jobs:
            return None
        return jobs.pop(0)
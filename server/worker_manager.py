import threading
lock=threading.Lock()
free_workers=[]
busy_workers=[]

def add_worker(workerSocket):
    with lock:
        free_workers.append(workerSocket)

def choose_worker():
    with lock:
        if not free_workers:
            return None
        worker=free_workers.pop(0)
        busy_workers.append(worker)
        return worker

def work_done(workerSocket):
    with lock:
        if workerSocket in busy_workers:
            busy_workers.remove(workerSocket)
            free_workers.append(workerSocket)

def remove_worker(workerSocket):
    with lock:
        if workerSocket in free_workers:
            free_workers.remove(workerSocket)
        if workerSocket in busy_workers:
            busy_workers.remove(workerSocket)
free_workers=[]
busy_workers=[]

def add_worker(workerSocket):
    free_workers.append(workerSocket)

def choose_worker():
    if not free_workers:
        return None
    else:
        worker=free_workers.pop(0)
        busy_workers.append(worker)
        return worker

def work_done(workerSocket):
    if workerSocket in busy_workers:
        busy_workers.remove(workerSocket)
        free_workers.append(workerSocket)

import threading
from socket import *
import client_handler
import scheduler
import worker_manager
port=5000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(3)
print("SERVER SIDE")
def process_jobs():
    while True:
        job=scheduler.get_next_job()
        if job==None:
            continue
        length,connectionSocket,message=job
        w=worker_manager.choose_worker()
        if w is None:
            scheduler.add_job(length,connectionSocket,message)
            continue
        w.send(message.encode())
        result = w.recv(1024)
        if not result:
            connectionSocket.send("WORKER DISCONNECTED".encode())
            worker_manager.rmove_worker(w)
            connectionSocket.close()
            continue
        worker_manager.work_done(w)
        result = result.decode()
        connectionSocket.send(result.encode())
        connectionSocket.close()
threading.Thread(target=process_jobs, daemon=True).start()
while True:
    connectionSocket,addr=serverSocket.accept()
    thread=threading.Thread(target=client_handler.handle_client,args=(connectionSocket,addr))
    thread.start()
    
    
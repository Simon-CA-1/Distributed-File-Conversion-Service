import threading
from socket import *
import client_handler
import scheduler
import worker_manager
from file_transfer import send_file,receive_file
from config import HOST,PORT
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((HOST,PORT))
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
        send_file(w,message)
        receive_file(w,"output_file.png")
        worker_manager.work_done(w)
        send_file(connectionSocket,"output_file.png")
        connectionSocket.close()
threading.Thread(target=process_jobs, daemon=True).start()
while True:
    connectionSocket,addr=serverSocket.accept()
    thread=threading.Thread(target=client_handler.handle_client,args=(connectionSocket,addr))
    thread.start()
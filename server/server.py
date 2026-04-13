import threading
import ssl
import os
from socket import *
import client_handler
import scheduler
import worker_manager
from file_transfer import send_file,receive_file
from config import HOST,PORT
serverSocket = socket(AF_INET, SOCK_STREAM)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
serverSocket = context.wrap_socket(serverSocket, server_side=True)
serverSocket.bind((HOST, PORT))
serverSocket.listen(3)
print("SERVER SIDE")

def get_output_name(input_path):
    base,ext=os.path.splitext(input_path)
    ext=ext.lower()
    if ext==".jpg":
        return base+".png"
    if ext==".csv":
        return base+".json"
    return input_path

def handle_job(length,connectionSocket,message,w):
    input_name=os.path.basename(message)
    output_name=get_output_name(message)
    w.send(input_name.encode())
    w.recv(1024)
    send_file(w,message)
    receive_file(w,output_name)
    worker_manager.work_done(w)
    send_file(connectionSocket,output_name)
    connectionSocket.close()

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
        thread=threading.Thread(target=handle_job,args=(length,connectionSocket,message,w),daemon=True)
        thread.start()
threading.Thread(target=process_jobs, daemon=True).start()
while True:
    connectionSocket,addr=serverSocket.accept()
    thread=threading.Thread(target=client_handler.handle_client,args=(connectionSocket,addr))
    thread.start()
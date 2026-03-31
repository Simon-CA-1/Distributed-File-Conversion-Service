import os
import worker_manager
import scheduler
from file_transfer import receive_file
def handle_client(connectionSocket,addr):
    message=connectionSocket.recv(1024)
    if not message:
        connectionSocket.close()
        return
    message=message.decode()
    if message=="WORKER":
        worker_manager.add_worker(connectionSocket)
        connectionSocket.send("CONNECTED".encode())
        return
    file_path="input_file"
    receive_file(connectionSocket,file_path)
    size= os.path.getsize(file_path)
    scheduler.add_job(size,connectionSocket,file_path)
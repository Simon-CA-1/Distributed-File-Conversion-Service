import worker_manager
import scheduler
from file_transfer import receive_file
import os

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

    if message=="CLIENT":
        connectionSocket.send("CONNECTED".encode())
        file_path="input_file.jpg"
        receive_file(connectionSocket,file_path)
        size=os.path.getsize(file_path)
        scheduler.add_job(size,connectionSocket,file_path)
        return

    connectionSocket.close()
import worker_manager
import scheduler
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
    scheduler.add_job(len(message),connectionSocket,message)
        
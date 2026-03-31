import worker_manager
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
    w=worker_manager.choose_worker()
    if(w==None):
        connectionSocket.send("NO WORKER".encode())
        connectionSocket.close()
        return
    w.send(message.encode())
    message=w.recv(1024)
    if not message:
        connectionSocket.send("WORKER DISCONNECTED".encode())
        connectionSocket.close()
        return
    worker_manager.work_done(w)
    message=message.decode()
    connectionSocket.send(message.encode())
    connectionSocket.close()
        
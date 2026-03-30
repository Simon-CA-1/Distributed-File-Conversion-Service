import worker_manager
def handle_client(connectionSocket,addr):
    message=connectionSocket.recv(1024)
    message=message.decode()
    if message=="WORKER":
        worker_manager.add_worker(connectionSocket)
        connectionSocket.send("CONNECTED".encode())
        return
    else:
        if worker_manager.free_workers:
            w=worker_manager.choose_worker()
            if(w==None):
                connectionSocket.close()
                return
            w.send(message.encode())
            message=w.recv(1024)
            if not message:
                connectionSocket.close()
                return
            worker_manager.work_done(w)
            message=message.decode()
            connectionSocket.send(message.encode())
            connectionSocket.close()
        else:
            connectionSocket.send("No worker".encode())
            connectionSocket.close()
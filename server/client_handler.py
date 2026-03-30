worker=[]
def handle_client(connectionSocket,addr):
    message=connectionSocket.recv(1024)
    message=message.decode()
    if message=="WORKER":
        worker.append(connectionSocket)
        connectionSocket.send("CONNECTED".encode())
        return
    else:
        if worker:
            w=worker[0]
            w.send(message.encode())
            message=w.recv(1024)
            if not message:
                connectionSocket.close()
                return

            message=message.decode()
            connectionSocket.send(message.encode())
            connectionSocket.close()
        else:
            connectionSocket.send("No worker".encode())
            connectionSocket.close()
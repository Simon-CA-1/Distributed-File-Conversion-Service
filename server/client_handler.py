worker=[]
def handle_client(connectionSocket,addr):
    message=connectionSocket.recv(1024)
    message=message.decode()
    if message=="WORKER":
        worker.append(connectionSocket)
        connectionSocket.send("CONNECTED".encode())
    else:
        message=message+"-processed"
        connectionSocket.send(message.encode())
        connectionSocket.close()
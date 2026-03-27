import threading
from socket import *
port=5000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(3)
print("Server ready")
def handle_client(connectionSocket,addr):
    message=connectionSocket.recv(1024)
    message=message.decode()
    message=message+"-processed"
    connectionSocket.send(message.encode())
    connectionSocket.close()
while True:
    connectionSocket,addr=serverSocket.accept()
    thread=threading.Thread(target=handle_client,args=(connectionSocket,addr))
    thread.start()
    
import threading
from socket import *
import client_handler
import worker_handler
port=5000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(3)
print("Server ready")

while True:
    connectionSocket,addr=serverSocket.accept()
    thread=threading.Thread(target=client_handler.handle_client,args=(connectionSocket,addr))
    thread.start()
    
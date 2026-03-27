from socket import *
port=5000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(3)
print("Server ready")
while True:
    connectionSocket,addr=serverSocket.accept()
    message=connectionSocket.recv(1024).decode()
    message=message+"-processed"
    connectionSocket.send(message.encode())
    connectionSocket.close()
    
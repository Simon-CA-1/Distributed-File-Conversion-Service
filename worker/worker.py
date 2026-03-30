from socket import *
servername="localhost"
serverport=5000
workerSocket=socket(AF_INET,SOCK_STREAM)
workerSocket.connect((servername,serverport))
while True:
    text=workerSocket.recv(1024)
    text=text.decode()
    text=text+"1"
    workerSocket.send(text.encode())

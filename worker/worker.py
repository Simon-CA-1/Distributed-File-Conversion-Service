from socket import *
from config import SERVER_HOST,SERVER_PORT
workerSocket=socket(AF_INET,SOCK_STREAM)
workerSocket.connect((SERVER_HOST,SERVER_HOST))
print("WORKER SIDE")
workerSocket.send("WORKER".encode())
while True:
    text=workerSocket.recv(1024)
    text=text.decode()
    if not text:
        break
    if(text=="CONNECTED"):
        continue
    text=text+"-processed"
    workerSocket.send(text.encode())

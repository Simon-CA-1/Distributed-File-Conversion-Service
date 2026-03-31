from socket import *
from config import SERVER_HOST,SERVER_PORT
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((SERVER_HOST,SERVER_PORT))
print("CLIENT SIDE")
print("Connected to server")
message=input("Enter the message: ")
clientSocket.send(message.encode())
modified_message=clientSocket.recv(1024)
modified_message=modified_message.decode()
if modified_message=="NO WORKER":
    print("No worker available")
else:
    print("Modified message from server:",modified_message)
clientSocket.close()

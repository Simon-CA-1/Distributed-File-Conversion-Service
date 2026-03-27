from socket import *
servername="localhost"
port=5000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((servername,port))
print("Connected to server")
message=input("Enter the message: ")
clientSocket.send(message.encode())
modified_message=clientSocket.recv(1024)
modified_message=modified_message.decode()
clientSocket.close()
print("Modified message from server:",modified_message)
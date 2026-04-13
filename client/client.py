import time
import os
import ssl
from socket import *
from config import SERVER_HOST,SERVER_PORT
from file_transfer import send_file,receive_file

clientSocket = socket(AF_INET, SOCK_STREAM)
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
clientSocket = context.wrap_socket(clientSocket, server_hostname=SERVER_HOST)
clientSocket.connect((SERVER_HOST,SERVER_PORT))

print("CLIENT SIDE")
print("Connected to server")

def get_output_name(input_name):
	base,ext=os.path.splitext(input_name)
	ext=ext.lower()
	if ext==".jpg":
		return base+".png"
	if ext==".csv":
		return base+".json"
	return input_name

message=input("Enter the file path: ")
original_name=os.path.basename(message)
output_name=get_output_name(original_name)

clientSocket.send("CLIENT".encode())
clientSocket.recv(1024)
clientSocket.send(original_name.encode())
clientSocket.recv(1024)

start=time.time()
send_file(clientSocket,message)
receive_file(clientSocket,output_name)
end=time.time()
print("Time Taken:",end-start)
clientSocket.close()
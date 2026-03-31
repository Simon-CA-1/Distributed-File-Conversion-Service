from socket import *
from config import SERVER_HOST,SERVER_PORT
from file_transfer import send_file,receive_file
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((SERVER_HOST,SERVER_PORT))
print("CLIENT SIDE")
print("Connected to server")
message=input("Enter the file path: ")
send_file(clientSocket,message)
receive_file(clientSocket,"output_file")
clientSocket.close()
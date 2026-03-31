from converter import convert_file
from socket import *
from config import SERVER_HOST,SERVER_PORT
from file_transfer import receive_file,send_file

workerSocket=socket(AF_INET,SOCK_STREAM)
workerSocket.connect((SERVER_HOST,SERVER_PORT))

print("WORKER SIDE")

workerSocket.send("WORKER".encode())
workerSocket.recv(1024)

while True:
    receive_file(workerSocket,"input_file.jpg")
    output_file=convert_file("input_file.jpg")
    send_file(workerSocket,output_file)
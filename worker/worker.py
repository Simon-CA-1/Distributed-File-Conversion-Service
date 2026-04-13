from converter import convert_file
import os
import ssl
from socket import *
from config import SERVER_HOST,SERVER_PORT
from file_transfer import receive_file,send_file

workerSocket = socket(AF_INET, SOCK_STREAM)
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
workerSocket = context.wrap_socket(workerSocket, server_hostname=SERVER_HOST)
workerSocket.connect((SERVER_HOST,SERVER_PORT))

print("WORKER SIDE")

workerSocket.send("WORKER".encode())
workerSocket.recv(1024)

while True:
    file_name_data=workerSocket.recv(1024)
    if not file_name_data:
        break
    file_name=os.path.basename(file_name_data.decode())
    if not file_name:
        file_name="input_file"
    workerSocket.send("OK".encode())
    receive_file(workerSocket,file_name)
    output_file=convert_file(file_name)
    send_file(workerSocket,output_file)
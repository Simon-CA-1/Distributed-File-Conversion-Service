import os
from config import FILE_CHUNK_SIZE

def send_file(sock, file_path):
    file_size = os.path.getsize(file_path)
    sock.send(str(file_size).encode())
    sock.recv(1024)
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(FILE_CHUNK_SIZE)
            if not chunk:
                break
            sock.send(chunk)
    print("File sent")


def receive_file(sock, output_path):
    file_size = int(sock.recv(1024).decode())
    sock.send("OK".encode())
    received = 0
    with open(output_path, "wb") as f:
        while received < file_size:
            data = sock.recv(FILE_CHUNK_SIZE)
            if not data:
                break
            f.write(data)
            received += len(data)
    print("File received")
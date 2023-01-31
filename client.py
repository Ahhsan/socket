import socket

c=socket.socket()
c.connect(('localhost',6969))

print(c.recv(1024).decode())

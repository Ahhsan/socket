import socket

s=socket.socket()
s.bind(('localhost',6969))
s.listen()
while True:
    c,add=s.accept()
    print("Successfully connected with ",add)
    c.send(bytes('Welcome to the server','utf-8'))
    c.close()


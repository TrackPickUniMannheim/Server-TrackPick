import cherrypy;
import socketserver;
import socket;
import io;


TCP_IP = '127.0.0.1'
TCP_PORT = 4444
BUFFER_SIZE = 20  # For the fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr);
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print( "received data:", data);
    conn.send(data)  # echo for showing the data received.
conn.close()

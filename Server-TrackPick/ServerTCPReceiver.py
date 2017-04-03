from socketserver import ThreadingMixIn,ForkingMixIn,StreamRequestHandler
import socket,select
import time

TCPInSocket = socket.socket()
host = '127.0.0.1'
print(host)
port = 9999
TCPInSocket.bind((host,port))
TCPInSocket.listen(5)
inputs = [TCPInSocket]
while True:
    rs,ws,es = select.select(inputs,[],[])
    servertime = int(round(time.time()*1000))
    for r in rs:
        if r is TCPInSocket:
            c,addr = TCPInSocket.accept()
            inputs.append(c)
            print((str(addr))+"Server"+(str(servertime)))
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except:
                disconnected = True
            if disconnected:
                inputs.remove(r)
            else:
                print(data)
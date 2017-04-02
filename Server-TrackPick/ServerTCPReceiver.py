from socketserver import ThreadingMixIn,ForkingMixIn,StreamRequestHandler
import socket,select

s = socket.socket()
#host = socket.gethostname()
host = '127.0.0.1'
print(host)
port = 9999
s.bind((host,port))
s.listen(5)
inputs = [s]
while True:
    rs,ws,es = select.select(inputs,[],[])
    for r in rs:
        if r is s:
            c,addr = s.accept()
            inputs.append(c)
            print(addr)
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
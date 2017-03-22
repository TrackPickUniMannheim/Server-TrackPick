import socketserver
import socket

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
The request handler class for server.
Instantiated once per connection to the server, and must override the handle() method to implement communication to the client.
"""


    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999 #Handler for the port and IP with

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    #server.bind(("0.0.0.0", 9999))

    # Activate the server
    server.serve_forever()



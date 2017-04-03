import socketserver
import socket

class ConnectionTCPToCache: #Connection Socket from Cache to Client socket for Database.

    def __init__(self, TCPtoCache=None):
        if TCPtoCache is None:
            self.TCPtoCache = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.TCPtoCache = TCPtoCache
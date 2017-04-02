import socketserver
import socket
import pymongo
import subprocess
import DispatchHandler
import sys

class ConnectionCacheToDBSocket: #Connection Socket from Cache to Client socket for Database.

    def __init__(self, CToDBSock=None):
        if CToDBSock is None:
            self.CToDBSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.CToDBSock = CToDBSock

class GetCollection(object): #Connection Setup to MongoDB (Currently to test_database for connection testing)

    from pymongo import MongoClient
    conn = MongoClient()
    conn = MongoClient('localhost', 27017)
    db = conn.get_database('test_database')
    print(db.collection_names())


class ReadDocument(object): # Crud for reading data from (i.e Test database)
    from pymongo import MongoClient
    read = MongoClient()
    read = MongoClient('localhost',27017)
    dbread = read.get_database('test_database')
    print(dbread.document)






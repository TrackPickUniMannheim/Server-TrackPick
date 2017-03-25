import socketserver
import socket
import pymongo
import subprocess
import DispatchHandler
import sys

class Connection(object): #Connection Setup to MongoDB (Currently to test_database for connection testing)

    from pymongo import MongoClient
    conn = MongoClient()
    conn = MongoClient('localhost', 27017)
    db = conn.get_database('test_database')
    print(db.collection_names())






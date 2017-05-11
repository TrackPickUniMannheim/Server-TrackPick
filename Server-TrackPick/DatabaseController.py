import socketserver
import socket
import pymongo
import subprocess
import DispatchHandler
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) # Connection with the designated queue
channel = connection.channel()

channel.queue_declare(queue='trackPick')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='trackPick')


print(' Now getting data...')
channel.start_consuming()

connection.close()







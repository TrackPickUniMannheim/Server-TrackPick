import sys
import socket
import threading
import time
import pika
from pika import exceptions
import logging

#@Developers: Niranjan Basnet, Zuli Wu

#Module Description: Handling incoming streams for pushing into Rabbitmq queue.

QUIT = False
LOGGER = logging.getLogger(__name__)

class ClientThread(threading.Thread): # Class that implements the client threads in this server

    def __init__(self, client_sock): # Initialize the object, save the socket that this thread will use

        threading.Thread.__init__(self)
        self.client = client_sock

    def run(self): #Thread's main loop where this function returns and the thread is finished and terminated

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) # Connect via pika with localhost

        global QUIT # Declare QUIT as global, and method can change it
        done = False
        data = self.readline() # Read data from the socket and process it
        if data is None:
            #exit()
            sys.exit()


        else:
            while not done:
                # Case where data was received
                if data == "disconnect": # Check whether stream should be stopped or not
                    done = True
                    #print("Found disconnect")
                    self.client.close()
                    #connection.close()
                    return
                elif data.strip() == '': # Check for whitespaces in the incoming streams
                    #print("Found disconnect again")
                    self.client.close()
                    connection.close()
                    print("Connection Closed")
                    QUIT = True
                    #channel.close()
                    #exit()
                    sys.exit()
                    return
                elif data == "connect" or data is not None: # Initiates regardless with connect message or available data.
                                                            # Main loop for data streaming income

                    servertime = int(round(time.time() * 1000))  # Arrival time taken on each
                                                                    # thread and concatinated with the data
                    # Wrapping with external JSON for server time

                    for d in data.split("\n"): # For line wise data in incoming streams
                        data = d
                    outdata = '{"servertime":' + '"' + str(servertime) + '","cdata":' + str(data) + '}'
                    #print(outdata +"\n")
                    print(outdata)
                    #connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
                    channel = connection.channel() # Connect channel through connection

                    channel.queue_declare(queue='trackPick') # Queue declaration with "trackPick"
                    channel.basic_publish(exchange='',
                                          routing_key='trackPick',  # Routing with key "trackPick"
                                          body=outdata)

                    print("Sending Data to queue...")


                    #connection.close()

                    data = self.readline()

            return

    def readline(self):
            # Helper function, reads chars from the socket, and returns
            # them as a lowercase string (to make string uniform for all types)
        data = True
        buffer = ''
        while data:
            data = self.client.recv(1024)
            buffer += data.decode('utf-8')

            if (buffer.find('\n') != -1):
                data = False
        buffer = buffer.strip().lower()
        return buffer

    def writeline(self, text):

        self.client.send(text.strip().decode('utf-8') + '\n')
    def close(self,reply_code=200,reply_text='Normal Shutdown'):
        try:
            if self.is_closed:
                LOGGER.debug('Close called on closed connection (%s): %s',
                             reply_code, reply_text)
                return
            LOGGER.info('Closing connection (%s): %s', reply_code, reply_text)
            self._user_initiated_close = True
            for impl_channel in pika.compat.dictvalues(self._impl._channels):
                channel = impl_channel._get_cookie()
                if channel.is_open:
                    try:
                        channel.close(reply_code, reply_text)
                    except exceptions.ChannelClosed as exc:
                        # Log and suppress broker-closed channel
                        LOGGER.warning('Got Channel Closed exception while closing channel '
                                       'from connection.close: %r', exc)

            self._impl.close(reply_code, reply_text)
        except:
            print("Connection could not be closed")

        #self._flush_output(self._closed_result.is_ready)



class Server:

        # Server class that opens up a socket and listens for incoming connections.
        # Every time a new connection arrives, it creates a new ClientThread thread
        # object and defers the processing of the connection to it.

    def __init__(self):
        self.sock = None
        self.thread_list = []

    def run(self):

            # Server main loop that creates the server (incoming) socket, and listens on it of incoming
            # connections. Once an incoming connection is detected, creates a
            # "ClientThread" to handle it, and goes back to listening mode.

        all_good = False
        try_count = 0

        while not all_good: # Attempt to open the socket if execution is fine

            if 3 < try_count: # Handling if we try more than 3 times but without success that port is occupied.

                sys.exit(1)
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket

                self.sock.bind(('0.0.0.0', 9999)) # Bind it to the interface and port we want to listen on

                self.sock.listen(5) # Listening to 5 Simultaneous connection
                all_good = True
                break
            except socket.error: # Handling Binding Error

                print('Socket connection error... Waiting 5 seconds to retry.') # Short 5 seconds
                                                                                # time for socket replinishment

                del self.sock
                time.sleep(5)
                try_count += 1

        print("Server is up and listening for stream...")

        try:

            while not QUIT:
                try:

                    self.sock.settimeout(0.500)
                    client = self.sock.accept()[0] # Timeout handling for connection error
                except socket.timeout:

                    # No connection detected, sleep for one second, then check
                    # if the global QUIT flag has been set

                    time.sleep(1)
                    if QUIT:
                        print("Received quit command. Shutting down...")
                        break
                    continue

                # Create the ClientThread object and let it handle the incoming
                # connection and data

                new_thread = ClientThread(client)
                #print('Incoming Connection. Started thread ', ) # Current thread information
                #print(new_thread.getName())
                self.thread_list.append(new_thread)
                new_thread.start()

                for thread in self.thread_list: # Thread loop in the thread list
                    if not thread.isAlive():
                        self.thread_list.remove(thread)
                        thread.join()

        except KeyboardInterrupt: # Handling keyboard interrupt for customer user interaction
            print('Ctrl+C pressed... Shutting Down')
        except Exception:
            print('Exception caught: %s\nClosing...') # Clear the list of threads, giving each
                                                        # thread 1 second to finish
        for thread in self.thread_list:
            thread.join(1.0)
        self.sock.close()


if "__main__" == __name__:
    server = Server()
    server.run()

    print("Terminated")

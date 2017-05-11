import sys
import socket
import threading
import time
import pika

QUIT = False


class ClientThread(threading.Thread): # Class that implements the client threads in this server

    def __init__(self, client_sock): # Initialize the object, save the socket that this thread will use

        threading.Thread.__init__(self)
        self.client = client_sock

    def run(self): #Thread's main loop where this function returns and the thread is finished and terminated


        global QUIT # Declare QUIT as global, and method can change it
        done = False
        data = self.readline() # Read data from the socket and process it

        if data is 'b%':
            self.writeline("No data thus quitting")
            QUIT = True
            done = True

        while not done:
            #if 'quit' == data:
                #self.writeline('Quitting...')
                #QUIT = True
                #done = True
            # Case where data was received
            if data is None:
                self.client.close()
            else:
                arrivetime = int(round(time.time() * 1000)) #Arrival time taken on each thread and concatinated with the data
                data = str(data) + "Arrival Time" + str(arrivetime)
                print(data) # Main data for Incoming Data
                connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) # connect via pika with localhost
                channel = connection.channel() # connect channel through connection

                channel.queue_declare(queue='trackPick') # Queue declaration with "trackPick"
                channel.basic_publish(exchange='',
                                      routing_key='trackPick',  # Routing with key "trackPick"
                                      body=data)

                if data is None:
                    QUIT = True
                    done = True

                print("Still Sending data...")
                connection.close()


                data = self.readline()
        self.client.close()
        return

    def readline(self):

            # Helper function, reads up to 1024 chars from the socket, and returns
            # them as a string (lowercase)

        result = self.client.recv(1024)
        if (None != result):
            result = result.strip().lower()
        return result

    def writeline(self, text):

        self.client.send(text.strip().decode('utf-8') + '\n')


class Server:

        # Server class that opens up a socket and listens for incoming connections.
        # Every time a new connection arrives, it creates a new ClientThread thread
        # object and defers the processing of the connection to it.

    def __init__(self):
        self.sock = None
        self.thread_list = []

    def run(self):

            # Server main loop that creates the server (incoming) socket, and listens on it of incoming
            # connections. Once an incomming connection is detected, creates a
            # "ClientThread" to handle it, and goes back to listening mode.

        all_good = False
        try_count = 0

        while not all_good: # Attempt to open the socket if execution is fine

            if 3 < try_count: # Handling if we try more than 3 times but without success that port is occupied.

                sys.exit(1)
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket

                self.sock.bind(('127.0.0.1', 9999)) # Bind it to the interface and port we want to listen on

                self.sock.listen(5) # Listening to 5 Simultanous connection
                all_good = True
                break
            except socket.error: # Handling Binding Error

                print('Socket connection error... Waiting 5 seconds to retry.') # Short 5 seconds time for socket replinishment

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
                print('Incoming Connection. Started thread ', ) # Current thread information
                print(new_thread.getName())
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
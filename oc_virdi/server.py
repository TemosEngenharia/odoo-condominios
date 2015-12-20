import socket
import sys
import binascii
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 9870 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(1)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
#    conn.send(bytearray([0x21, 0x01, 0x00, 0x00, 0x4e, 0x61, 0xbc, 0x00,
#                         0x0b, 0xfe, 0x13, 0xac, 0x14, 0x00, 0x00, 0x00,
#                         0x03, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
#                         0x30, 0x30, 0x30, 0x30, 0x00, 0x00, 0x00, 0x00]))
#    conn.send(bytearray([0x21, 0x21, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
#                         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
#                         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
#                         0x30, 0x30, 0x30, 0x30, 0x00, 0x00, 0x00, 0x00]))
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(4098)
	msg = binascii.hexlify(data).decode()

	print msg[0:4]
	if msg[2:4] == "01":
	        reply = bytearray([0x21, 0x01, 0x00, 0x00, 0x4e, 0x61, 0xbc, 0x00, 
				   0x0b, 0xfe, 0x13, 0xac, 0x14, 0x00, 0x00, 0x00, 
				   0x03, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
				   0x30, 0x30, 0x30, 0x30, 0x00, 0x00, 0x00, 0x00])
        if not data:
            break

     
#        conn.sendall(reply)
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()


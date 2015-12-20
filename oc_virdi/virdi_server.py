# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
from thread import *
import sys
import socket
import binascii
from oc_virdi.models import vd_comms



def definition():
    global data, hex_data, HOST, PORT, server
    data = None
    hex_data = None
    HOST = '172.19.254.11'
    PORT = 9870
    a = HOST.split('.')
    server = '0x{:02x}'.format(int(a[3], 10)) + '0x{:02x}'.format(int(a[2], 10)) + '0x{:02x}'.format(int(a[1], 10)) + '0x{:02x}'.format(int(a[0], 10))
    server = server.replace('0x', '')

if __name__ == '__main__':
    definition()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# Start listening on socket
s.listen(1)
print 'Socket now listening'


# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # infinite loop so that function do not terminate and thread do not end.
    while True:

        # Receiving from client
        global data, hex_data
        data = conn.recv(4096)

        if not data:
            break
        
        hex_data = binascii.hexlify(data).decode()
        print 'Recebendo Pacote'
        print 'Recebido: ', hex_data
        opt = hex_data[2:4]
        replay = vd_comms.options[opt](hex_data, server)
        
        if replay == None:
            break
        
        conn.sendall(replay)
    # came out of loop
    conn.close()

# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    # start new thread takes 1st argument as a function name to be run,
    # second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn, ))

s.close()

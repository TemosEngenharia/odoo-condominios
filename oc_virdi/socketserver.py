# -*- coding: utf-8 -*-
import struct
import string
from datetime import datetime


def definition():
    global data, hex_data, HOST, PORT, server
    data = None
    HOST = '172.19.254.11'
    PORT = 9870
    hex_data = '2101000001000000fdfe13ac340800000002010a03000301303030308000000000026514a2650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    a = HOST.split('.')
    server = '0x{:02x}'.format(int(a[3], 10)) + '0x{:02x}'.format(int(a[2], 10)) + '0x{:02x}'.format(int(a[1], 10)) + '0x{:02x}'.format(int(a[0], 10))
    server = server.replace('0x', '')


def comPackageToSend(_start, _command, _cid, _tid, _param1, _param2, _param3,
                     _errorcode, _extradata):
    datagram = struct.pack('>BBHIIIQII', _start, _command, _cid, _tid, _param1,
                           _param2, _param3, _errorcode, _extradata)
    return datagram


def comPackageReceived(_data):
    datagrama = struct.unpack('>BBHIIIQII', _data)
    return datagrama


def comTerminalLogon():
    print "Logon do Terminal"

    # Sending message to connected client
    print "Sincronismo de Hora"
    a = datetime.strftime(datetime.now(), '%Y.%m.%d.%H.%M.%S')
    b = a.split('.')
    param3 = '0x{:04x}'.format(int(b[0])) + '0x{:02x}'.format(int(b[1])) + '0x{:02x}'.format(int(b[2])) + '0x{:02x}'.format(int(b[3]))

    start = hex_data[0:2]
    command = hex_data[2:4]
    cid = hex_data[4:8]
    tid = hex_data[8:16]
    param1 = '0x00000000'
    param2 = '0x00000000'
    param3 = param3.replace('0x', '')
    print param3
    errorcode = hex_data[48:56]
    extradata = '0x00'
    replay = comPackageToSend(int(start, 16), int(command, 16), int(cid, 16),
                              int(tid, 16), int(param1, 16), int(param2, 16),
                              int(param3, 16), int(errorcode, 16),
                              int(extradata, 16))
    print comPackageReceived(replay)
    # print 'Replay: ', struct.unpack('>BBHIIIQII', replay)

if __name__ == '__main__':
    definition()
    comTerminalLogon()

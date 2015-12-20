# -*- coding: utf-8 -*-
import struct
import binascii
from datetime import datetime


def calc_checksum(s):
    return '%2X' % (-(sum(ord(c) for c in s) % 256) & 0xFF)


def TIME_INFO():
    a = datetime.strftime(datetime.now(), '%Y.%m.%d.%H.%M.%S')
    b = a.split('.')
    _y = '0x{:04x}'.format(int(b[0]))
    _mo = '0x{:02x}'.format(int(b[1]))
    _d = '0x{:02x}'.format(int(b[2]))
    _h = '0x{:02x}'.format(int(b[3]))
    _mi = '0x{:02x}'.format(int(b[4]))
    _se = '0x{:02x}'.format(int(b[5]))
    _re = '0x{:02x}'.format(int(0))
    _vd_date = struct.pack('=HBBBBBB', int(_y, 16), int(_mo, 16),
                           int(_d, 16), int(_h, 16), int(_mi, 16),
                           int(_se, 16), int(_re, 16))

    _vd_date = binascii.hexlify(_vd_date).decode()
    return _vd_date


def comPackC01(_start, _command, _cid, _tid, _param1, _param2, _param3,
               _errorcode, _extradata):
    _headercrc = '0x00'
    _extradatacrc = '0x00'
    datagram = struct.pack('>BBHIIIQIHBB', int(_start, 16), int(_command, 16),
                           int(_cid, 16), int(_tid, 16), int(_param1, 16),
                           int(_param2, 16), int(_param3, 16),
                           int(_errorcode, 16), int(_extradata, 16),
                           int(_headercrc, 16), int(_extradatacrc, 16))

    return datagram


def comPackC02(_start, _command, _cid, _tid, _param1, _param2, _param3,
               _errorcode, _extradata, _data):
    _headercrc = '0x00'
    _extradatacrc = '0x00'
    datagram = struct.pack('>BBHIIIQIHBBQ', int(_start, 16), int(_command, 16),
                           int(_cid, 16), int(_tid, 16), int(_param1, 16),
                           int(_param2, 16), int(_param3, 16),
                           int(_errorcode, 16), int(_extradata, 16),
                           int(_headercrc, 16), int(_extradatacrc, 16),
                           int(_data, 16))
    return datagram

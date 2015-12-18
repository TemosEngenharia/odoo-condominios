# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
from thread import *
import sys
import socket
import binascii
import struct


def definition():
    global data, hex_data, HOST, PORT, server
    data = None
    hex_data = None
    HOST = '172.19.254.11'
    PORT = 9870
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
    start = hex_data[0:2]
    command = hex_data[2:4]
    cid = hex_data[4:8]
    tid = hex_data[8:16]
    param1 = server
    param2 = '0x0a000000'
    param3 = hex_data[40:44]+'000000000000'
    errorcode = hex_data[48:56]
    extradata = '0x00'
    replay = comPackageToSend(int(start, 16), int(command, 16), int(cid, 16),
                              int(tid, 16), int(param1, 16), int(param2, 16),
                              int(param3, 16), int(errorcode, 16),
                              int(extradata, 16))
    conn.sendall(replay)


def comTerminalLogoff():
    print "Logoff do Terminal"


def comTCardSerialNReading():
    print "Leitura do número de Série do Cartão"


def comTimeSync():
    print "Sincronismo de Hora"
    start = hex_data[0:2]
    command = hex_data[2:4]
    cid = hex_data[4:8]
    tid = hex_data[8:16]
    param1 = '0x00000000'
    param2 = '0x00000000'
    param3 = 
    errorcode = hex_data[48:56]
    extradata = '0x00'
    replay = comPackageToSend(int(start, 16), int(command, 16), int(cid, 16),
                              int(tid, 16), int(param1, 16), int(param2, 16),
                              int(param3, 16), int(errorcode, 16),
                              int(extradata, 16))
    conn.sendall(replay)
    


def comSendingTerminalStatus():
    print "Enviando Status do Terminal"

    conn.sendall(bytearray([0x21, 0x0a, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
                            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                            0x30, 0x30, 0x30, 0x30, 0x00, 0x00, 0x00, 0x00]))


def comSendingAuthResult():
    print "Enviando Resultado da Autenticação"


def comCheckUserDuplication():
    print "Verificando duplicidade de usuário"


def comBringMealDataSum():
    print "Buscando informação sobre refeições"


def comBringAntipassBackInfo():
    print "Buscando informação de Antipass Back"


def comBringUserAuthInfo():
    print "Buscando informação de autenticação de usuário"


def comServerAuth():
    print "Autenticação no Servidor"


def comNCNOSignalAlarm():
    print "Sinal de alarme NC/NO"


def comSettingTerminalOption():
    print "Definindo Opção no Terminal"


def comSCardSerialNReading():
    print "Leitura do número de Série do Cartão"


def comTerminalTimeSetting():
    print "Definindo a hora do Terminal"


def comForceOpenTerminalLock():
    print "Abertura forçada da trava associada ao terminal"


def comControlTerminalPeripheralDevice():
    print "Controle do dispositivo periférico do terminal"


def comBringTerminalAuthRecord():
    print "Buscando registro de autenticação do terminal"


def comBringTerminalAuditLog():
    print "Buscando o log de auditoria do terminal"


def comUpgradeTerminalFirmware():
    print "Realizando Upgrade de Firmware no Terminal"


def comBringTerminalFirmwareVersion():
    print "Buscando a Versão do Firmware do Terminal"


def comTerminalUserSync():
    print "Realizando o sincronismo dos usuários no Terminal"


def comSettingTerminalMealOption():
    print "Definindo as opções de refeição no terminal"


def comShinsegyeTerminalMealUserManagement():
    print "Gerenciamento das refeições dos usuários no terminal, Shinsegye"


def comTerminalMealUserManagement():
    print "Gerenciamento das refeições dos usuários no terminal"


def comSmartCardLayoutSetting():
    print "Definição do layout do SmartCard"


def comWiegandCommunicationSetting():
    print "Definição da comunicação da porta Wiegand"


def comTerminalAccessAuthoritySetting():
    print "Definição da hierarquia de acesso no terminal"


def comEmergencyAlarmSetting():
    print "Definição do alarme de emergência"


def comAnnouncementMessageSending():
    print "Enviando mensagem pública aos terminais"

options = {
           '01': comTerminalLogon,
           '02': comTerminalLogoff,
           '06': comTCardSerialNReading,
           '09': comTimeSync,
           '0a': comSendingTerminalStatus,
           '13': comSendingAuthResult,
           '29': comCheckUserDuplication,
           '34': comBringMealDataSum,
           '1a': comBringAntipassBackInfo,
           '1b': comBringUserAuthInfo,
           '1c': comServerAuth,
           '60': comNCNOSignalAlarm,
           '05': comSettingTerminalOption,
           '07': comSCardSerialNReading,
           '08': comTerminalTimeSetting,
           '0c': comForceOpenTerminalLock,
           '0d': comControlTerminalPeripheralDevice,
           '16': comBringTerminalAuthRecord,
           '17': comBringTerminalAuditLog,
           '20': comUpgradeTerminalFirmware,
           '21': comBringTerminalFirmwareVersion,
           '27': comTerminalUserSync,
           '33': comSettingTerminalMealOption,
           '35': comShinsegyeTerminalMealUserManagement,
           '36': comTerminalMealUserManagement,
           '40': comSmartCardLayoutSetting,
           '41': comWiegandCommunicationSetting,
           '42': comTerminalAccessAuthoritySetting,
           '51': comEmergencyAlarmSetting,
           '53': comAnnouncementMessageSending,
}

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
        data = conn.recv(1024)

        hex_data = binascii.hexlify(data).decode()
        opt = hex_data[2:4]
        options[opt]()
        if not data:
            break

    # came out of loop
    conn.close()

# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    # start new thread takes 1st argument as a function name to be run,
    # second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn, ))  # @UndefinedVariable

s.close()

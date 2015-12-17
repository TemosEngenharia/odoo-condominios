# -*- coding: utf-8 -*-
from thread import * #@PydevCodeAnalysisIgnore
import socket
import sys
import binascii

HOST = ''    # Symbolic name meaning all available interfaces
PORT = 9870  # Arbitrary non-privileged port


def definition():
    global data, msg
    data = None
    msg = None


def comTerminalLogon():
    print "Logon do Terminal"
    print '0x' + msg[0:2]
    print '0x' + msg[2:4]
    print '0x' + msg[6:8] + ' 0x' + msg[4:6]
    TID = msg[14:16] + msg[12:14] + msg[10:12] + msg[8:10]
    print int(TID, 16)
    IPv4_a = int(msg[22:24], 16)
    IPv4_b = int(msg[20:22], 16)
    IPv4_c = int(msg[18:20], 16)
    IPv4_d = int(msg[16:18], 16)
    print IPv4_a, '.', IPv4_b,  '.', IPv4_c,  '.', IPv4_d
    TMN = msg[30:32] + msg[28:30] + msg[26:28] + msg[24:26]
    print int(TMN, 16)
    print '[0] - ' + '0x' + msg[32:34]
    print '[1] - ' + '0x' + msg[34:36]
    print '[2] - ' + '0x' + msg[36:38]
    print '[3] - ' + '0x' + msg[38:40]
    print '[4] - ' + '0x' + msg[40:42]
    print '[5] - ' + '0x' + msg[42:44]
    print '[6] - ' + '0x' + msg[44:46]
    print '[7] - ' + '0x' + msg[46:48]
    print '0x' + msg[48:56]
    print '0x' + msg[56:60]
    print '0x' + msg[60:62]
    print '0x' + msg[62:64]

    # Sending message to connected client
    conn.sendall(bytearray([0x21, 0x01, 0x00, 0x00, 0x4e, 0x61, 0xbc, 0x00,
                            0x0b, 0xfe, 0x13, 0xac, 0x14, 0x00, 0x00, 0x00,
                            0x03, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                            0x30, 0x30, 0x30, 0x30, 0x00, 0x00, 0x00, 0x00]))


def comTerminalLogoff():
    print "Logoff do Terminal"


def comTCardSerialNReading():
    print "Leitura do número de Série do Cartão"


def comTimeSync():
    print "Sincronismo de Hora"


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
        global data, msg
        data = conn.recv(4098)
        msg = binascii.hexlify(data).decode()

        opt = msg[2:4]
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
    start_new_thread(clientthread, (conn, ))

s.close()

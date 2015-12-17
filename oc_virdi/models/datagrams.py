# -*- coding: utf-8 -*-
def comTerminalLogon():
    print "Logon do Terminal"


def comTerminalLogoff():
    print "Logoff do Terminal"


def comTCardSerialNReading():
    print "Leitura do número de Série do Cartão"


def comTimeSync():
    print "Sincronismo de Hora"


def comSendingTerminalStatus():
    print "Enviando Status do Terminal"


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

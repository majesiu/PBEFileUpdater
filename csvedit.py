import csv, re

TPEconverter = {'115': 557,'114': 554,'113': 548,'112': 544,'111': 540,'110': 536,'109': 532,'108': 528,'107': 524,'106': 520,'105': 516,'104': 512,'103': 508,'102': 504,'101': 500,'100': 498,'99': 497,'98': 495,'97': 493,'96': 492,'95': 490,'94': 488,'93': 486,'92': 485,'91': 483,'90': 481,'89': 480,'88': 478,'87': 476,'86': 475,'85': 473,'84': 471,'83': 469,'82': 468,'81': 466,'80': 464,'79': 463,'78': 461,'77': 459,'76': 458,'75': 456,'74': 454,'73': 452,'72': 451,'71': 449,'70': 447,'69': 445,'68': 444,'67': 442,'66': 440,'65': 438,'64': 437,'63': 435,'62': 432,'61': 429,'60': 426,'59': 423,'58': 420,'57': 417,'56': 414,'55': 411,'54': 409,'53': 406,'52': 403,'51': 399,'50': 393,'49': 387,'48': 381,'47': 375,'46': 369,'45': 363,'44': 357,'43': 350,'42': 344,'41': 338,'40': 332,'39': 326,'38': 320,'37': 314,'36': 308,'35': 302,'34': 296,'33': 290,'32': 284,'31': 278,'30': 273,'29': 266,'28': 260,'27': 254,'26': 248,'25': 242,'24': 236,'23': 230,'22': 224,'21': 218,'20': 212}
players = dict()

with open('ootp dump.csv', newline='', encoding="cp437") as ootpcsvfile:
    ootpdump = csv.reader(ootpcsvfile, delimiter=',', quotechar='"')
    for row in ootpdump:
        key = row[6]+" "+row[5]
        players[key] = row

with open('roster_pages.csv', newline='', encoding="cp437") as dbcsvfile:
    dbpostdumb = csv.reader(dbcsvfile, delimiter=',', quotechar='"')
    counter = 0
    for row in dbpostdumb:
        if(counter != 0):
            header = re.search(r'] (?P<playername>.*) - (?P<position>\w{1,2})',row[0])
            if(header != None and header.group('position') != 'SP' and header.group('position') != 'RP'):
                battingattrs = re.search(r"BABIP vs LHP: (?P<BABIPvsL>\d{2,3}).*BABIP vs RHP: (?P<BABIPvsR>\d{2,3}).*Avoid K's vs LHP: (?P<AvoidvsL>\d{2,3}).*Avoid K's vs RHP: (?P<AvoidvsR>\d{2,3}).*Gap vs LHP: (?P<GapvsL>\d{2,3}).*Gap vs RHP: (?P<GapvsR>\d{2,3}).*Power vs LHP: (?P<PowervsL>\d{2,3}).*Power vs RHP: (?P<PowervsR>\d{2,3}).*Eye\/Patience vs LHP: (?P<EyevsL>\d{2,3}).*Eye\/Patience vs RHP: (?P<EyevsR>\d{2,3}).*Speed \(Base & Run\): (?P<Speed>\d{2,3}).*Stealing Ability: (?P<Stealing>\d{2,3})",row[1],re.S)
                fieldingattrs = re.search(r"Fielding Range: (?P<Range>\d{2,3}).*Fielding Error: (?P<Error>\d{2,3}).*Fielding/Catching Arm: (?P<Arm>\d{2,3}).*Turn Double Play: (?P<DP>\d{2,3}).*Catcher Ability: (?P<CAB>\d{2,3})",row[1],re.S)
                if(header.group('playername') in players):
                    print(header.group('playername'), header.group('position'))
                    player = players.pop(header.group('playername'))
                    player[31] = TPEconverter[battingattrs.group('BABIPvsL')]
                    player[37] = TPEconverter[battingattrs.group('BABIPvsR')]
                    player[43] = TPEconverter[max(battingattrs.group('BABIPvsL'), battingattrs.group('BABIPvsR'))]
                    player[30] = TPEconverter[battingattrs.group('AvoidvsL')]
                    player[36] = TPEconverter[battingattrs.group('AvoidvsR')]
                    player[42] = TPEconverter[max(battingattrs.group('AvoidvsL'), battingattrs.group('AvoidvsR'))]
                    player[27] = TPEconverter[battingattrs.group('GapvsL')]
                    player[33] = TPEconverter[battingattrs.group('GapvsR')]
                    player[39] = TPEconverter[max(battingattrs.group('GapvsL'), battingattrs.group('GapvsR'))]
                    player[28] = TPEconverter[battingattrs.group('PowervsL')]
                    player[34] = TPEconverter[battingattrs.group('PowervsR')]
                    player[40] = TPEconverter[max(battingattrs.group('PowervsL'), battingattrs.group('PowervsR'))]
                    player[29] = TPEconverter[battingattrs.group('EyevsL')]
                    player[35] = TPEconverter[battingattrs.group('EyevsR')]
                    player[41] = TPEconverter[max(battingattrs.group('EyevsL'), battingattrs.group('EyevsR'))]
                    player[26] = ""
                    player[32] = ""
                    player[47] = int(battingattrs.group('Speed'))*2
                    player[50] = int(battingattrs.group('Speed'))*2
                    player[48] = int(battingattrs.group('Stealing'))*2
                    player[49] = int(battingattrs.group('Stealing'))*2
                    player[67] = int(fieldingattrs.group('Range'))*2
                    player[73] = int(fieldingattrs.group('Range'))*2
                    player[68] = int(fieldingattrs.group('Error'))*2
                    player[74] = int(fieldingattrs.group('Error'))*2
                    player[69] = int(fieldingattrs.group('Arm'))*2
                    player[75] = int(fieldingattrs.group('Arm'))*2
                    player[72] = int(fieldingattrs.group('Arm'))*2
                    player[70] = int(fieldingattrs.group('DP'))*2
                    player[71] = int(fieldingattrs.group('CAB'))*2
                    #temporary framing
                    player[155] = int(fieldingattrs.group('CAB'))*2
                    players[header.group('playername')] = player
        counter += 1
        
with open(r'C:\\Users\\sutem\\Downloads\\Expos\\modified_rooster.csv', 'w', newline='', encoding="cp437") as outputcsvfile:
    writer = csv.writer(outputcsvfile, delimiter=',', quotechar='"')
    for player in players.values():
        writer.writerow(player)
        # counter += 1
        # if(counter > 10): break
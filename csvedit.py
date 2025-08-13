import csv, re

TPEconverter = {'115': 557,'114': 554,'113': 548,'112': 544,'111': 540,'110': 536,'109': 532,'108': 528,'107': 524,'106': 520,'105': 516,'104': 512,'103': 508,'102': 504,'101': 500,'100': 498,'99': 497,'98': 495,'97': 493,'96': 492,'95': 490,'94': 488,'93': 486,'92': 485,'91': 483,'90': 481,'89': 480,'88': 478,'87': 476,'86': 475,'85': 473,'84': 471,'83': 469,'82': 468,'81': 466,'80': 464,'79': 463,'78': 461,'77': 459,'76': 458,'75': 456,'74': 454,'73': 452,'72': 451,'71': 449,'70': 447,'69': 445,'68': 444,'67': 442,'66': 440,'65': 438,'64': 437,'63': 435,'62': 432,'61': 429,'60': 426,'59': 423,'58': 420,'57': 417,'56': 414,'55': 411,'54': 409,'53': 406,'52': 403,'51': 399,'50': 393,'49': 387,'48': 381,'47': 375,'46': 369,'45': 363,'44': 357,'43': 350,'42': 344,'41': 338,'40': 332,'39': 326,'38': 320,'37': 314,'36': 308,'35': 302,'34': 296,'33': 290,'32': 284,'31': 278,'30': 273,'29': 266,'28': 260,'27': 254,'26': 248,'25': 242,'24': 236,'23': 230,'22': 224,'21': 218,'20': 212}

VelocityConverter = {'88 - 90': 8,'89 - 91': 9, '90 - 92': 10, '91 - 93': 11, '92 - 94': 12, '93 - 95': 13, '94 - 96': 14, '95 - 97': 15, '96 - 98': 16, '97 - 99': 17, '98 - 100': 18, '99 - 101': 19, '100+': 20}

players = dict()

def updateBatter(player, battingattrs, fieldingattrs, header):
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

def updatePitcher(player, row, header):
    pitchingattrs = re.search(r"Movement vs.? LHB: (?P<MovesvsL>\d{2,3}).*Movement vs.? RHB: (?P<MovesvsR>\d{2,3}).*Control vs.? LHB: (?P<ControlvsL>\d{2,3}).*Control vs.? RHB: (?P<ControlvsR>\d{2,3}).*Stamina: (?P<Stamina>\d{2,3}).*Holding Runners: (?P<Hold>\d{2,3}).*GB%: (?P<GB>\d{2})",row[1],re.S)
    velocity = re.search(r"Velocity: (?P<Velocity>\d{2,3} - \d{2,3}|\d{3}\+)",row[1])
    player[65] = VelocityConverter[velocity.group('Velocity').strip()]
    player[156] = VelocityConverter[velocity.group('Velocity').strip()]
    print("Velocity:", velocity.group('Velocity').strip(), "Converted:", player[65])
    player[53] = TPEconverter[pitchingattrs.group('MovesvsL')]
    player[55] = TPEconverter[pitchingattrs.group('MovesvsR')]
    player[57] = TPEconverter[max(pitchingattrs.group('MovesvsL'), pitchingattrs.group('MovesvsR'))]
    player[54] = TPEconverter[pitchingattrs.group('ControlvsL')]
    player[56] = TPEconverter[pitchingattrs.group('ControlvsR')]
    player[58] = TPEconverter[max(pitchingattrs.group('ControlvsL'), pitchingattrs.group('ControlvsR'))]
    # player[150] = TPEconverter[pitchingattrs.group('pbabip')]
    #pbabip set to 120 for all pitchers for now
    player[150] = 120
    player[62] = int(pitchingattrs.group('Stamina'))*2
    player[63] = int(pitchingattrs.group('Hold'))*2
    player[64] = pitchingattrs.group('GB')
    #set stuff to 0 for proper calcs
    player[122] = 0
    #set L/R split to 1
    player[123] = 1
    fastball = re.search(r"Fastball: (?P<Fastball>\d{2,3})",row[1])
    if fastball != None:
        player[125] = TPEconverter[fastball.group('Fastball')]
        player[137] = TPEconverter[fastball.group('Fastball')]
    slider = re.search(r"Slider: (?P<Slider>\d{2,3})",row[1])
    if slider != None:
        player[126] = TPEconverter[slider.group('Slider')]
        player[138] = TPEconverter[slider.group('Slider')]
    curveball = re.search(r"Curveball: (?P<Curveball>\d{2,3})",row[1])
    if curveball != None:
        player[127] = TPEconverter[curveball.group('Curveball')]
        player[139] = TPEconverter[curveball.group('Curveball')]    
    changeup = re.search(r"Changeup: (?P<Changeup>\d{2,3})",row[1])
    if changeup != None:
        player[128] = TPEconverter[changeup.group('Changeup')]
        player[140] = TPEconverter[changeup.group('Changeup')]
    cutter = re.search(r"Cutter: (?P<Cutter>\d{2,3})",row[1])
    if cutter != None:
        player[129] = TPEconverter[cutter.group('Cutter')]
        player[141] = TPEconverter[cutter.group('Cutter')]
    sinker = re.search(r"Sinker: (?P<Sinker>\d{2,3})",row[1])
    if sinker != None:
        player[130] = TPEconverter[sinker.group('Sinker')]
        player[142] = TPEconverter[sinker.group('Sinker')]
    splitter = re.search(r"Splitter: (?P<Splitter>\d{2,3})",row[1])
    if splitter != None:
        player[131] = TPEconverter[splitter.group('Splitter')]
        player[143] = TPEconverter[splitter.group('Splitter')]
    forkball = re.search(r"Forkball: (?P<Forkball>\d{2,3})",row[1])
    if forkball != None:
        player[132] = TPEconverter[forkball.group('Forkball')]
        player[144] = TPEconverter[forkball.group('Forkball')]
    screwball = re.search(r"Screwball: (?P<Screwball>\d{2,3})",row[1])
    if screwball != None:
        player[133] = TPEconverter[screwball.group('Screwball')]
        player[145] = TPEconverter[screwball.group('Screwball')]
    circlechange = re.search(r"Circlechange: (?P<Circlechange>\d{2,3})",row[1])
    if circlechange != None:
        player[134] = TPEconverter[circlechange.group('Circlechange')]
        player[146] = TPEconverter[circlechange.group('Circlechange')]
    knucklecurve = re.search(r"Knucklecurve: (?P<Knucklecurve>\d{2,3})",row[1])
    if knucklecurve != None:
        player[135] = TPEconverter[knucklecurve.group('Knucklecurve')]
        player[147] = TPEconverter[knucklecurve.group('Knucklecurve')]
    players[header.group('playername')] = player



        
with open('mpbe_rosters.csv', newline='', encoding="cp437") as ootpcsvfile:
    ootpdump = csv.reader(ootpcsvfile, delimiter=',', quotechar='"')
    counter = 0
    for row in ootpdump:
        if(not row[0].startswith("//")):
            key = row[6]+" "+row[5]
            players[key] = row
            counter += 1
    print("Players loaded: ", counter)  

with open('roster_pages.csv', newline='', encoding="cp437") as dbcsvfile:
    dbpostdumb = csv.reader(dbcsvfile, delimiter=',', quotechar='"')
    counter = 0
    processedBatters = 0
    processedPitchers = 0
    for row in dbpostdumb:
        if(counter != 0):
            header = re.search(r'] (?P<playername>.*) - (?P<position>\w{1,2})',row[0])
            if(header != None):
                if(header.group('position') != 'SP' and header.group('position') != 'RP'):
                    battingattrs = re.search(r"BABIP vs LHP: (?P<BABIPvsL>\d{2,3}).*BABIP vs RHP: (?P<BABIPvsR>\d{2,3}).*Avoid K's vs LHP: (?P<AvoidvsL>\d{2,3}).*Avoid K's vs RHP: (?P<AvoidvsR>\d{2,3}).*Gap vs LHP: (?P<GapvsL>\d{2,3}).*Gap vs RHP: (?P<GapvsR>\d{2,3}).*Power vs LHP: (?P<PowervsL>\d{2,3}).*Power vs RHP: (?P<PowervsR>\d{2,3}).*Eye\/Patience vs LHP: (?P<EyevsL>\d{2,3}).*Eye\/Patience vs RHP: (?P<EyevsR>\d{2,3}).*Speed \(Base & Run\): (?P<Speed>\d{2,3}).*Stealing Ability: (?P<Stealing>\d{2,3})",row[1],re.S)
                    fieldingattrs = re.search(r"Fielding Range: (?P<Range>\d{2,3}).*Fielding Error: (?P<Error>\d{2,3}).*Fielding/Catching Arm: (?P<Arm>\d{2,3}).*Turn Double Play: (?P<DP>\d{2,3}).*Catcher Ability: (?P<CAB>\d{2,3})",row[1],re.S)
                    if(header.group('playername') in players):
                        print(header.group('playername'), header.group('position'))
                        player = players.pop(header.group('playername'))
                        updateBatter(player, battingattrs, fieldingattrs, header)
                        processedBatters += 1
                    # else:
                    #     print("Batter not found in players dictionary:", header.group('playername')," - ", header.group('position'))
                else:
                    if(header.group('playername') in players):
                        print(header.group('playername'), header.group('position'))
                        player = players.pop(header.group('playername'))
                        updatePitcher(player, row, header)
                        processedPitchers += 1
            #         else:
            #             print("Pitcher not found in players dictionary:", header.group('playername')," - ", header.group('position'))

            # else:
            #     print("Header not found in row:", row[0])
        counter += 1
    print("Processed Players: ", counter, " - Processed batters:", processedBatters, " - Processed pitchers:", processedPitchers)

with open(r'C:\\Users\\sutem\\Downloads\\Expos\\modified_rooster_mlpbe.csv', 'w', newline='', encoding="cp437") as outputcsvfile:
    writer = csv.writer(outputcsvfile, delimiter=',', quotechar='"')
    for player in players.values():
        writer.writerow(player)
        # counter += 1
        # if(counter > 10): break


players = dict()

        
with open('pbe_rosters6.csv', newline='', encoding="cp437") as ootpcsvfile:
    ootpdump = csv.reader(ootpcsvfile, delimiter=',', quotechar='"')
    counter = 0
    for row in ootpdump:
        if(not row[0].startswith("//")):
            key = row[6]+" "+row[5]
            players[key] = row
            counter += 1
    print("Players loaded: ", counter)  

with open('roster_pages.csv', newline='', encoding="cp437") as dbcsvfile:
    dbpostdumb = csv.reader(dbcsvfile, delimiter=',', quotechar='"')
    counter = 0
    processedBatters = 0
    for row in dbpostdumb:
        if(counter != 0):
            header = re.search(r'] (?P<playername>.*) - (?P<position>\w{1,2})',row[0])
            if(header != None):
                if(header.group('position') != 'SP' and header.group('position') != 'RP'):
                    battingattrs = re.search(r"BABIP vs LHP: (?P<BABIPvsL>\d{2,3}).*BABIP vs RHP: (?P<BABIPvsR>\d{2,3}).*Avoid K's vs LHP: (?P<AvoidvsL>\d{2,3}).*Avoid K's vs RHP: (?P<AvoidvsR>\d{2,3}).*Gap vs LHP: (?P<GapvsL>\d{2,3}).*Gap vs RHP: (?P<GapvsR>\d{2,3}).*Power vs LHP: (?P<PowervsL>\d{2,3}).*Power vs RHP: (?P<PowervsR>\d{2,3}).*Eye\/Patience vs LHP: (?P<EyevsL>\d{2,3}).*Eye\/Patience vs RHP: (?P<EyevsR>\d{2,3}).*Speed \(Base & Run\): (?P<Speed>\d{2,3}).*Stealing Ability: (?P<Stealing>\d{2,3})",row[1],re.S)
                    fieldingattrs = re.search(r"Fielding Range: (?P<Range>\d{2,3}).*Fielding Error: (?P<Error>\d{2,3}).*Fielding/Catching Arm: (?P<Arm>\d{2,3}).*Turn Double Play: (?P<DP>\d{2,3}).*Catcher Ability: (?P<CAB>\d{2,3})",row[1],re.S)
                    if(header.group('playername') in players):
                        print(header.group('playername'), header.group('position'))
                        updateBatter(player, battingattrs, fieldingattrs, header)
                        processedBatters += 1
                    # else:
                    #     print("Batter not found in players dictionary:", header.group('playername')," - ", header.group('position'))
                else:
                    if(header.group('playername') in players):
                        print(header.group('playername'), header.group('position'))
                        player = players.pop(header.group('playername'))
                        updatePitcher(player, row, header)
                        processedPitchers += 1
            #         else:
            #             print("Pitcher not found in players dictionary:", header.group('playername')," - ", header.group('position'))

            # else:
            #     print("Header not found in row:", row[0])
        counter += 1
    print("Processed Players: ", counter, " - Processed batters:", processedBatters, " - Processed pitchers:", processedPitchers)

with open(r'C:\\Users\\sutem\\Downloads\\Expos\\modified_rooster_pbe.csv', 'w', newline='', encoding="cp437") as outputcsvfile:
    writer = csv.writer(outputcsvfile, delimiter=',', quotechar='"')
    for player in players.values():
        writer.writerow(player)
        # counter += 1
        # if(counter > 10): break
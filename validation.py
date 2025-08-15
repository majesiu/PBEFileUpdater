import csv, re

TPEconverter = {'115': 557,'114': 554,'113': 548,'112': 544,'111': 540,'110': 536,'109': 532,'108': 528,'107': 524,'106': 520,'105': 516,'104': 512,'103': 508,'102': 504,'101': 500,'100': 498,'99': 497,'98': 495,'97': 493,'96': 492,'95': 490,'94': 488,'93': 486,'92': 485,'91': 483,'90': 481,'89': 480,'88': 478,'87': 476,'86': 475,'85': 473,'84': 471,'83': 469,'82': 468,'81': 466,'80': 464,'79': 463,'78': 461,'77': 459,'76': 458,'75': 456,'74': 454,'73': 452,'72': 451,'71': 449,'70': 447,'69': 445,'68': 444,'67': 442,'66': 440,'65': 438,'64': 437,'63': 435,'62': 432,'61': 429,'60': 426,'59': 423,'58': 420,'57': 417,'56': 414,'55': 411,'54': 409,'53': 406,'52': 403,'51': 399,'50': 393,'49': 387,'48': 381,'47': 375,'46': 369,'45': 363,'44': 357,'43': 350,'42': 344,'41': 338,'40': 332,'39': 326,'38': 320,'37': 314,'36': 308,'35': 302,'34': 296,'33': 290,'32': 284,'31': 278,'30': 273,'29': 266,'28': 260,'27': 254,'26': 248,'25': 242,'24': 236,'23': 230,'22': 224,'21': 218,'20': 212}

VelocityConverter = {'88 - 90': 8,'89 - 91': 9, '90 - 92': 10, '91 - 93': 11, '92 - 94': 12, '93 - 95': 13, '94 - 96': 14, '95 - 97': 15, '96 - 98': 16, '97 - 99': 17, '98 - 100': 18, '99 - 101': 19, '100+': 20}

def parseBatter(player, battingattrs, fieldingattrs, header):
    if(int(player[31]) != int(TPEconverter[battingattrs.group('BABIPvsL')])):
        print(header.group('playername'), header.group('position'),"BABIP vs L diff: ", player[31], " ", TPEconverter[battingattrs.group('BABIPvsL')])
    if(int(player[37]) != int(TPEconverter[battingattrs.group('BABIPvsR')])):
        print(header.group('playername'), header.group('position'),"BABIP vs R diff: ", player[37], " ", TPEconverter[battingattrs.group('BABIPvsR')])
    if(int(player[43]) != int(TPEconverter[max(battingattrs.group('BABIPvsL'), battingattrs.group('BABIPvsR'))])):
        print(header.group('playername'), header.group('position'),"BABIP POT diff: ", player[43], " ", TPEconverter[max(battingattrs.group('BABIPvsL'), battingattrs.group('BABIPvsR'))])
    if(int(player[30]) != int(TPEconverter[battingattrs.group('AvoidvsL')])):
        print(header.group('playername'), header.group('position'),"Avoid vs L K's diff: ", player[30], " ", TPEconverter[battingattrs.group('AvoidvsL')])
    if(int(player[36]) != int(TPEconverter[battingattrs.group('AvoidvsR')])):
        print(header.group('playername'), header.group('position'),"Avoid vs R K's diff: ", player[36], " ", TPEconverter[battingattrs.group('AvoidvsR')])
    if(int(player[42]) != int(TPEconverter[max(battingattrs.group('AvoidvsL'), battingattrs.group('AvoidvsR'))])):
        print(header.group('playername'), header.group('position'),"Avoid POT K's diff: ", player[42], " ", TPEconverter[max(battingattrs.group('AvoidvsL'), battingattrs.group('AvoidvsR'))])
    if(int(player[27]) != int(TPEconverter[battingattrs.group('GapvsL')])):  
        print(header.group('playername'), header.group('position'),"Gap vs L diff: ", player[27], " ", TPEconverter[battingattrs.group('GapvsL')])
    if(int(player[33]) != int(TPEconverter[battingattrs.group('GapvsR')])):
        print(header.group('playername'), header.group('position'),"Gap vs R diff: ", player[33], " ", TPEconverter[battingattrs.group('GapvsR')])
    if(int(player[39]) != int(TPEconverter[max(battingattrs.group('GapvsL'), battingattrs.group('GapvsR'))])):
        print(header.group('playername'), header.group('position'),"Gap POT diff: ", player[39], " ", TPEconverter[max(battingattrs.group('GapvsL'), battingattrs.group('GapvsR'))])
    if(int(player[28]) != int(TPEconverter[battingattrs.group('PowervsL')])):
        print(header.group('playername'), header.group('position'),"Power vs L diff: ", player[28], " ", TPEconverter[battingattrs.group('PowervsL')])
    if(int(player[34]) != int(TPEconverter[battingattrs.group('PowervsR')])):
        print(header.group('playername'), header.group('position'),"Power vs R diff: ", player[34], " ", TPEconverter[battingattrs.group('PowervsR')])
    if(int(player[40]) != int(TPEconverter[max(battingattrs.group('PowervsL'), battingattrs.group('PowervsR'))])):
        print(header.group('playername'), header.group('position'),"Power POT diff: ", player[40], " ", TPEconverter[max(battingattrs.group('PowervsL'), battingattrs.group('PowervsR'))])
    if(int(player[29]) != int(TPEconverter[battingattrs.group('EyevsL')])):
        print(header.group('playername'), header.group('position'),"Eye vs L diff: ", player[29], " ", TPEconverter[battingattrs.group('EyevsL')])
    if(int(player[35]) != int(TPEconverter[battingattrs.group('EyevsR')])):
        print(header.group('playername'), header.group('position'),"Eye vs R diff: ", player[35], " ", TPEconverter[battingattrs.group('EyevsR')])
    if(int(player[41]) != int(TPEconverter[max(battingattrs.group('EyevsL'), battingattrs.group('EyevsR'))])):
        print(header.group('playername'), header.group('position'),"Eye POT diff: ", player[41], " ", TPEconverter[max(battingattrs.group('EyevsL'), battingattrs.group('EyevsR'))])
    if(int(player[47]) != (int(battingattrs.group('Speed'))*2)):
        print(header.group('playername'), header.group('position'),"Speed diff: ", player[47], " ", int(battingattrs.group('Speed'))*2)
    if(int(player[50]) != (int(battingattrs.group('Speed'))*2)):
        print(header.group('playername'), header.group('position'),"Speed diff: ", player[50], " ", int(battingattrs.group('Speed'))*2)
    if(int(player[48]) != (int(battingattrs.group('Stealing'))*2)):
        print(header.group('playername'), header.group('position'),"Stealing diff: ", player[48], " ", int(battingattrs.group('Stealing'))*2)
    if(int(player[49]) != (int(battingattrs.group('Stealing'))*2)):
        print(header.group('playername'), header.group('position'),"Stealing diff: ", player[49], " ", int(battingattrs.group('Stealing'))*2)
    if(int(player[67]) != (int(fieldingattrs.group('Range'))*2)):
        print(header.group('playername'), header.group('position'),"Range diff: ", player[67], " ", int(fieldingattrs.group('Range'))*2)
    if(int(player[73]) != (int(fieldingattrs.group('Range'))*2)):
        print(header.group('playername'), header.group('position'),"Range diff: ", player[73], " ", int(fieldingattrs.group('Range'))*2)
    if(int(player[68]) != (int(fieldingattrs.group('Error'))*2)):
        print(header.group('playername'), header.group('position'),"Error diff: ", player[68], " ", int(fieldingattrs.group('Error'))*2)
    if(int(player[74]) != (int(fieldingattrs.group('Error'))*2)):
        print(header.group('playername'), header.group('position'),"Error diff: ", player[74], " ", int(fieldingattrs.group('Error'))*2)
    if(int(player[69]) != (int(fieldingattrs.group('Arm'))*2)):
        print(header.group('playername'), header.group('position'),"Arm diff: ", player[69], " ", int(fieldingattrs.group('Arm'))*2)
    if(int(player[75]) != (int(fieldingattrs.group('Arm'))*2)):
        print(header.group('playername'), header.group('position'),"Arm diff: ", player[75], " ", int(fieldingattrs.group('Arm'))*2)
    if(int(player[72]) != (int(fieldingattrs.group('Arm'))*2)):
        print(header.group('playername'), header.group('position'),"Arm diff: ", player[72], " ", int(fieldingattrs.group('Arm'))*2)
    if(int(player[70]) != (int(fieldingattrs.group('DP'))*2)):
        print(header.group('playername'), header.group('position'),"DP diff: ", player[70], " ", int(fieldingattrs.group('DP'))*2)
    if(int(player[71]) != (int(fieldingattrs.group('CAB'))*2)):
        print(header.group('playername'), header.group('position'),"Catcher Ability diff: ", player[71], " ", int(fieldingattrs.group('CAB'))*2)
    #temporary framing
    if(int(player[155]) != (int(fieldingattrs.group('CAB'))*2)):
        print(header.group('playername'), header.group('position'),"Catcher Framing diff: ", player[155], " ", int(fieldingattrs.group('CAB'))*2)

def parsePitcher(player, row, header):
    pitchingattrs = re.search(r"Movement vs.? LHB: (?P<MovesvsL>\d{2,3}).*Movement vs.? RHB: (?P<MovesvsR>\d{2,3}).*Control vs.? LHB: (?P<ControlvsL>\d{2,3}).*Control vs.? RHB: (?P<ControlvsR>\d{2,3}).*Stamina: (?P<Stamina>\d{2,3}).*Holding Runners: (?P<Hold>\d{2,3}).*GB%: (?P<GB>\d{2})",row[1],re.S)
    velocity = re.search(r"Velocity: (?P<Velocity>\d{2,3} - \d{2,3}|\d{3}\+)",row[1])
    if(int(player[65]) != VelocityConverter[velocity.group('Velocity').strip()]):
        print(header.group('playername'), header.group('position'),"Velocity diff: ", player[65], " ", VelocityConverter[velocity.group('Velocity').strip()])
    if(int(player[156]) != VelocityConverter[velocity.group('Velocity').strip()]):
        print(header.group('playername'), header.group('position'),"Velocity Pot diff: ", player[156], " ", VelocityConverter[velocity.group('Velocity').strip()])
    if(int(player[53]) != TPEconverter[pitchingattrs.group('MovesvsL')]):
        print(header.group('playername'), header.group('position'),"Moves vs L diff: ", player[53], " ", TPEconverter[pitchingattrs.group('MovesvsL')])
    if(int(player[55]) != TPEconverter[pitchingattrs.group('MovesvsR')]):
        print(header.group('playername'), header.group('position'),"Moves vs R diff: ", player[55], " ", TPEconverter[pitchingattrs.group('MovesvsR')])
    if(int(player[57]) != TPEconverter[max(pitchingattrs.group('MovesvsL'), pitchingattrs.group('MovesvsR'))]):
        print(header.group('playername'), header.group('position'),"Moves POT diff: ", player[57], " ", TPEconverter[max(pitchingattrs.group('MovesvsL'), pitchingattrs.group('MovesvsR'))])
    if(int(player[54]) != TPEconverter[pitchingattrs.group('ControlvsL')]):
        print(header.group('playername'), header.group('position'),"Control vs L diff: ", player[54], " ", TPEconverter[pitchingattrs.group('ControlvsL')])
    if(int(player[56]) != TPEconverter[pitchingattrs.group('ControlvsR')]):
        print(header.group('playername'), header.group('position'),"Control vs R diff: ", player[56], " ", TPEconverter[pitchingattrs.group('ControlvsR')])
    if(int(player[58]) != TPEconverter[max(pitchingattrs.group('ControlvsL'), pitchingattrs.group('ControlvsR'))]):
        print(header.group('playername'), header.group('position'),"Control POT diff: ", player[58], " ", TPEconverter[max(pitchingattrs.group('ControlvsL'), pitchingattrs.group('ControlvsR'))])
    if(int(player[150]) != 120):
        print(header.group('playername'), header.group('position'),"pbabip diff: ", player[150], " 120")
    if(int(player[62]) != (int(pitchingattrs.group('Stamina'))*2)):
        print(header.group('playername'), header.group('position'),"Stamina diff: ", player[62], " ", int(pitchingattrs.group('Stamina'))*2)
    if(int(player[63]) != (int(pitchingattrs.group('Hold'))*2)):
        print(header.group('playername'), header.group('position'),"Hold diff: ", player[63], " ", int(pitchingattrs.group('Hold'))*2)
    if(player[64] != pitchingattrs.group('GB')):
        print(header.group('playername'), header.group('position'),"GB diff: ", player[64], " ", pitchingattrs.group('GB'))
    if(float(player[123]) != float(1)):
        print(header.group('playername'), header.group('position'),"L/R split diff: ", player[123], " 1")
    fastball = re.search(r"Fastball: (?P<Fastball>\d{2,3})",row[1])
    if fastball != None and (int(player[125]) != TPEconverter[fastball.group('Fastball')]):
        print(header.group('playername'), header.group('position'),"Fastball diff: ", player[125], " ", TPEconverter[fastball.group('Fastball')])
    if fastball != None and (int(player[137]) != TPEconverter[fastball.group('Fastball')]):
        print(header.group('playername'), header.group('position'),"Fastball Pot diff: ", player[137], " ", TPEconverter[fastball.group('Fastball')])
    slider = re.search(r"Slider: (?P<Slider>\d{2,3})",row[1])
    if slider != None and int(player[126]) != TPEconverter[slider.group('Slider')]:
        print(header.group('playername'), header.group('position'),"Slider diff: ", player[126], " ", TPEconverter[slider.group('Slider')]) 
    if slider != None and int(player[138]) != TPEconverter[slider.group('Slider')]:
        print(header.group('playername'), header.group('position'),"Slider Pot diff: ", player[138], " ", TPEconverter[slider.group('Slider')])
    curveball = re.search(r"Curveball: (?P<Curveball>\d{2,3})",row[1])
    if curveball != None and int(player[127]) != TPEconverter[curveball.group('Curveball')]:
        print(header.group('playername'), header.group('position'),"Curveball diff: ", player[127], " ", TPEconverter[curveball.group('Curveball')])
    if curveball != None and int(player[139]) != TPEconverter[curveball.group('Curveball')]:
        print(header.group('playername'), header.group('position'),"Curveball Pot diff: ", player[139], " ", TPEconverter[curveball.group('Curveball')])
    changeup = re.search(r"Changeup: (?P<Changeup>\d{2,3})",row[1])
    if changeup != None and int(player[128]) != TPEconverter[changeup.group('Changeup')]:
        print(header.group('playername'), header.group('position'),"Changeup diff: ", player[128], " ", TPEconverter[changeup.group('Changeup')])
    if changeup != None and int(player[140]) != TPEconverter[changeup.group('Changeup')]:
        print(header.group('playername'), header.group('position'),"Changeup Pot diff: ", player[140], " ", TPEconverter[changeup.group('Changeup')])
    cutter = re.search(r"Cutter: (?P<Cutter>\d{2,3})",row[1])
    if cutter != None and (int(player[129]) != TPEconverter[cutter.group('Cutter')]):
        print(header.group('playername'), header.group('position'),"Cutter diff: ", player[129], " ", TPEconverter[cutter.group('Cutter')])
    if cutter != None and (int(player[141]) != TPEconverter[cutter.group('Cutter')]):
        print(header.group('playername'), header.group('position'),"Cutter Pot diff: ", player[141], " ", TPEconverter[cutter.group('Cutter')]) 
    sinker = re.search(r"Sinker: (?P<Sinker>\d{2,3})",row[1])
    if sinker != None and (int(player[130]) != TPEconverter[sinker.group('Sinker')]):
        print(header.group('playername'), header.group('position'),"Sinker diff: ", player[130], " ", TPEconverter[sinker.group('Sinker')])
    if sinker != None and (int(player[142]) != TPEconverter[sinker.group('Sinker')]):
        print(header.group('playername'), header.group('position'),"Sinker Pot diff: ", player[142], " ", TPEconverter[sinker.group('Sinker')]) 
    splitter = re.search(r"Splitter: (?P<Splitter>\d{2,3})",row[1])
    if splitter != None and (int(player[131]) != TPEconverter[splitter.group('Splitter')]):
        print(header.group('playername'), header.group('position'),"Splitter diff: ", player[131], " ", TPEconverter[splitter.group('Splitter')])
    if splitter != None and (int(player[143]) != TPEconverter[splitter.group('Splitter')]):
        print(header.group('playername'), header.group('position'),"Splitter Pot diff: ", player[143], " ", TPEconverter[splitter.group('Splitter')]) 
    forkball = re.search(r"Forkball: (?P<Forkball>\d{2,3})",row[1])
    if forkball != None:
        if(int(player[132]) != TPEconverter[forkball.group('Forkball')]):
            print(header.group('playername'), header.group('position'),"Forkball diff: ", player[132], " ", TPEconverter[forkball.group('Forkball')])
        if(int(player[144]) != TPEconverter[forkball.group('Forkball')]):
            print(header.group('playername'), header.group('position'),"Forkball Pot diff: ", player[144], " ", TPEconverter[forkball.group('Forkball')])
    screwball = re.search(r"Screwball: (?P<Screwball>\d{2,3})",row[1])
    if screwball != None and (int(player[133]) != TPEconverter[screwball.group('Screwball')]):
        print(header.group('playername'), header.group('position'),"Screwball diff: ", player[133], " ", TPEconverter[screwball.group('Screwball')])
    if screwball != None and (int(player[145]) != TPEconverter[screwball.group('Screwball')]):
        print(header.group('playername'), header.group('position'),"Screwball Pot diff: ", player[145], " ", TPEconverter[screwball.group('Screwball')]) 
    circlechange = re.search(r"Circlechange: (?P<Circlechange>\d{2,3})",row[1])
    if circlechange != None and (int(player[134]) != TPEconverter[circlechange.group('Circlechange')]):
        print(header.group('playername'), header.group('position'),"Circlechange diff: ", player[134], " ", TPEconverter[circlechange.group('Circlechange')])
    if circlechange != None and (int(player[146]) != TPEconverter[circlechange.group('Circlechange')]):
        print(header.group('playername'), header.group('position'),"Circlechange Pot diff: ", player[146], " ", TPEconverter[circlechange.group('Circlechange')])
    knucklecurve = re.search(r"Knucklecurve: (?P<Knucklecurve>\d{2,3})",row[1])
    if knucklecurve != None and (int(player[135]) != TPEconverter[knucklecurve.group('Knucklecurve')]):
        print(header.group('playername'), header.group('position'),"Knucklecurve diff: ", player[135], " ", TPEconverter[knucklecurve.group('Knucklecurve')])
    if knucklecurve != None and (int(player[147]) != TPEconverter[knucklecurve.group('Knucklecurve')]):
        print(header.group('playername'), header.group('position'),"Knucklecurve Pot diff: ", player[147], " ", TPEconverter[knucklecurve.group('Knucklecurve')])

players = dict()

with open('pbe_rostersw4.csv', newline='', encoding="UTF-8") as ootpcsvfile:
    ootpdump = csv.reader(ootpcsvfile, delimiter=',', quotechar='"')
    counter = 0
    for row in ootpdump:
        if(not row[0].startswith("//")):
            key = (row[6]+" "+row[5]).lower().strip()
            players[key] = row
            counter += 1
    print("Loaded", counter, "players from pbe_rosters.csv")

    
with open('mpbe_rostersw4.csv', newline='', encoding="UTF-8") as ootpcsvfile:
    ootpdump = csv.reader(ootpcsvfile, delimiter=',', quotechar='"')
    counter = 0
    for row in ootpdump:
        if(not row[0].startswith("//")):
            key = (row[6]+" "+row[5]).lower().strip()
            players[key] = row
            counter += 1
    print("Loaded", counter, "players from mpbe_rosters.csv")

with open('roster_pages.csv', newline='', encoding="UTF-8") as dbcsvfile:
    dbpostdumb = csv.reader(dbcsvfile, delimiter=',', quotechar='"')
    counter = 0
    processedBatters = 0
    processedPitchers = 0
    for row in dbpostdumb:
        if(counter != 0):
            header = re.search(r'] (?P<playername>.*) - (?P<position>\w{1,2})',row[0], re.IGNORECASE)
            if(header != None):
                if(header.group('position') != "SP" and header.group('position') != "RP"):
                    battingattrs = re.search(r"BABIP vs LHP: (?P<BABIPvsL>\d{2,3}).*BABIP vs RHP: (?P<BABIPvsR>\d{2,3}).*Avoid K's vs LHP: (?P<AvoidvsL>\d{2,3}).*Avoid K's vs RHP: (?P<AvoidvsR>\d{2,3}).*Gap vs LHP: (?P<GapvsL>\d{2,3}).*Gap vs RHP: (?P<GapvsR>\d{2,3}).*Power vs LHP: (?P<PowervsL>\d{2,3}).*Power vs RHP: (?P<PowervsR>\d{2,3}).*Eye\/Patience vs LHP: (?P<EyevsL>\d{2,3}).*Eye\/Patience vs RHP: (?P<EyevsR>\d{2,3}).*Speed \(Base & Run\): (?P<Speed>\d{2,3}).*Stealing Ability: (?P<Stealing>\d{2,3})",row[1],re.S)
                    fieldingattrs = re.search(r"Fielding Range: (?P<Range>\d{2,3}).*Fielding Error: (?P<Error>\d{2,3}).*Fielding/Catching Arm: (?P<Arm>\d{2,3}).*Turn Double Play: (?P<DP>\d{2,3}).*Catcher Ability: (?P<CAB>\d{2,3})",row[1],re.S)
                    if(header.group('playername').lower().strip() in players):
                        # print(header.group('playername'), header.group('position'))
                        player = players.pop(header.group('playername').lower().strip())
                        parseBatter(player, battingattrs, fieldingattrs, header)    
                        processedBatters += 1
                    else:
                        print("Batter not found in players dictionary:", header.group('playername').encode("utf-8")," - ", header.group('position'), " | ", row[0].encode("utf-8"))
                # else:
                #     if(header.group('playername').lower().strip() in players):
                #         # print(header.group('playername'), header.group('position'))
                #         player = players.pop(header.group('playername').lower().strip())
                #         parsePitcher(player, row, header)
                #         processedPitchers += 1
                #     else:
                        print("Pitcher not found in players dictionary:", header.group('playername').encode("utf-8")," - ", header.group('position'), " | ", row[0].encode("utf-8"))

            else:
                print("Wrong player thread title: " ,row[0])
        counter += 1
    print("Processed Players: ", counter, " - Processed batters:", processedBatters, " - Processed pitchers:", processedPitchers)
        

import csv, re

with open('roster_pages.csv', newline='', encoding="cp437") as csvfile:
    dbpostdumb = csv.reader(csvfile, delimiter=',', quotechar='"')
    counter = 0
    for row in dbpostdumb:
        if(counter != 0):
            header = re.search(r'] (?P<playername>.*) - (?P<position>\w{1,2})',row[0])
            # print(row)
            if(header.group('position') != 'SP' and header.group('position') != 'RP'):
                print(header.group(1,2))
                battingattrs = re.search(r"BABIP vs LHP: (?P<BABIPvsL>\d{2,3}).*BABIP vs RHP: (?P<BABIPvsR>\d{2,3}).*Avoid K's vs LHP: (?P<AvoidvsL>\d{2,3}).*Avoid K's vs RHP: (?P<AvoidvsR>\d{2,3}).*Gap vs LHP: (?P<GapvsL>\d{2,3}).*Gap vs RHP: (?P<GapvsR>\d{2,3}).*Power vs LHP: (?P<PowervsL>\d{2,3}).*Power vs RHP: (?P<PowervsR>\d{2,3}).*Eye\/Patience vs LHP: (?P<EyevsL>\d{2,3}).*Eye\/Patience vs RHP: (?P<EyevsR>\d{2,3}).*Speed \(Base & Run\): (?P<Speed>\d{2,3}).*Stealing Ability: (?P<Stealing>\d{2,3})",row[1],re.S)
                print(battingattrs.group(1,2,3,4,5,6,7,8,9,10,11,12))
                fieldingattrs = re.search(r"Fielding Range: (?P<Range>\d{2,3}).*Fielding Error: (?P<Error>\d{2,3}).*Fielding/Catching Arm: (?P<Arm>\d{2,3}).*Turn Double Play: (?P<DP>\d{2,3}).*Catcher Ability: (?P<CAB>\d{2,3})",row[1],re.S)
                print(battingattrs.group(1,2,3,4,5))
        counter += 1
        #LastName,FirstName,Contact vL,Gap vL,Power vL,Eye vL,Avoid K vL,BABIP vL,Contract Vr,Gap Vr,Power vR,Eye vR,Ks vR,BABIP vR,Contact Pot,Gap Pot,Power Pot,Eye Pot,Ks Pot,BABIP Pot,speed,steal rate,steal,running,sac bunt,bunt hit,
        # Infield Range,Infield Error,Infield Arm,DP,CatcherAbil,Catcher Arm,OF Range,OF Error,OF Arm,Catcher Framing	
        #Move vL,Control vL,Movement vR,Control vR,Move Pot,Control Pot,Stamina,Hold,GB%,Velocity,
        # Stuff Overall,Stuff R/L split,Stuff Pot.,Fastball (scale: 0-5),Slider,Curveball,Changeup,Cutter,Sinker,Splitter,Forkball,Screwball,Circlechange,Knucklecurve,Knuckleball,
        # Fastball Pot.(scale: 0-5),Slider Pot.,Curveball Pot.,Changeup Pot.,Cutter Pot.,Sinker Pot.,Splitter Pot.,Forkball Pot.,Screwball Pot.,Circlechange Pot.,Knucklecurve Pot.,Knuckleball Pot.,pbabip,Velo Pot			
        
import csv

with open('ootp dump.csv', newline='', encoding="cp437") as csvfile:
    ootpdump = csv.reader(csvfile, delimiter=',', quotechar='"')
    players = dict()
    for row in ootpdump:
        key = row[6]+" "+row[5]
        players[key] = row
    print(players["Paulo Zalewski"])
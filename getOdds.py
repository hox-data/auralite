from json.tool import main
from msilib.schema import ODBCAttribute
from unittest.mock import patch
from bs4 import BeautifulSoup as bs
import os
import json


mainPath = os.path.dirname(__file__) #main path to root folder

folderOdds = r'\pages\odds'  #str of the path to odds
folderResults = r'\pages\results'  #str of the path to results

pathToOddDir = str(mainPath) + folderOdds   #path to the folder where the odd pages are located
pathToResultsDir = str(mainPath) + folderResults #path to the folder where the results pages are located

listOdds = [f for f in os.listdir(pathToOddDir) if f.endswith('.html')] #list of files in odds
listResults = [f for f in os.listdir(pathToResultsDir) if f.endswith('.html')]  #list of files in results

participants = []
odds_ = []
pointWin = []
winnerName = []

out_racers = str(mainPath) + '\\out\\' + 'racers.txt'
out_odds = str(mainPath) + '\\out\\' + 'odds.txt'
out_winner_name = str(mainPath) + '\\out\\' + 'winner_names.txt'
out_winner_odd = str(mainPath) + '\\out\\' + 'winner_odd.txt'

# print(listResults)

for results in listOdds:
    fullPath = str(pathToOddDir) + '\\' + results
    with open(fullPath) as f:
        soup = bs(f.read(), 'html.parser')
    for div in soup.find_all("div", class_="vr-ParticipantVirtual_Name"):
            div.find("div", class_="vr-ParticipantVirtual_Identifier")
            raceParticipants = div.get_text()
            participants.append(raceParticipants)

    participants.append('\n')

print(participants)

with open(out_racers, 'w') as f:
    f.write(json.dumps(participants))

participants.clear()



for odds in listOdds:   
    fullPath = str(pathToOddDir) + '\\' + odds
    with open(fullPath) as f:
        soup = bs(f.read(), 'html.parser')
    for div in soup.find_all("div", class_="vr-ParticipantVirtualOddsOnly gl-Participant_General"):
            div.find("div", class_="vr-ParticipantVirtualOddsOnly_Odds")
            raceOdds = div.get_text()
            odds_.append(raceOdds)
    
    odds_.append('\n')

print(odds_)

with open(out_odds, 'w') as f:
    f.write(json.dumps(odds_))

odds_.clear()

for winner in listResults:
    fullPath = str(pathToResultsDir) + '\\' + winner
    with open(fullPath)as f:
        soup = bs(f.read(), 'html.parser')
    for div in soup.find_all("div", class_="vrr-ParticipantInfo", limit=1):
            winner = soup.find("div", class_="vrr-ParticipantInfo_Runner")
            winnerName.append(winner.get_text())

    winnerName.append('\n')

print(winnerName)

with open(out_winner_name, 'w') as f:
    f.write(json.dumps(winnerName))

winnerName.clear()

for points in listResults:
    fullPath = str(pathToResultsDir) + '\\' + points
    with open(fullPath) as f:
        soup = bs(f.read(), 'html.parser')
    for div in soup.find_all("div", class_="vrr-OutrightParticipant gl-Market_General-cn1", limit=1):
        pts = soup.find("div", class_="vrr-Price")
        pointWin.append(pts.get_text())

    pointWin.append('\n')

print(pointWin)

with open(out_winner_odd, 'w') as f:
    f.write(json.dumps(pointWin))

pointWin.clear()
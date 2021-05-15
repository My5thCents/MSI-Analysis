import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
import math as math

champions = pd.read_csv("ChampionsPicked.csv")
picks = champions[champions["Pick/Ban"] == "Pick"]
bans = champions[(champions["Pick/Ban"] == "Ban") & (champions["Champion"] != "None")]

# get a list of all champs picked
champs_picked = sorted(picks.Champion.unique())
# get a list of all banned champs
champs_banned = sorted(bans.Champion.unique())
# get a list of all champs picked or banned
champs_total = sorted(champions.Champion.unique())
# get a list of all teams
teams = sorted(picks.Team.unique())

teamWinLoss = OrderedDict()
for i in teams:
    teamWinLoss[i] = [0, 0]

# get a dictionary for each team of their wins and losses
for index, row in picks.iterrows():
    if row["GameResult"] == "Win":
        teamWinLoss[row["Team"]][0] += 1
    else:
        teamWinLoss[row["Team"]][1] += 1
for i in teamWinLoss.keys():
    teamWinLoss[i][0] = teamWinLoss[i][0] // 5
    teamWinLoss[i][1] = teamWinLoss[i][1] // 5

# get a dictionary for each teams win/loss ratio
teamWinRate = OrderedDict()
for i in teams:
    teamWinRate[i] = teamWinLoss[i][0] / (teamWinLoss[i][0] + teamWinLoss[i][1])

# track each champions win/loss
champWinLoss = OrderedDict()
for i in champs_picked:
    champWinLoss[i] = [0, 0]

for index, row in picks.iterrows():
    if row["GameResult"] == "Win":
        champWinLoss[row["Champion"]][0] += 1
    else:
        champWinLoss[row["Champion"]][1] += 1

# Track each champions win rate
champWinRate = OrderedDict()
for i in champs_picked:
    champWinRate[i] = champWinLoss[i][0] / (champWinLoss[i][0] + champWinLoss[i][1])

# Track only the champs who have > 5 games played
champWinRate5Games = OrderedDict()
for i in champWinLoss:
    if champWinLoss[i][0] + champWinLoss[i][1] >= 5:
        champWinRate5Games[i] = champWinLoss[i][0] / (champWinLoss[i][0] + champWinLoss[i][1])

# Find the expected win totals of each champ with > 5 games
champExpectedWins = OrderedDict()
for i in champs_picked:
    champExpectedWins[i] = 0
for index, row in picks.iterrows():
    champExpectedWins[row["Champion"]] += (teamWinRate[row["Team"]]*(1-teamWinRate[row["TeamVS"]])) / ((teamWinRate[row["Team"]]*(1-teamWinRate[row["TeamVS"]]) + teamWinRate[row["TeamVS"]]*(1-teamWinRate[row["TeamVS"]]))+0.0000001)
champExpectedWins5Games = OrderedDict()
for i in champWinRate5Games.keys():
    champExpectedWins5Games[i] = champExpectedWins[i]

champExpectedWinRate5Games = OrderedDict()
for i in champExpectedWins5Games.keys():
    champExpectedWinRate5Games[i] = champExpectedWins5Games[i] / (champWinLoss[i][0] + champWinLoss[i][1])

expectedWinRateMinusActual = OrderedDict()
expectedWinsMinusActual = OrderedDict()

for i in champExpectedWins5Games:
    expectedWinsMinusActual[i] = champWinLoss[i][0] - champExpectedWins5Games[i]

for i in champExpectedWins5Games:
    expectedWinRateMinusActual[i] = champWinRate[i] - champExpectedWinRate5Games[i]

champWinsList = []
champExpectedWinsList = []
for i in champWinRate5Games:
    champWinsList.append(champWinLoss[i][0])
    champExpectedWinsList.append(champExpectedWins5Games[i])


champAdjustedWinRateList = []
for i in expectedWinRateMinusActual:
    champAdjustedWinRateList.append(expectedWinRateMinusActual[i]*100)

CIpicked5 = OrderedDict()
for i in champExpectedWins5Games.keys():
    CIpicked5[i] = 2*math.sqrt((champWinLoss[i][0]/(sum(champWinLoss[i]))*champWinLoss[i][1]/(sum(champWinLoss[i])))
                               / sum(champWinLoss[i]))
print(CIpicked5)
CIpicked5List = []
for i in CIpicked5.keys():
    CIpicked5List.append(CIpicked5[i]*100)

df = pd.DataFrame({"Win Rate - Expected Win Rate": champAdjustedWinRateList},
                  index=expectedWinRateMinusActual.keys())
ax = df.plot.bar(yerr=CIpicked5List)
ax.set_title("Win Rate - Expected Win Rate")
ax.get_legend().remove()
x_offset = -0.3
y_offset = 0.3
for p in ax.patches:
    b = p.get_bbox()
    val = "{:+.2f}".format(b.y1 + b.y0)
    if float(val) > 0:
        ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
    if float(val) < 0:
        ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 - 6*y_offset), fontsize=8)

plt.show(block=True)

champBans = OrderedDict()
for i in champs_banned:
    champBans[i] = 0

for index, row in bans.iterrows():
    champBans[row["Champion"]] += 1

champsBanned5 = OrderedDict()
for i in champBans.keys():
    if champBans[i] >= 5:
        champsBanned5[i] = champBans[i]
champsBannedList = []
for i in champsBanned5.keys():
    champsBannedList.append(champBans[i])


df = pd.DataFrame({"Total Bans": champsBannedList},
                  index=champsBanned5.keys())
ax = df.plot.bar()
ax.set_title("Total Champion Bans")
ax.get_legend().remove()
x_offset = -0.3
y_offset = 0.2
for p in ax.patches:
    b = p.get_bbox()
    val = "{:+.2f}".format(b.y1 + b.y0)
    ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)

plt.show()

expectedWinRateMinusActual = OrderedDict()
expectedWinsMinusActual = OrderedDict()

for i in champWinLoss:
    expectedWinsMinusActual[i] = champWinLoss[i][0] - champExpectedWins[i]

for i in champWinLoss:
    expectedWinRateMinusActual[i] = champWinRate[i] - champExpectedWins[i]/sum(champWinLoss[i])

teamPickEfficiency = OrderedDict()
for i in teams:
    teamPickEfficiency[i] = [0, 0]

for index, row in picks.iterrows():
    teamPickEfficiency[row["Team"]][0] += expectedWinRateMinusActual[row["Champion"]]
    teamPickEfficiency[row["Team"]][1] += 1

for i in teamPickEfficiency.keys():
    teamPickEfficiency[i] = 5*teamPickEfficiency[i][0]/teamPickEfficiency[i][1]

df = pd.DataFrame({"Teams Pick Efficiency": teamPickEfficiency},
                  index=teams)
ax = df.plot.bar(ylim=(-0.25, 0.25))
ax.set_title("Average Game Champion Pick Efficiency")
ax.get_legend().remove()
x_offset = -0.3
y_offset = 0.005
for p in ax.patches:
    b = p.get_bbox()
    val = "{:+.2f}".format(b.y1 + b.y0)
    if float(val) > 0:
        ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
    if float(val) < 0:
        ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 - 5*y_offset), fontsize=8)
plt.show()
print(sum(champAdjustedWinRateList)/len(expectedWinsMinusActual.keys()))

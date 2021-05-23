import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
import math as math

LSTop = {"Gangplank": "Z",
         "Chogath": "S",
         "Irelia": "S",
         "Karma": "S",
         "Lee Sin": "S",
         "Lulu": "S",
         "Rumble": "S",
         "Fiora": "A",
         "Camille": "A",
         "Kindred": "A",
         "Soraka": "A",
         "Akali": "B",
         "Dr Mundo": "B",
         "Jax": "B",
         "Jayce": "B",
         "Lucian": "B",
         "Malphite": "B",
         "Nocturne": "B",
         "Poppy": "B",
         "Riven": "B",
         "Sion": "B",
         "Vladimir": "B",
         "Zac": "B",
         "Zed": "B",
         "Aatrox": "C",
         "Darius": "C",
         "Gnar": "C",
         "Kalista": "C",
         "Illaoi": "C",
         "Ornn": "C",
         "Quinn": "C",
         "Sejuani": "C",
         "Ryze": "C",
         "Sett": "C",
         "Shen": "C",
         "Sylas": "C",
         "Trundle": "C",
         "Wukong": "C",
         "Urgot": "C",
         "Gragas": "DONT",
         "Kayle": "DONT",
         "Renekton": "DONT",
         "Mordekaiser": "DONT",
         "Kennen": "DONT",
         "Volibear": "DONT",
         }
LSJungle = {
    "Kindred": "Z",
    "Rumble": "Z",
    "Karthus": "S",
    "Fiddlesticks": "S",
    "Morgana": "S",
    "Lillia": "S",
    "Chogath": "A",
    "Ivern": "A",
    "Diana": "A",
    "Udyr": "A",
    "Lee Sin": "B",
    "Evelynn": "B",
    "Graves": "B",
    "Nocturne": "B",
    "Skarner": "B",
    "Zac": "B",
    "Xin Zhao": "B",
    "Rammus": "B",
    "Dr Mundo": "C",
    "Gragas": "C",
    "Ekko": "C",
    "Jarvan IV": "C",
    "Kayn": "C",
    "Poppy": "C",
    "Reksai": "C",
    "Trundle": "C",
    "Sejuani": "C",
    "Taliyah": "C",
    "Elise": "DONT",
    "Hecarim": "DONT",
    "Khazix": "DONT",
    "Nidalee": "DONT",
    "Olaf": "DONT",
    "Volibear": "DONT"
}
LSMid = {
    "Karma": "S",
    "Lulu": "S",
    "Orianna": "S",
    "Rumble": "S",
    "Seraphine": "S",
    "Zed": "S",
    "Chogath": "A",
    "Irelia": "A",
    "Lee Sin": "A",
    "Soraka": "A",
    "Tristana": "A",
    "Talon": "A",
    "Akali": "B",
    "Gangplank": "B",
    "Jayce": "B",
    "Kindred": "B",
    "Malzahar": "B",
    "Lucian": "B",
    "Nocturne": "B",
    "Qiyana": "B",
    "Sylas": "B",
    "Tryndamere": "B",
    "Viktor": "B",
    "Vladimir": "B",
    "Yone": "B",
    "Zilean": "B",
    "Annie": "C",
    "Anivia": "C",
    "Azir": "C",
    "Corki": "C",
    "Diana": "C",
    "Ekko": "C",
    "Galio": "C",
    "Leblanc": "C",
    "Renekton": "C",
    "Ryze": "C",
    "Sett": "C",
    "Syndra": "C",
    "Zoe": "C",
    "Twisted Fate": "C",
    "Kassadin": "C",
    "Ahri": "DONT",
    "Cassiopeia": "DONT"
}
LSBot = {
    "Kog Maw": "Z",
    "Varus": "Z",
    "Jinx": "S",
    "Soraka": "S",
    "Caitlyn": "A",
    "Ezreal": "A",
    "Miss Fortune": "A",
    "Karthus": "A",
    "Karma": "A",
    "Senna": "A",
    "Tristana": "A",
    "Seraphine": "A",
    "Kindred": "A",
    "Chogath": "A",
    "Ashe": "B",
    "Ziggs": "B",
    "Vayne": "B",
    "Vladimir": "B",
    "Draven": "C",
    "Kalista": "C",
    "Lucian": "C",
    "Samira": "C",
    "Twitch": "C",
    "Aphelios": "C",
    "Sivir": "C",
    "Kaisa": "DONT",
    "Xayah": "DONT",
    "Jhin": "DONT",
}
LSSupport = {
    "Karma": "Z",
    "Lulu": "Z",
    "Soraka": "S",
    "Seraphine": "S",
    "Blitzcrank": "A",
    "Taric": "A",
    "Morgana": "A",
    "Rakan": "A",
    "Rumble": "A",
    "Bard": "B",
    "Braum": "B",
    "Chogath": "B",
    "Galio": "B",
    "Leona": "B",
    "Thresh": "B",
    "Neeko": "B",
    "Xerath": "B",
    "Senna": "B",
    "Rell": "B",
    "Lux": "B",
    "Annie": "C",
    "Alistar": "C",
    "Janna": "C",
    "Nautilus": "C",
    "Tahm Kench": "C",
    "Maokai": "C",
    "Nami": "C",
    "Poppy": "C",
    "Pyke": "C",
    "Yuumi": "C",
    "Zilean": "C",
    "Brand": "C",
    "Sett": "DONT",
    "Shen": "DONT"
}



championsGroup = pd.read_csv("ChampionsPicked.csv")
championsRumble = pd.read_csv("ChampionsPickedRumbleStage.csv")
released = pd.read_csv("ChampionReleaseDate.csv")
teamExpected = pd.read_csv("TeamsWin%.csv")
frames = [championsGroup, championsRumble]
champions = pd.concat(frames)
expected = []
for index, row in champions.iterrows():
    x = teamExpected.loc[teamExpected["Team"] == row["Team"], "Percent"].iloc[0]
    y = teamExpected.loc[teamExpected["Team"] == row["TeamVS"], "Percent"].iloc[0]
    expected.append(x / (x + y))
champions["Expected"] = expected
picks = champions[champions["Pick/Ban"] == "Pick"]
bans = champions[(champions["Pick/Ban"] == "Ban") & (champions["Champion"] != "None")]
top = champions[champions["Role"] == "Top"]
jungle = champions[champions["Role"] == "Jungle"]
mid = champions[champions["Role"] == "Mid"]
adc = champions[champions["Role"] == "Adc"]
support = champions[champions["Role"] == "Support"]

uniqueChamps = sorted(champions.Champion.unique())

tiers = ["Z", "S", "A", "B", "C", "DONT", "Not in list"]

# find top win rates of all tiers in LS tier list
topWinLoss = OrderedDict()
for i in tiers:
    topWinLoss[i] = [0, 0]
for index, row in top.iterrows():
    try:
        if row["GameResult"] == "Win":
            topWinLoss[LSTop[row["Champion"]]][0] += 1
        else:
            topWinLoss[LSTop[row["Champion"]]][1] += 1
    except KeyError:
        LSTop[row["Champion"]] = "Not in list"
        if row["GameResult"] == "Win":
            topWinLoss[LSTop[row["Champion"]]][0] += 1
        else:
            topWinLoss[LSTop[row["Champion"]]][1] += 1

# find top win rates of all tiers in LS tier list
jungleWinLoss = OrderedDict()
for i in tiers:
    jungleWinLoss[i] = [0, 0]
for index, row in jungle.iterrows():
    try:
        if row["GameResult"] == "Win":
            jungleWinLoss[LSJungle[row["Champion"]]][0] += 1
        else:
            jungleWinLoss[LSJungle[row["Champion"]]][1] += 1
    except KeyError:
        LSJungle[row["Champion"]] = "Not in list"
        if row["GameResult"] == "Win":
            jungleWinLoss[LSJungle[row["Champion"]]][0] += 1
        else:
            jungleWinLoss[LSJungle[row["Champion"]]][1] += 1

# find top win rates of all tiers in LS tier list
midWinLoss = OrderedDict()
for i in tiers:
    midWinLoss[i] = [0, 0]
for index, row in mid.iterrows():
    try:
        if row["GameResult"] == "Win":
            midWinLoss[LSMid[row["Champion"]]][0] += 1
        else:
            midWinLoss[LSMid[row["Champion"]]][1] += 1
    except KeyError:
        LSMid[row["Champion"]] = "Not in list"
        if row["GameResult"] == "Win":
            midWinLoss[LSMid[row["Champion"]]][0] += 1
        else:
            midWinLoss[LSMid[row["Champion"]]][1] += 1

# find top win rates of all tiers in LS tier list
adcWinLoss = OrderedDict()
for i in tiers:
    adcWinLoss[i] = [0, 0]
for index, row in adc.iterrows():
    try:
        if row["GameResult"] == "Win":
            adcWinLoss[LSBot[row["Champion"]]][0] += 1
        else:
            adcWinLoss[LSBot[row["Champion"]]][1] += 1
    except KeyError:
        LSBot[row["Champion"]] = "Not in list"
        if row["GameResult"] == "Win":
            adcWinLoss[LSBot[row["Champion"]]][0] += 1
        else:
            adcWinLoss[LSBot[row["Champion"]]][1] += 1

# find top win rates of all tiers in LS tier list
supportWinLoss = OrderedDict()
for i in tiers:
    supportWinLoss[i] = [0, 0]
for index, row in support.iterrows():
    try:
        if row["GameResult"] == "Win":
            supportWinLoss[LSSupport[row["Champion"]]][0] += 1
        else:
            supportWinLoss[LSSupport[row["Champion"]]][1] += 1
    except KeyError:
        LSSupport[row["Champion"]] = "Not in list"
        if row["GameResult"] == "Win":
            supportWinLoss[LSSupport[row["Champion"]]][0] += 1
        else:
            supportWinLoss[LSSupport[row["Champion"]]][0] += 1


# find the total win loss of all tiers in LS tier list
totalWinLoss = OrderedDict()
for i in tiers:
    totalWinLoss[i] = [0, 0]

# find the top win ratio of all tiers
topWinRatio = OrderedDict()
for i in topWinLoss.keys():
    try:
        topWinRatio[i] = topWinLoss[i][0] / sum(topWinLoss[i])
    except ZeroDivisionError:
        topWinRatio[i] = topWinLoss[i][0] / (sum(topWinLoss[i]) + .00000000000001)
    totalWinLoss[i][0] += topWinLoss[i][0]
    totalWinLoss[i][1] += topWinLoss[i][1]

# find the jungle win ratio of all tiers
jungleWinRatio = OrderedDict()
for i in jungleWinLoss.keys():
    try:
        jungleWinRatio[i] = jungleWinLoss[i][0] / sum(jungleWinLoss[i])
    except ZeroDivisionError:
        jungleWinRatio[i] = jungleWinLoss[i][0] / (sum(jungleWinLoss[i]) + .00000000000001)
    totalWinLoss[i][0] += jungleWinLoss[i][0]
    totalWinLoss[i][1] += jungleWinLoss[i][1]

# find the mid win ratio of all tiers
midWinRatio = OrderedDict()
for i in midWinLoss.keys():
    try:
        midWinRatio[i] = midWinLoss[i][0] / sum(midWinLoss[i])
    except ZeroDivisionError:
        midWinRatio[i] = midWinLoss[i][0] / (sum(midWinLoss[i]) + .00000000000001)
    totalWinLoss[i][0] += midWinLoss[i][0]
    totalWinLoss[i][1] += midWinLoss[i][1]

# find the adc win ratio of all tiers
adcWinRatio = OrderedDict()
for i in adcWinLoss.keys():
    try:
        adcWinRatio[i] = adcWinLoss[i][0] / sum(adcWinLoss[i])
    except ZeroDivisionError:
        adcWinRatio[i] = adcWinLoss[i][0] / (sum(adcWinLoss[i]) + .00000000000001)
    totalWinLoss[i][0] += adcWinLoss[i][0]
    totalWinLoss[i][1] += adcWinLoss[i][1]

# find the support win ratio of all tiers
supportWinRatio = OrderedDict()
for i in supportWinLoss.keys():
    try:
        supportWinRatio[i] = supportWinLoss[i][0] / sum(supportWinLoss[i])
    except ZeroDivisionError:
        supportWinRatio[i] = supportWinLoss[i][0] / (sum(supportWinLoss[i]) + .00000000000001)
    totalWinLoss[i][0] += supportWinLoss[i][0]
    totalWinLoss[i][1] += supportWinLoss[i][1]

# find the total win ratio of all tiers
totalWinRatio = OrderedDict()
for i in totalWinLoss.keys():
    try:
        totalWinRatio[i] = totalWinLoss[i][0] / sum(totalWinLoss[i])
    except ZeroDivisionError:
        totalWinRatio[i] = totalWinLoss[i][0] / (sum(totalWinLoss[i]) + .00000000000001)

zTierList = [topWinRatio["Z"], jungleWinRatio["Z"], midWinRatio["Z"], adcWinRatio["Z"], supportWinRatio["Z"], totalWinRatio["Z"]]
sTierList = [topWinRatio["S"], jungleWinRatio["S"], midWinRatio["S"], adcWinRatio["S"], supportWinRatio["S"], totalWinRatio["S"]]
aTierList = [topWinRatio["A"], jungleWinRatio["A"], midWinRatio["A"], adcWinRatio["A"], supportWinRatio["A"], totalWinRatio["A"]]
bTierList = [topWinRatio["B"], jungleWinRatio["B"], midWinRatio["B"], adcWinRatio["B"], supportWinRatio["B"], totalWinRatio["B"]]
cTierList = [topWinRatio["C"], jungleWinRatio["C"], midWinRatio["C"], adcWinRatio["C"], supportWinRatio["C"], totalWinRatio["C"]]
dontTierList = [topWinRatio["DONT"], jungleWinRatio["DONT"], midWinRatio["DONT"], adcWinRatio["DONT"], supportWinRatio["DONT"], totalWinRatio["DONT"]]
naTierList = [topWinRatio["Not in list"], jungleWinRatio["Not in list"], midWinRatio["Not in list"], adcWinRatio["Not in list"], supportWinRatio["Not in list"], totalWinRatio["Not in list"]]

df = pd.DataFrame({
    "1. Z Tier": zTierList,
    "2. S Tier": sTierList,
    "3. A Tier": aTierList,
    "4. B Tier": bTierList,
    "5. C Tier": cTierList,
    "6. DONT Tier": dontTierList,
    "7. Not in list Tier": naTierList},
    index=["Top", "Jungle", "Mid", "Bot", "Support", "Total"]
)
ax = df.plot.bar()
ax.get_legend()
x_offset = -0.1
y_offset = 0.02
for p in ax.patches:
    b = p.get_bbox()
    val = "{:.2f}".format(b.y1 + b.y0)
    ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
plt.show()


# Plot top lane win rates
df = pd.DataFrame({
    "Top Win Rates": list(topWinRatio.values())},
    index=[tiers[x] + "\nPicks: " + str(sum(topWinLoss[tiers[x]])) for x in range(len(tiers))]
)
ax = df.plot.bar(title="Win Rates of each tier for top lane in LS and Nemesis Tier List")
ax.get_legend().remove()
x_offset = -0.05
y_offset = 0.01
for p in ax.patches:
    b = p.get_bbox()
    val = "{:.2f}".format(b.y1 + b.y0)
    ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
plt.show()

# Plot jungle lane win rates
df = pd.DataFrame({
    "Jungle Win Rates": list(jungleWinRatio.values())},
    index=[tiers[x] + "\nPicks: " + str(sum(jungleWinLoss[tiers[x]])) for x in range(len(tiers))]
)
ax = df.plot.bar(title="Win Rates of each tier for jungle in LS and Nemesis Tier List")
ax.get_legend().remove()
x_offset = -0.05
y_offset = 0.01
for p in ax.patches:
    b = p.get_bbox()
    val = "{:.2f}".format(b.y1 + b.y0)
    ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
plt.show()

# Plot mid lane win rates
df = pd.DataFrame({
    "Mid Win Rates": list(midWinRatio.values())},
    index=[tiers[x] + "\nPicks: " + str(sum(midWinLoss[tiers[x]])) for x in range(len(tiers))]
)
ax = df.plot.bar(title="Win Rates of each tier for mid lane in LS and Nemesis Tier List")
ax.get_legend().remove()
x_offset = -0.05
y_offset = 0.01
for p in ax.patches:
    b = p.get_bbox()
    val = "{:.2f}".format(b.y1 + b.y0)
    ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
plt.show()

# Plot bot lane win rates
df = pd.DataFrame({
    "Jungle Win Rates": list(adcWinRatio.values())},
    index=[tiers[x] + "\nPicks: " + str(sum(adcWinLoss[tiers[x]])) for x in range(len(tiers))]
)
ax = df.plot.bar(title="Win Rates of each tier for bot lane in LS and Nemesis Tier List")
ax.get_legend().remove()
x_offset = -0.05
y_offset = 0.01
for p in ax.patches:
    b = p.get_bbox()
    val = "{:.2f}".format(b.y1 + b.y0)
    ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
plt.show()

# Plot support lane win rates
df = pd.DataFrame({
    "Jungle Win Rates": list(supportWinRatio.values())},
    index=[tiers[x] + "\nPicks: " + str(sum(supportWinLoss[tiers[x]])) for x in range(len(tiers))]
)
ax = df.plot.bar(title="Win Rates of each tier for support in LS and Nemesis Tier List")
ax.get_legend().remove()
x_offset = -0.05
y_offset = 0.01
for p in ax.patches:
    b = p.get_bbox()
    val = "{:.2f}".format(b.y1 + b.y0)
    ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
plt.show()

# Plot total win rates
df = pd.DataFrame({
    "Jungle Win Rates": list(totalWinRatio.values())},
    index=[tiers[x] + "\nPicks: " + str(sum(totalWinLoss[tiers[x]])) for x in range(len(tiers))]
)
ax = df.plot.bar(title="Win Rates of each tier in total for LS and Nemesis Tier List")
ax.get_legend().remove()
x_offset = -0.05
y_offset = 0.01
for p in ax.patches:
    b = p.get_bbox()
    val = "{:.2f}".format(b.y1 + b.y0)
    ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
plt.show()

CI = OrderedDict()
for i in totalWinLoss.keys():
    CI[i] = 1.96*math.sqrt(0.5*0.5/sum(totalWinLoss[i]))

CIList = []
for i in CI.keys():
    CIList.append(CI[i])

# Plot total win rates with confidence intervals
df = pd.DataFrame({
    "Jungle Win Rates": list(totalWinRatio.values())},
    index=[tiers[x] + "\nPicks: " + str(sum(totalWinLoss[tiers[x]])) for x in range(len(tiers))]
)
ax = df.plot.bar(yerr=CIList, ylim=(0, 1.0))
ax.set_title("Win Rates of each tier in total for LS and Nemesis Tier List with confidence interval")
ax.get_legend().remove()
x_offset = -0.05
y_offset = 0.01
for p in ax.patches:
    b = p.get_bbox()
    val = "{:.2f}".format(b.y1 + b.y0)
    ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
plt.axhline(y=0.5, color='r', linestyle='-')
plt.show()

# for i in LSTop.keys():
#     if LSTop[i] == "Not in list":
#         print(i)
# for i in LSJungle.keys():
#     if LSJungle[i] == "Not in list":
#         print(i)
# for i in LSMid.keys():
#     if LSMid[i] == "Not in list":
#         print(i)
# for i in LSBot.keys():
#     if LSBot[i] == "Not in list":
#         print(i)
# for i in LSSupport.keys():
#     if LSSupport[i] == "Not in list":
#         print(i)

topTierExpectedWins = OrderedDict()
jungleTierExpectedWins = OrderedDict()
midTierExpectedWins = OrderedDict()
adcTierExpectedWins = OrderedDict()
supportTierExpectedWins = OrderedDict()
totalTierExpectedWins = OrderedDict()
topTierExpectedWinsPercent = OrderedDict()
jungleTierExpectedWinsPercent = OrderedDict()
midTierExpectedWinsPercent = OrderedDict()
adcTierExpectedWinsPercent = OrderedDict()
supportTierExpectedWinsPercent = OrderedDict()
totalTierExpectedWinsPercent = OrderedDict()
topTierBlinds = OrderedDict()
jungleTierBlinds = OrderedDict()
midTierBlinds = OrderedDict()
adcTierBlinds = OrderedDict()
supportTierBlinds = OrderedDict()
totalTierBlinds = OrderedDict()
topTierBlindsPercent = OrderedDict()
jungleTierBlindsPercent = OrderedDict()
midTierBlindsPercent = OrderedDict()
adcTierBlindsPercent = OrderedDict()
supportTierBlindsPercent = OrderedDict()
totalTierBlindsPercent = OrderedDict()

for tier in tiers:
    topTierExpectedWins[tier] = 0
    jungleTierExpectedWins[tier] = 0
    midTierExpectedWins[tier] = 0
    adcTierExpectedWins[tier] = 0
    supportTierExpectedWins[tier] = 0
    topTierBlinds[tier] = 0
    jungleTierBlinds[tier] = 0
    midTierBlinds[tier] = 0
    adcTierBlinds[tier] = 0
    supportTierBlinds[tier] = 0
    topTierBlindsPercent[tier] = 0
    jungleTierBlindsPercent[tier] = 0
    midTierBlindsPercent[tier] = 0
    adcTierBlindsPercent[tier] = 0
    supportTierBlindsPercent[tier] = 0
for index, row in top.iterrows():
    topTierExpectedWins[LSTop[row["Champion"]]] += row["Expected"]
    if row["Blind?"] == "B":
        topTierBlinds[LSTop[row["Champion"]]] += 1

for index, row in jungle.iterrows():
    jungleTierExpectedWins[LSJungle[row["Champion"]]] += row["Expected"]
    if row["Blind?"] == "B":
        jungleTierBlinds[LSJungle[row["Champion"]]] += 1

for index, row in mid.iterrows():
    midTierExpectedWins[LSMid[row["Champion"]]] += row["Expected"]
    if row["Blind?"] == "B":
        midTierBlinds[LSMid[row["Champion"]]] += 1

for index, row in adc.iterrows():
    adcTierExpectedWins[LSBot[row["Champion"]]] += row["Expected"]
    if row["Blind?"] == "B":
        adcTierBlinds[LSBot[row["Champion"]]] += 1

for index, row in support.iterrows():
    supportTierExpectedWins[LSSupport[row["Champion"]]] += row["Expected"]
    if row["Blind?"] == "B":
        supportTierBlinds[LSSupport[row["Champion"]]] += 1

for tier in tiers:
    topTierBlindsPercent[tier] = round(topTierBlinds[tier]/(sum(topWinLoss[tier]) + 0.0000001), 5)
    jungleTierBlindsPercent[tier] = round(jungleTierBlinds[tier]/(sum(jungleWinLoss[tier]) + 0.0000001), 5)
    midTierBlindsPercent[tier] = round(midTierBlinds[tier]/(sum(midWinLoss[tier]) + 0.00000001), 5)
    adcTierBlindsPercent[tier] = round(adcTierBlinds[tier]/(sum(adcWinLoss[tier]) + 0.0000001), 5)
    supportTierBlindsPercent[tier] = round(supportTierBlinds[tier]/(sum(supportWinLoss[tier]) + 0.000001), 5)
    topTierExpectedWinsPercent[tier] = round(topTierExpectedWins[tier]/(sum(topWinLoss[tier]) + 0.000001), 5)
    jungleTierExpectedWinsPercent[tier] = round(jungleTierExpectedWins[tier]/(sum(jungleWinLoss[tier]) + 0.000001), 5)
    midTierExpectedWinsPercent[tier] = round(midTierExpectedWins[tier]/(sum(midWinLoss[tier]) + 0.0000001), 5)
    adcTierExpectedWinsPercent[tier] = round(adcTierExpectedWins[tier]/(sum(adcWinLoss[tier]) + 0.0000001), 5)
    supportTierExpectedWinsPercent[tier] = round(supportTierExpectedWins[tier]/(sum(supportWinLoss[tier]) + 0.000001), 5)
    totalTierBlinds[tier] = topTierBlinds[tier] + jungleTierBlinds[tier] + midTierBlinds[tier] + adcTierBlinds[tier] + supportTierBlinds[tier]
    totalTierBlindsPercent[tier] = totalTierBlinds[tier] / sum(totalWinLoss[tier])
    totalTierExpectedWins[tier] = topTierExpectedWins[tier] + jungleTierExpectedWins[tier] + midTierExpectedWins[tier] + adcTierExpectedWins[tier] + supportTierExpectedWins[tier]
    totalTierExpectedWinsPercent[tier] = totalTierExpectedWins[tier]/sum(totalWinLoss[tier])

totalActualMinusExpected = OrderedDict()
for tier in tiers:
    totalActualMinusExpected[tier] = totalWinRatio[tier] - totalTierExpectedWinsPercent[tier]


df = pd.DataFrame({"Win Rate - Expected Win Rate": list(totalActualMinusExpected.values())},
                  index=tiers)
ax = df.plot.bar(yerr=CIList)
ax.set_title("Win Rate - Expected Win Rate")
ax.get_legend().remove()
x_offset = -0.3
y_offset = 0.005
for p in ax.patches:
    b = p.get_bbox()
    val = "{:+.2f}".format(b.y1 + b.y0)
    if float(val) > 0:
        ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=8)
    if float(val) < 0:
        ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 - y_offset), fontsize=8)
plt.axhline(y=0, color='r', linestyle='-')
plt.show()

mostPlayedRole = OrderedDict()
for champion in uniqueChamps:
    mostPlayedRole[champion] = [0, 0, 0, 0, 0]
for index, row in picks.iterrows():
    if row["Role"] == "Top":
        mostPlayedRole[row["Champion"]][0] += 1
    elif row["Role"] == "Jungle":
        mostPlayedRole[row["Champion"]][1] += 1
    elif row["Role"] == "Mid":
        mostPlayedRole[row["Champion"]][2] += 1
    elif row["Role"] == "Adc":
        mostPlayedRole[row["Champion"]][3] += 1
    elif row["Role"] == "Support":
        mostPlayedRole[row["Champion"]][4] += 1

for champion in mostPlayedRole.keys():
    max_value = max(mostPlayedRole[champion])
    max_index = mostPlayedRole[champion].index(max_value)
    if max_value == 0:
        if champion in LSTop.keys():
            mostPlayedRole[champion] = "Top"
        elif champion in LSJungle.keys():
            mostPlayedRole[champion] = "Jungle"
        elif champion in LSMid.keys():
            mostPlayedRole[champion] = "Mid"
        elif champion in LSBot.keys():
            mostPlayedRole[champion] = "Adc"
        elif champion in LSSupport.keys():
            mostPlayedRole[champion] = "Support"
        else:
            mostPlayedRole[champion] = "Not in list"
    elif max_index == 0:
        mostPlayedRole[champion] = "Top"
    elif max_index == 1:
        mostPlayedRole[champion] = "Jungle"
    elif max_index == 2:
        mostPlayedRole[champion] = "Mid"
    elif max_index == 3:
        mostPlayedRole[champion] = "Adc"
    elif max_index == 4:
        mostPlayedRole[champion] = "Support"

count = 0
bansPerTier = OrderedDict()
for tier in tiers:
    bansPerTier[tier] = 0
for index, row in bans.iterrows():
    count += 1
    champion = row["Champion"]
    role = mostPlayedRole[champion]
    try:
        if role == "Top":
            bansPerTier[LSTop[champion]] += 1
        if role == "Jungle":
            bansPerTier[LSJungle[champion]] += 1
        if role == "Mid":
            bansPerTier[LSMid[champion]] += 1
        if role == "Adc":
            bansPerTier[LSBot[champion]] += 1
        if role == "Support":
            bansPerTier[LSSupport[champion]] += 1
        if role == "Not in list":
            bansPerTier["Not in list"] += 1
    except KeyError:
        bansPerTier["Not in list"] += 1


for tier in tiers:
    print(tier, "\t",
          round(totalWinRatio[tier], 3), "\t",
          round(totalTierExpectedWinsPercent[tier], 3), "\t",
          round(totalActualMinusExpected[tier], 3), "\t",
          sum(totalWinLoss[tier]), "\t",
          bansPerTier[tier], "\t",
          round(totalTierBlindsPercent[tier], 3))

count = 0
for index, row in picks.iterrows():
    count += row["Expected"]

print(count/5)

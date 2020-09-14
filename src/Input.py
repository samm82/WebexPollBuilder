from datetime import datetime
from sys import exit
from os.path import isdir, isfile, splitext

from GUI import inFileNotSelected, invalidInFile, invalidOutDir, \
    invalidTime, outDirNotSelected, timeNotSelected, webexPollBuilderGUI


def genTimeList():
    t = ["0:30", "0:45"]
    mins = ["00", "15", "30", "45"]
    TIME_MAX = 5
    for i in range(1, TIME_MAX):
        t = t + list(map(lambda x: ":".join([str(i), x]), mins))
    t.append(str(TIME_MAX) + ":00")
    return t


def gui():
    timeList = genTimeList()
    while True:
        event, values = webexPollBuilderGUI(timeList)
        if event == "OK":
            if not values[0]:
                timeNotSelected()
            elif values[0] not in timeList:
                invalidTime(values[0])
            elif not values[1]:
                inFileNotSelected()
            elif not isfile(values[1]) or splitext(values[1])[1] != ".txt":
                invalidInFile(values[1])
            elif not values[2]:
                outDirNotSelected()
            elif not isdir(values[2]):
                invalidOutDir(values[2])
            else:
                if not values[3]:
                    values[3] = datetime.now().strftime("%m%d%Y")
                # can't use tuple unpacking or the like; type(values) == dict
                return values[0], values[1], values[2], values[3]
        else:
            exit()


# Also removes trailing whitespace; is this the best place to do it?
def readData(path):
    with open(path, encoding='utf-8') as f:
        data = f.readlines()
    while data[-1] == "\n":
        del data[-1]
    return data

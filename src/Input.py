from datetime import datetime
from sys import exit
from os.path import isdir, isfile, splitext
from pathvalidate import is_valid_filename

from GUI import inFileNotSelected, invalidInFile, invalidOutDir, \
    invalidOutFilename, invalidTime, outDirNotSelected, timeNotSelected, \
    webexPollBuilderGUI


def genTimeList():
    t = ["0:30", "0:45"]
    mins = ["00", "15", "30", "45"]
    TIME_MAX = 5
    for i in range(1, TIME_MAX):
        t = t + list(map(lambda x: ":".join([str(i), x]), mins))
    t.append(str(TIME_MAX) + ":00")
    return t


def validFileName(name):
    if name in ('CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4',
                'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2',
                'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'):
        return False

    return is_valid_filename(name)


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
                fileName = values[3]
                if not fileName:
                    fileName = datetime.now().strftime("%m%d%Y")
                elif not validFileName(fileName):
                    invalidOutFilename(fileName)
                    continue
                # can't use tuple unpacking or the like; type(values) == dict
                return values[0], values[1], values[2], fileName
        else:
            exit()


# Also removes trailing whitespace; is this the best place to do it?
def readData(path):
    with open(path, encoding='utf-8') as f:
        data = f.readlines()
    while data[-1] == "\n":
        del data[-1]
    return data

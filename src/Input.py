from datetime import datetime
from sys import exit
from os.path import isdir, isfile, splitext

import PySimpleGUI as sg


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
        event, values = sg.Window("Webex Poll Builder").Layout(
            [[sg.Text("How long should the question last for?"),
              sg.Combo(timeList)],
             [sg.Text("Select the file with the question and answers.")],
             [sg.In(), sg.FileBrowse()],
             [sg.Text("Select the directory to save output file to.")],
             [sg.In(), sg.FolderBrowse()],
             [sg.Text("Enter filename. (Default is date)")],
             [sg.In()],
             [sg.CloseButton("OK"), sg.CloseButton("Cancel")]]
        ).Read()

        if event == "OK":
            if not values[0]:
                sg.popup(
                    "Please select a time from the drop-down menu.",
                    title="Time Not Selected"
                )

            elif values[0] not in timeList:
                sg.popup(
                    "Invalid time: " + str(values[0]),
                    "Please select a time from the drop-down menu.",
                    title="Invalid Time"
                )

            elif not values[1]:
                sg.popup(
                    "Please select a valid input (.txt) file.",
                    title="Input File Not Selected"
                )

            elif not isfile(values[1]) or splitext(values[1])[1] != ".txt":
                sg.popup(
                    "Invalid input file: {0}.".format(values[1]),
                    "Please select a valid input (.txt) file.",
                    title="Invalid Input File"
                )

            elif not values[2]:
                sg.popup(
                    "Please select a valid output directory.",
                    title="Output Directory Not Selected"
                )

            elif not isdir(values[2]):
                sg.popup(
                    "Invalid Output Directory: {0}.".format(values[2]),
                    "Please select a valid output directory.",
                    title="Invalid Output Directory"
                )

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

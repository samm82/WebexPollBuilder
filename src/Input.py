from datetime import datetime

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

        if event in ["Cancel", sg.WIN_CLOSED]:
            exit()
        elif event == "OK":
            if values[0] in timeList:
                if not values[3]:
                    values[3] = datetime.now().strftime("%m%d%Y")
                # can't use tuple unpacking or the like; type(values) == dict
                return values[0], values[1], values[2], values[3]
            else:
                event, values = sg.popup(
                    "Invalid time: {0}.".format(values[0]),
                    "Please select a time from the drop-down menu."
                )
                if event == sg.WIN_CLOSED:
                    exit()
        else:
            raise ValueError("Invalid event value.")


def readData(path):
    with open(path, encoding='utf-8') as f:
        # as to not return with a file left open
        data = f.readlines()
    return data

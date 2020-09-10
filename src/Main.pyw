from datetime import datetime
from os.path import isfile, join

import PySimpleGUI as sg

def formatString(s):
    return s.strip().replace(" ", "&nbsp;")

def formatAnswers(l):
    answers = []
    for a in l:
        if a:
            a = a.split(" ", 1)
            a[1] = formatString(a[1])
            answers.append(a)
        else:
            ValueError("Unexpected blank line")

    formattedAnswers = []
    trueCount = 0
    for a in answers:
        if a[0].upper() == 'T':
            correct = "true"
            trueCount += 1
        elif a[0].upper() == 'F':
            correct = "false"
        else:
            raise ValueError("Invalid input; expected 'T' or 'F', got", a[0])

        formattedAnswers.append('<ANSWER ISCORRECT="{0}">{1}</ANSWER>\n'.format(correct, a[1]))

    if trueCount == 1:
        qType = "mcone"
    elif trueCount > 1:
        qType = "mcmany"
    elif trueCount == 0:
        raise ValueError("There must be at least one correct answer.")
    else:
        raise ValueError("Invalid number of correct questions; check that there is at least one.")

    return formattedAnswers, qType


def main():
    programName = "Webex Poll Builder"
    # make time list
    timeList = ["0:30", "0:45"]
    for i in range(1, 5):
        timeList = timeList + list(map(lambda x : ":".join([str(i), x]), ["00", "15", "30", "45"]))
    timeList.append("5:00")

    # build GUI
    event, values = sg.Window(programName).Layout(
        [[sg.Text("How long should the question last for?"), sg.Combo(timeList)],
        [sg.Text("Select the file with the question and answers.")],
        [sg.In(), sg.FileBrowse()],
        [sg.Text("Select the directory to save output file to.")],
        [sg.In(), sg.FolderBrowse()],
        [sg.Text("Enter filename. (Default is date)")],
        [sg.In()],
        [sg.CloseButton("OK"), sg.CloseButton("Cancel")]]
        ).Read()

    if event == "Cancel":
        exit()
    elif event == "OK":
        time, filepath = values[0], values[1]

        f = open(filepath, "r")
        lines = f.readlines()
        f.close()

        if not lines[0]:
            raise ValueError("Expected title in file.")
        else:
            title = formatString(lines[0])

        if len(lines) != 1:
            if lines[1] != "\n":
                raise ValueError("Expected blank second line in file.")
            answers, q = formatAnswers(lines[2:])
        else:
            answers, q = [], "text"

        output = ['<?xml version="1.0" encoding="UTF-16"?>\n', \
                  '<POLL TYPE="named" SHOWTIMER="yes" ALARM="{0}" NOANSWER="yes" SHOWRESPONSE="yes">\n\n'.format(time), \
                  '<QUESTION TYPE="{0}" TITLE="{1}">\n'.format(q, title)] + answers + ['</QUESTION>\n\n</POLL>']

        if values[3]:
            outFilepath = join(values[2], values[3])
        else:
            outFilepath = join(values[2], datetime.now().strftime("%m%d%Y"))

        saved, i = 0, 1
        while saved < 1:
            out = outFilepath + "-" + str(i) + ".atp"
            if isfile(out):
                i += 1
            else:
                f = open(out, "w")
                f.writelines(output)
                f.close()
                saved += 1

    else:
        raise ValueError("Invalid event value.")

if __name__ == "__main__":
    main()
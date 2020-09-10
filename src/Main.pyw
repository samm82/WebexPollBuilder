import codecs
from datetime import datetime
from os.path import isfile, join

import PySimpleGUI as sg

def genTimeList():
    t = ["0:30", "0:45"]
    for i in range(1, 5):
        t = t + list(map(lambda x : ":".join([str(i), x]), ["00", "15", "30", "45"]))
    t.append("5:00")
    return t

def formatString(s):
    return s.strip().replace(" ", "&nbsp;")

def formatAnswers(l):
    answers, trueCount = [], 0
    for i in range(len(l)):
        if l[i] and l[i] != "\n":
            a = l[i].split(" ", 1)

            if a[0].upper() == 'T':
                correct = "true"
                trueCount += 1
            elif a[0].upper() == 'F':
                correct = "false"
            else:
                raise ValueError("Invalid input; expected 'T' or 'F', got", a[0])

            answers.append('<ANSWER ISCORRECT="{0}">{1}</ANSWER>\n'.format(correct, formatString(a[1])))

        else:
            break        

    if trueCount == 1:
        qType = "mcone"
    elif trueCount > 1:
        qType = "mcmany"
    elif trueCount == 0:
        raise ValueError("There must be at least one correct answer.")
    else:
        raise ValueError("Invalid number of correct questions; check that there is at least one.")

    return answers, qType, i

def getQuestion(l):
    if not l[0]:
        raise ValueError("Expected title in file.")
    else:
        if len(l) == 1 or l[2][0:2].upper() not in ["T ", "F "]:
            return [formatString(l[0])], "text", 2
        else:
            if l[1] != "\n":
                raise ValueError("Expected blank line; check that the input file is formatted correctly.")

            answers, qType, i = formatAnswers(l[2:])
            return [formatString(l[0])] + answers, qType, i + 3

def main():
    # GUI
    event, values = sg.Window("Webex Poll Builder").Layout(
        [[sg.Text("How long should the question last for?"), sg.Combo(genTimeList())],
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
        time, filepath, outDir = values[0], values[1], values[2]
        if values[3]:
            filename = values[3]
        else:
            filename = datetime.now().strftime("%m%d%Y")

        with open(filepath, encoding='utf-8') as f:
            lines = f.readlines()

        while lines:
            question, qType, startLine = getQuestion(lines)

            output = ['<?xml version="1.0" encoding="UTF-16"?>\n', \
                      '<POLL TYPE="named" SHOWTIMER="yes" ALARM="{0}" NOANSWER="yes" SHOWRESPONSE="yes">\n\n'.format(time), \
                      '<QUESTION TYPE="{0}" TITLE="{1}">\n'.format(qType, question[0])] + question[1:] + ['</QUESTION>\n\n</POLL>']

            outFilepath = join(outDir, filename)

            i = 1
            while True:
                out = outFilepath + "-" + str(i) + ".atp"
                if isfile(out):
                    i += 1
                else:
                    f = open(out, "w")
                    f.writelines(output)
                    f.close()
                    break

            lines = lines[startLine:]

    else:
        raise ValueError("Invalid event value.")

if __name__ == "__main__":
    main()
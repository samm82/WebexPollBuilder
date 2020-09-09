import PySimpleGUI as sg

def formatString(s):
    return s.strip().replace(" ", "&nbsp;")

def main():
    # make time list
    timeList = ["0:30", "0:45"]
    for i in range(1, 5):
        timeList = timeList + list(map(lambda x : ":".join([str(i), x]), ["00", "15", "30", "45"]))
    timeList.append("5:00")

    # build GUI
    event, values = sg.Window("Dad Webex").Layout(
        [[sg.Text("How long should the question last for?"), sg.Combo(timeList)],
        [sg.Text("Select the file with the question and answers.")],
        [sg.In(), sg.FileBrowse()],
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
        if lines[1] != "\n":
            raise ValueError("Expected blank second line in file.")
        answers = []
        for i in lines[2:]:
            if i:
                answers.append(formatString(i))
            else:
                ValueError("Unexpected blank line")

        output = ['<?xml version="1.0" encoding="UTF-16"?>\n', \
                  '<POLL TYPE="named" SHOWTIMER="yes" ALARM="{0}" NOANSWER="yes" SHOWRESPONSE="yes">\n\n'.format(time), \
                  '<QUESTION TYPE="mcmany" TITLE="{0}">\n'.format(title)]

        for i in answers:
            output.append('<ANSWER ISCORRECT="false">{0}</ANSWER>\n'.format(i))

        output.append('</QUESTION>\n\n</POLL>')

        # Save output file
        event, values = sg.Window("Dad Webex").Layout(
            [[sg.Text("Choose output destination file.")],
            [sg.In(), sg.FileSaveAs(key='save', file_types=(("ATP", "*.atp"), ("Plain Text", "*.txt"),))],
            [sg.CloseButton("OK"), sg.CloseButton("Cancel")]]
            ).Read()

        if event == "Cancel":
            exit()
        elif event == "OK":
            save = values['save']

            # add file extension if not already
            if not save.endswith(".txt") and not save.endswith(".atp"):
                save = save + ".atp"

            f = open(save, "w")
            f.writelines(output)
            f.close()

        else:
            raise ValueError("Invalid event value.")

    else:
        raise ValueError("Invalid event value.")

if __name__ == "__main__":
    main()
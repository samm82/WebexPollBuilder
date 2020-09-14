import PySimpleGUI as sg


def webexPollBuilderGUI(t):
    return sg.Window("Webex Poll Builder").Layout(
        [[sg.Text("How long should the question last for?"),
          sg.Combo(t)],
         [sg.Text("Select the file with the question and answers.")],
         [sg.In(), sg.FileBrowse()],
         [sg.Text("Select the directory to save output file to.")],
         [sg.In(), sg.FolderBrowse()],
         [sg.Text("Enter filename. (Default is date)")],
         [sg.In()],
         [sg.CloseButton("OK"), sg.CloseButton("Cancel")]]
    ).Read()


def timeNotSelected():
    sg.popup("Please select a time from the drop-down menu.",
             title="Time Not Selected")


def invalidTime(t):
    sg.popup("Invalid time: " + str(t),
             "Please select a time from the drop-down menu.",
             title="Invalid Time")


def inFileNotSelected():
    sg.popup("Please select a valid input (.txt) file.",
             title="Input File Not Selected")


def invalidInFile(f):
    sg.popup("Invalid input file: {0}".format(f),
             "Please select a valid input (.txt) file.",
             title="Invalid Input File")


def outDirNotSelected():
    sg.popup("Please select a valid output directory.",
             title="Output Directory Not Selected")


def invalidOutDir(d):
    sg.popup("Invalid Output Directory: {0}".format(d),
             "Please select a valid output directory.",
             title="Invalid Output Directory")


def invalidOutFilename(f):
    sg.popup("Invalid Output Filename: {0}".format(f),
             "Please enter a valid file name (or leave the field blank).",
             title="Invalid Output Filename")


def noCorrectAnswer():
    sg.popup("There must be at least one correct answer.",
             title="No Correct Answer(s)")


def invalidFileFormat(e, g):
    sg.popup("".join(["Expected ", e, ", got ", g, "."]),
             title="Invalid File Format")


def invalidAnswerFormat(s):
    invalidFileFormat("'T' or 'F' at beginning of answer", "'" + s + "'")


def noQuestion():
    invalidFileFormat("question", "a blank line")


def noBlankLineAfterQuestion(s):
    invalidFileFormat("a blank line after question", "'" + s + "'")

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
    return sg.popup("Please select a time from the drop-down menu.",
                    title="Time Not Selected"
                    )


def invalidTime(t):
    return sg.popup("Invalid time: " + str(t),
                    "Please select a time from the drop-down menu.",
                    title="Invalid Time"
                    )


def inFileNotSelected():
    return sg.popup("Please select a valid input (.txt) file.",
                    title="Input File Not Selected"
                    )


def invalidInFile(f):
    return sg.popup("Invalid input file: {0}".format(f),
                    "Please select a valid input (.txt) file.",
                    title="Invalid Input File"
                    )


def outDirNotSelected():
    return sg.popup("Please select a valid output directory.",
                    title="Output Directory Not Selected"
                    )


def invalidOutDir(d):
    return sg.popup("Invalid Output Directory: {0}".format(d),
                    "Please select a valid output directory.",
                    title="Invalid Output Directory"
                    )

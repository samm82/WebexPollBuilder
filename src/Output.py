from os.path import isfile

import PySimpleGUI as sg


def saveToFile(path, data):
    i = 1
    while True:
        file = path + "{0}.atp".format(i)
        if isfile(file):
            i += 1
        else:
            f = open(file, "w")
            f.writelines(data)
            f.close()
            return


def success(n, d):
    if n == 0:
        sg.popup("No files were written.")
        return
    elif n == 1:
        output = "Successfully wrote 1 file to the following directory: \n{0}.".format(d) # noqa E501
    else:
        output = "Successfully wrote {0} files to the following directory: \n{1}.".format(n, d) # noqa E501
    sg.popup(output, title="Success")

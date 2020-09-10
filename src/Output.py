from os.path import isfile

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

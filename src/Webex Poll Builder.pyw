from Input import gui, readData
from Process import processQuestion
from Output import saveToFile


def buildPolls(lines, t, p):
    while lines:
        output, start = processQuestion(lines, t)
        saveToFile(p, output)
        lines = lines[start:]


def main():
    time, inFilePath, outFilePath = gui()
    lines = readData(inFilePath)
    buildPolls(lines, time, outFilePath)


if __name__ == "__main__":
    main()

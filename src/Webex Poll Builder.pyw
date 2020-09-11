from os.path import join

from Input import gui, readData
from Process import processQuestion
from Output import saveToFile


def main():
    time, inFilePath, outDir, fileName = gui()
    lines = readData(inFilePath)

    while lines:
        output, startLine = processQuestion(lines, time)
        outFilePath = join(outDir, fileName) + "-"
        saveToFile(outFilePath, output)
        lines = lines[startLine:]


if __name__ == "__main__":
    main()

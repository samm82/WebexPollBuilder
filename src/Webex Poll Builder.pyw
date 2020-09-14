from os.path import join

from Input import gui, readData
from Process import processQuestion
from Output import saveToFile, success


def buildPolls(lines, t, d, f):
    p = join(d, f) + "-"
    fileCount = 0
    while lines:
        output, start = processQuestion(lines, t)
        if output is None:
            return fileCount
        saveToFile(p, output)
        lines = lines[start:]
        fileCount += 1

    return fileCount


def main():
    time, inFilePath, outDir, fileName = gui()
    lines = readData(inFilePath)
    count = buildPolls(lines, time, outDir, fileName)
    success(count, outDir)


if __name__ == "__main__":
    main()

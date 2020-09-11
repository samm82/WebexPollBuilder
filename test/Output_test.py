from os import curdir, path, remove
import sys

sys.path.append(path.abspath("src"))

from Output import saveToFile


class TestSaveToFile:
    outDir = path.join(curdir, "test", "output")
    stableDir = path.join(curdir, "test", "stable")

    def test_file_contents_correct(self):
        data = ['<?xml version="1.0" encoding="UTF-16"?>\n',
                '<POLL TYPE="named" SHOWTIMER="yes" ALARM="1:45"' +
                ' NOANSWER="yes" SHOWRESPONSE="yes">\n',
                '\n', '<QUESTION TYPE="mcmany"' +
                ' TITLE="Will&nbsp;this&nbsp;code&nbsp;work?">\n',
                '<ANSWER ISCORRECT="true">Yes</ANSWER>\n',
                '<ANSWER ISCORRECT="false">No</ANSWER>\n',
                '<ANSWER ISCORRECT="true">Hopefully</ANSWER>\n',
                '<ANSWER ISCORRECT="false">Who&nbsp;knows?</ANSWER>\n',
                '</QUESTION>\n', '\n', '</POLL>']

        saveToFile(path.join(self.outDir, "oneMCManyOut-"), data)

        fileName = "oneMCManyOut-1.atp"
        outPath = path.join(self.outDir, fileName)

        assert path.isfile(outPath)

        with open(path.join(outPath)) as f:
            out = f.readlines()
        with open(path.join(self.stableDir, fileName)) as f:
            stableOut = f.readlines()

        assert out == stableOut

        # clean up
        remove(path.join(outPath))

    def test_numbering(self):
        data = ["\n"]
        pathPreface = path.join(self.outDir, "fileExists-")

        for i in [1, 4, 6]:
            saveToFile(pathPreface, data)
            assert path.isfile(pathPreface + str(i) + ".atp")

        for i in [1, 4, 6]:
            remove(pathPreface + str(i) + ".atp")

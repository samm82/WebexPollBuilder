from os import curdir, path, remove
import sys

sys.path.append(path.abspath("src"))

main = __import__("Webex Poll Builder")


class TestBuildPolls:
    inputDir = path.join(curdir, "test", "input")
    outDir = path.join(curdir, "test", "output")
    stableDir = path.join(curdir, "test", "stable")

    def test_multiple_questions(self):
        with open(path.join(self.inputDir, "multVarious.txt")) as f:
            data = f.readlines()

        main.buildPolls(data, "1:45", self.outDir, "multVariousOut")

        for i in range(1, 6):
            filename = "multVariousOut-{0}.atp".format(i)
            outPath = path.join(self.outDir, filename)

            with open(outPath) as f:
                out = f.readlines()
            with open(path.join(self.stableDir, filename)) as f:
                stableOut = f.readlines()

            assert out == stableOut

            remove(outPath)

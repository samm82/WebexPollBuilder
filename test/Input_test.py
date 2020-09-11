from os import curdir, path
import sys

sys.path.append(path.abspath("src"))

from Input import genTimeList, readData


class TestGenTimeList:
    def test_correct_time_list(self):
        assert genTimeList() == ["0:30", "0:45", "1:00", "1:15", "1:30",
                                 "1:45", "2:00", "2:15", "2:30", "2:45",
                                 "3:00", "3:15", "3:30", "3:45", "4:00",
                                 "4:15", "4:30", "4:45", "5:00"]


class TestReadData:
    inputDir = path.join(curdir, "test", "input")

    def test_one_short_answer(self):
        data = readData(path.join(self.inputDir, "oneText.txt"))
        assert data == ["How have you been?"]

    def test_one_mcone(self):
        data = readData(path.join(self.inputDir, "oneMCOne.txt"))
        assert data == ["Pick the first option.\n", "\n",
                        "T This one\n", "F Not this one"]

    def test_one_mcmany(self):
        data = readData(path.join(self.inputDir, "oneMCMany.txt"))
        assert data == ["Will this code work?\n", "\n", "T Yes\n",
                        "F No\n", "T Hopefully\n", "F Who knows?"]

    def test_trailing_newlines(self):
        data = readData(path.join(self.inputDir, "trailingNewlines.txt"))
        assert data == ["This question has trailing whitespace.\n", "\n",
                        "F No, it doesn't\n", "T Yes, it does\n"]

    def test_multiple_various(self):
        data = readData(path.join(self.inputDir, "multVarious.txt"))
        assert data == ["Which of the following are Avengers?\n", "\n",
                        "T Iron Man\n", "F Superman\n", "F Wolverine\n",
                        "T Spiderman\n", "T Doctor Strange\n", "\n",
                        "Write an essay.\n", "\n",
                        "Did you like writing the essay?\n", "\n", "T Yes\n",
                        "F No\n", "\n", "Why or why not?\n", "\n",
                        "Should we include essays in the future?\n"]

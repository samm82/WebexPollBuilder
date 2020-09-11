from os import curdir, path
import sys

sys.path.append(path.abspath("src"))

from Process import formatString, formatAnswers, processQuestion


class TestFormatString:
    def test_strip_whitespace(self):
        assert formatString("test   ") == "test"
        assert formatString("  test \t\n") == "test"
        assert not formatString("\n \n \t   ")

    def test_replace_chars(self):
        assert formatString("&") == "&amp;"
        assert formatString("<") == "&lt;"
        assert formatString(">") == "&gt;"
        assert formatString("\"") == "&quot;"
        assert formatString("'") == "&apos;"
        assert formatString("a z") == "a&nbsp;z"

    def test_full_functionality(self):
        assert formatString(" \n \t &<te'st \"123\">\n ") \
            == "&amp;&lt;te&apos;st&nbsp;&quot;123&quot;&gt;"


class TestFormatAnswers:
    def test_just_mcone(self):
        ans = ["F This is wrong\n", "F So is this\n", "T This is it\n",
               "F Too far\n", "F Go back"]
        out = ['<ANSWER ISCORRECT="false">This&nbsp;is&nbsp;wrong</ANSWER>\n',
               '<ANSWER ISCORRECT="false">So&nbsp;is&nbsp;this</ANSWER>\n',
               '<ANSWER ISCORRECT="true">This&nbsp;is&nbsp;it</ANSWER>\n',
               '<ANSWER ISCORRECT="false">Too&nbsp;far</ANSWER>\n',
               '<ANSWER ISCORRECT="false">Go&nbsp;back</ANSWER>\n']
        a, q, i = formatAnswers(ans)
        assert a == out
        assert q == "mcone"
        assert i == len(out) + 3

    def test_just_mcmany(self):
        ans = ["T Iron Man\n", "F Superman\n", "F Wolverine\n",
               "T Spiderman\n", "T Doctor Strange"]
        out = ['<ANSWER ISCORRECT="true">Iron&nbsp;Man</ANSWER>\n',
               '<ANSWER ISCORRECT="false">Superman</ANSWER>\n',
               '<ANSWER ISCORRECT="false">Wolverine</ANSWER>\n',
               '<ANSWER ISCORRECT="true">Spiderman</ANSWER>\n',
               '<ANSWER ISCORRECT="true">Doctor&nbsp;Strange</ANSWER>\n']
        a, q, i = formatAnswers(ans)
        assert a == out
        assert q == "mcmany"
        assert i == len(out) + 3

    def test_mcmany_with_trailing(self):
        ans = ["T Iron Man\n", "F Superman\n", "F Wolverine\n",
               "T Spiderman\n", "T Doctor Strange\n", "\n",
               "This is the next question."]
        out = ['<ANSWER ISCORRECT="true">Iron&nbsp;Man</ANSWER>\n',
               '<ANSWER ISCORRECT="false">Superman</ANSWER>\n',
               '<ANSWER ISCORRECT="false">Wolverine</ANSWER>\n',
               '<ANSWER ISCORRECT="true">Spiderman</ANSWER>\n',
               '<ANSWER ISCORRECT="true">Doctor&nbsp;Strange</ANSWER>\n']

        a, q, i = formatAnswers(ans)

        assert a == out
        assert q == "mcmany"
        assert i == len(out) + 3


class TestProcessQuestion:
    stableDir = path.join(curdir, "test", "stable")

    def test_one_short_answer(self):
        q = ["Tell me something I do not know."]
        with open(path.join(self.stableDir, "oneTextOut-1.atp")) as f:
            stableOut = f.readlines()

        out, i = processQuestion(q, "5:00")

        assert out == stableOut
        assert i == 2

    def test_one_mcone(self):
        q = ["Can you answer this question?\n", "\n", "T Yes\n", "F No\n"]
        with open(path.join(self.stableDir, "oneMCOneOut-1.atp")) as f:
            stableOut = f.readlines()

        out, i = processQuestion(q, "0:45")

        assert out == stableOut
        assert i == 5

    def test_one_mcany(self):
        q = ["Will this code work?\n", "\n", "T Yes\n", "F No\n",
             "T Hopefully\n", "F Who knows?"]
        with open(path.join(self.stableDir, "oneMCManyOut-1.atp")) as f:
            stableOut = f.readlines()

        out, i = processQuestion(q, "1:45")

        assert out == stableOut
        assert i == 7

    def test_short_answer_with_trailing(self):
        q = ["Tell me something I do not know.\n", "\n", "Was that fun?"]
        with open(path.join(self.stableDir, "oneTextOut-1.atp")) as f:
            stableOut = f.readlines()

        out, i = processQuestion(q, "5:00")

        assert out == stableOut
        assert i == 2

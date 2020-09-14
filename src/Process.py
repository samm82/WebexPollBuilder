from GUI import invalidAnswerFormat, noBlankLineAfterQuestion, \
    noCorrectAnswer, noQuestion


def formatString(s):
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    s = s.replace("\"", "&quot;")
    s = s.replace("\'", "&apos;")
    return s.strip().replace(" ", "&nbsp;")


def formatAnswers(l):
    answers, trueCount = [], 0
    for line in l:
        if line and line != "\n":
            a = line.split(" ", 1)

            if a[0].upper() == 'T':
                correct = "true"
                trueCount += 1
            elif a[0].upper() == 'F':
                correct = "false"
            else:
                invalidAnswerFormat(a[0])
                return None, None, None

            answers.append('<ANSWER ISCORRECT="{0}">'.format(correct) +
                           '{0}</ANSWER>\n'.format(formatString(a[1])))

        else:
            break

    if trueCount == 1:
        qType = "mcone"
    elif trueCount > 1:
        qType = "mcmany"
    else:
        noCorrectAnswer()
        return None, None, None

    return answers, qType, len(answers) + 3


def processQuestion(l, t):
    if l[0] == "\n":
        noQuestion()
        return None, None
    else:
        if len(l) == 1 or l[2][0:2].upper() not in ["T ", "F "]:
            a, qType, i = [], "text", 2
        else:
            if l[1] != "\n":
                noBlankLineAfterQuestion(l[1].strip())
                return None, None
            a, qType, i = formatAnswers(l[2:])
            if a is None:
                return None, None

    return ['<?xml version="1.0" encoding="UTF-16"?>\n',
            '<POLL TYPE="named" SHOWTIMER="yes" ALARM="{0}"'.format(t) +
            ' NOANSWER="yes" SHOWRESPONSE="yes">\n', '\n',
            '<QUESTION TYPE="{0}"'.format(qType) +
            ' TITLE="{0}">\n'.format(formatString(l[0]))
            ] + a + ['</QUESTION>\n', '\n', '</POLL>'], i

def formatString(s):
    return s.strip().replace(" ", "&nbsp;")

def formatAnswers(l):
    answers, trueCount = [], 0
    for i in range(len(l)):
        if l[i] and l[i] != "\n":
            a = l[i].split(" ", 1)

            if a[0].upper() == 'T':
                correct = "true"
                trueCount += 1
            elif a[0].upper() == 'F':
                correct = "false"
            else:
                raise ValueError("Invalid input; expected 'T' or 'F', got", a[0])

            answers.append('<ANSWER ISCORRECT="{0}">{1}</ANSWER>\n'.format(correct, formatString(a[1])))

        else:
            break        

    if trueCount == 1:
        qType = "mcone"
    elif trueCount > 1:
        qType = "mcmany"
    elif trueCount == 0:
        raise ValueError("There must be at least one correct answer.")
    else:
        raise ValueError("Invalid number of correct questions; check that there is at least one.")

    return answers, qType, i + 3

def processQuestion(l, t):
    if not l[0]:
        raise ValueError("Expected title in file.")
    else:
        if len(l) == 1 or l[2][0:2].upper() not in ["T ", "F "]:
            a, qType, i = [], "text", 2
        else:
            if l[1] != "\n":
                raise ValueError("Expected blank line; check that the input file is formatted correctly.")
            a, qType, i = formatAnswers(l[2:])

    return ['<?xml version="1.0" encoding="UTF-16"?>\n', \
            '<POLL TYPE="named" SHOWTIMER="yes" ALARM="{0}" NOANSWER="yes" SHOWRESPONSE="yes">\n\n'.format(t), \
            '<QUESTION TYPE="{0}" TITLE="{1}">\n'.format(qType, formatString(l[0]))] + a + ['</QUESTION>\n\n</POLL>'], i

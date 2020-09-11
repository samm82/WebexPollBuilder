# WebexPollBuilder
A program to build polls to save and use with Webex from text files.

## Input File Format
- Each question should be on a separate line, with a blank line after the title.
- Each answer should be on a separate line, with either a "T" or an "F" at the start of the line (to denote if the question is a correct answer or not), followed by a space.
- There should be no trailing newlines at the end of the file.
- Questions not followed by answers will be processed as short answer questions.

### Example
```txt
// test/input/multVarious.txt

Which of the following are Avengers?

T Iron Man
F Superman
F Wolverine
T Spiderman
T Doctor Strange

Write an essay.

Did you like writing the essay?

T Yes
F No

Why or why not?

Should we include essays in the future?
```
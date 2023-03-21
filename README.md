# Quiz data collector

I wanted to create a quiz data collector for gathering my students' quiz exams responses into a CSV file that I can easily use to calculate their marks. So I asked to **ChatGPT** for a Python script with the following prompt:
```
Hi! I want to make an interactive Python application to register students responses of a quiz exam into a CSV file. To do so, I want to use inquirer. The script should first ask the number of quiz questions and then ask for the true answers (e.g. A, B, C, and so on). Then it should start a loop to keep askings for students' responses. For each student, it should first ask its name and ID and then ask for the student's response to each question. In the end, all responses should be stored into a CSV file with one row for each student plus a header row with the question numbers. The second row must be the true answers asked at the beginning of the script.
```

The first program (`scripts/program_v1.py`) is generated with the following explanation:

> This code first asks for the number of quiz questions and the true answers to those questions. It then enters a loop where it asks for the student's name and ID, as well as their responses to each question. It continues to ask for more students until the user indicates that there are no more students to add. Finally, it writes all the responses to a CSV file with one row for each student, a header row with the question numbers, and a second row with the true answers.

And this is the CSV generated in a first interaction:

```
Name,ID,Question 1,Question 2,Question 3
,A,B,C
Hugo,12,A,B,D
,123,A,A,A
```

It looks good but I want two corrections:
- Add an extra `,` in the second line which contains the true quiz answers.
- Remove `Question ` from the header row.

So my next prompt is:
```
It looks great!! Can you add two things:
- Ask for the output file name at the beginning.
- Remove "Question " from the header row.
- Fix the second row and add the missing "," at the beginning.
```

So it comes with a new version of the program (`scripts/program_v2.py`) that produces this CSV:
```
Name,ID,1,2,3
,A,B,C
Hugo,12,A,C,D
Pepe,13,B,D,E
Laura,13,B,,A
```

This version does not fix the problem with the second row but I'll fix it later. I ask it for a new "feature":
```
Good!! I want another feature: the script should also ask for the possible choices at the beginning (e.g. A, B, C or T/F) and then check if each answer introduced is within those possible choices.
```

And it gives me a new version (`scripts/program_v3.py`) that looks great but I notice that I forgot two make two things explicit, so I ask for them:
```
I forgot to mention two things that the script should also do:
- Allow for empty responses.
- The possible answer choices are all the same for all questions, so it should be only asked once at the beginning and not for every question.

Can you update the code accordingly?
```

And it gives the corrected code (`scripts/program_v4.py`), which works very well!

I only need to fix the way the second row is written into the file by changing it to `writer.writerow(['', '', *true_answers])` (it is `scripts/program_v4_fixed.py).

Finally, I created the `quiz-collector.py` script with `autopep8 scripts/program_v4_fixed.py  > quiz-collector.py`.

## Setting up the Python environment

Run these commands to set up the Python environment:
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install inquire
```
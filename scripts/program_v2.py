import csv
import inquirer

# Ask for the output file name
output_file = inquirer.prompt([inquirer.Text('output_file', message='What should be the name of the output file (without extension)?')])['output_file']

# Ask for the number of quiz questions
num_questions = inquirer.prompt([inquirer.Text('num_questions', message='How many questions are in the quiz?')])['num_questions']
num_questions = int(num_questions)

# Ask for the true answers to the quiz
true_answers = []
for i in range(1, num_questions+1):
    answer = inquirer.prompt([inquirer.Text(f'question_{i}', message=f'What is the correct answer for question {i}? (e.g. A, B, C)')])[f'question_{i}']
    true_answers.append(answer)

# Ask for student responses and store them in a CSV file
responses = []
while True:
    # Ask for the student's name and ID
    questions = [inquirer.Text('name', message='What is your name?'), inquirer.Text('id', message='What is your student ID?')]
    student_info = inquirer.prompt(questions)

    # Ask for the student's responses to each question
    student_responses = []
    for i in range(1, num_questions+1):
        response = inquirer.prompt([inquirer.Text(f'question_{i}', message=f'What is your answer for question {i}? (e.g. A, B, C)')])[f'question_{i}']
        student_responses.append(response)

    # Add the student's responses to the list of all responses
    responses.append([student_info['name'], student_info['id']] + student_responses)

    # Ask if there are more students to add
    more_students = inquirer.prompt([inquirer.Confirm('more_students', message='Do you want to add another student?')])['more_students']
    if not more_students:
        break

# Write the responses to a CSV file
with open(f'{output_file}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'ID'] + [f'{i}' for i in range(1, num_questions+1)])
    writer.writerow(['', *true_answers])
    writer.writerows(responses)

print(f'Quiz responses saved to {output_file}.csv')

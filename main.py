import importlib
import os
import sys

print(f"Estou executando a partir de: {os.getcwd()}")
print(f"O Python está procurando módulos em: {sys.path}")

all_questions = os.listdir('questions')

while True:

    try:
        question_number = int(input("Choose the question's number from 1 to 10: "))
    except ValueError:
        print("Invalid entry, you must specify a integer number between 1 and 10")
        continue

    file_name = f"Q{question_number}.py"

    if file_name in all_questions:
        question = "questions.Q" + str(question_number)
        try:
            if question in sys.modules:
                module = importlib.reload(sys.modules[question])
            else:
                module = importlib.import_module(question)
        except:
            print(f"Error: The question {question_number} was not found.")
    else:
        print("Error: The file was not found")
        continue

    status = input("Type 'Exit' if you want to end the program; Press any key if you want to continue: ")

    if status.lower() == 'exit':
        break

print("Program ended.")
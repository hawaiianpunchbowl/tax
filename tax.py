import csv
import random

def read_questions_from_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        questions = list(reader)
    return questions

def start_quiz(questions):
    random.shuffle(questions)
    for question, answer in questions:
        user_answer = input(f"Q: {question} (Yes/No): ").strip().lower()
        if user_answer not in ['yes', 'no']:
            print("Invalid input. Please answer with 'Yes' or 'No'.")
            continue
        if user_answer == answer.lower():
            print("Correct!")
        else:
            print("Wrong answer. Try again.")
            break
    else:
        print("Congratulations! You answered all questions correctly.")

def main():
    csv_file = 'tax.csv'  # Replace with your CSV file path
    questions = read_questions_from_csv(csv_file)
    start_quiz(questions)

if __name__ == "__main__":
    main()

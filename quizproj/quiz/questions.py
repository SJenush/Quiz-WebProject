import random


def CreateContext(action):
    questions = [
    "What is the capital of France?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the largest planet in our solar system?",
    "In what year did the Titanic sink?",
    "Who painted the Mona Lisa?",
    "What is the chemical symbol for water?",
    "Who was the first person to walk on the Moon?",
    "What is the smallest country in the world?",
    "What is the longest river in the world?",
    "Who is known as the 'Father of Computers'?"
    ]
    options = [
    ["Paris", "Rome", "Berlin", "Madrid"],
    ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
    ["Jupiter", "Saturn", "Earth", "Mars"],
    ["1912", "1905", "1923", "1898"],
    ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
    ["H2O", "CO2", "O2", "NaCl"],
    ["Neil Armstrong", "Yuri Gagarin", "Buzz Aldrin", "Michael Collins"],
    ["Vatican City", "Monaco", "San Marino", "Liechtenstein"],
    ["Nile", "Amazon", "Yangtze", "Mississippi"],
    ["Charles Babbage", "Alan Turing", "John von Neumann", "Blaise Pascal"]
    ]
    for opt in options:
        random.shuffle(opt)
    if action=='QuizPage':
        quiz_data=zip(questions,options)
        context={
        'quiz_data':quiz_data,
        }
    elif action=='ViewScore':
        quiz_data=zip(questions,GetAnswers())
        context={
        'quiz_data':quiz_data,
        }
    return context
def GetAnswers():
    answers = [
    "Paris",
    "William Shakespeare",
    "Jupiter",
    "1912",
    "Leonardo da Vinci",
    "H2O",
    "Neil Armstrong",
    "Vatican City",
    "Nile",
    "Charles Babbage"
    ]
    return answers
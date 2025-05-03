import nltk
from nltk.stem import WordNetLemmatizer
import random

# Download required NLTK data
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('punkt_tab')

# Define a dictionary of intents and responses
intents = {
    'greetings': ['Hello!', 'Hi!', 'Hey!'],
    'goodbye': ['See you later!', 'Bye!', 'Goodbye!'],
    'admission': ['You can contact our admission office for more information.', 'Please visit our website for admission details.'],
    'courses': ['We offer various courses in engineering, arts, and science.', 'You can check our website for course details.'],
    'fee': ['The annual fees range from 20,000/- to 30,000/- depending on the course']
}

# Define a function to process user input
def process_input(input_text):
    lemmatizer = WordNetLemmatizer()
    tokens = nltk.word_tokenize(input_text)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return tokens

# Define a function to generate responses
def generate_response(tokens):
    for intent, responses in intents.items():
        if any(token in intent for token in tokens):
            return random.choice(responses)
    return 'I didnt understand that. Please try again!'

def chatbot():
    print('Welcome to our college chatbot!')
    print('You can ask any details about admission,courses and fees')
    print('How can I help you')
    while True:
        user_input = input('You: ')
        tokens = process_input(user_input)
        response = generate_response(tokens)
        print('Chatbot:', response)
        if user_input.lower() == 'bye':
            break

# Run the chatbot
chatbot()
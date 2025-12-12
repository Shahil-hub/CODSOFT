import re
from datetime import datetime

print("Chatbot: Hey! I’m your RULE-BASED-Chatbot. Ask me anything! Type 'bye' to exit.\n")

def add_question(response, question):
    return f"{response} {question}"

def get_response(user_input):
    ui = user_input.lower()

    # ------------------------
    #  FACT-BASED RESPONSES
    # ------------------------

    # Richest person
    if "richest" in ui or "wealthiest" in ui:
        response = "The richest person on earth is Elon Musk with an estimated net worth of around $497 billion."
        return add_question(response, "Do you want to know about his companies?")

    # Richest company
    if "richest company" in ui or "most valuable company" in ui:
        response = "As of 2025, Microsoft is the most valuable company in the world."
        return add_question(response, "Do you want to know what Microsoft is famous for?")

    # World population
    if "world population" in ui:
        response = "The world population is approximately 8.1 billion people."
        return add_question(response, "Do you want to know which country has the highest population?")

    # Fastest car
    if "fastest car" in ui:
        response = "The fastest production car is the SSC Tuatara, reaching speeds over 531 km/h."
        return add_question(response, "Do you like supercars?")

    # Tallest building
    if "tallest building" in ui:
        response = "The tallest building in the world is the Burj Khalifa at 828 meters."
        return add_question(response, "Do you want to know where it is located?")

    # Largest country
    if "largest country" in ui:
        response = "The largest country by area is Russia."
        return add_question(response, "Do you want to know the largest country by population?")

    # Founder questions
    if "founder of google" in ui:
        response = "Google was founded by Larry Page and Sergey Brin."
        return add_question(response, "Do you want to know when it was founded?")

    if "founder of tesla" in ui:
        response = "Tesla was founded by Martin Eberhard and Marc Tarpenning, but Elon Musk made it famous."
        return add_question(response, "Do you want to know more about Tesla?")

    if "founder of openai" in ui:
        response = "OpenAI was founded by Sam Altman, Elon Musk, Greg Brockman and others in 2015."
        return add_question(response, "Do you want to know what OpenAI does?")

    # AI definitions
    if "what is ai" in ui:
        response = "AI, or Artificial Intelligence, refers to machines that can perform tasks requiring human-like intelligence."
        return add_question(response, "Do you want a simple or advanced explanation?")

    if "what is machine learning" in ui or "what is ml" in ui:
        response = "Machine Learning is a subset of AI where systems learn from data to make predictions or decisions."
        return add_question(response, "Do you want to know its real-life applications?")

    # --------------------------------
    #   DAILY KNOWLEDGE FEATURES
    # --------------------------------

    # Jokes
    if "joke" in ui:
        jokes = [
            "Why don't programmers like nature? It has too many bugs!",
            "Why do Java developers wear glasses? Because they don't C#!",
            "What do you call 8 hobbits? A hobbyte."
        ]
        response = jokes[0]
        return add_question(response, "Want another joke?")

    # Motivation
    if "motivate" in ui or "motivation" in ui or "quote" in ui:
        response = "Believe in yourself — every expert was once a beginner!"
        return add_question(response, "Do you want another motivation quote?")

    # Compliment
    if "you are smart" in ui:
        response = "Thank you! I try my best."
        return add_question(response, "Do you want me to compliment you too?")

    # ------------------------
    #  OTHER BASIC FEATURES
    # ------------------------

    # Greetings
    if re.search(r"\b(hi|hello|hey|hola)\b", ui):
        return add_question("Hello! How can I help you today?", "What would you like to ask?")

    # Asking name
    if "your name" in ui:
        return add_question("I am a rule-based smart chatbot created by Shahil!", "What's your name?")

    # Creator
    if "who created you" in ui:
        return add_question("I was created by Shahil as part of his AI internship project!", "Do you want him to teach you AI too?")

    # Date
    if "date" in ui:
        today = datetime.now().strftime("%d %B %Y")
        return add_question(f"Today's date is {today}.", "Do you want to know the time too?")

    # Time
    if "time" in ui:
        current_time = datetime.now().strftime("%I:%M %p")
        return add_question(f"The current time is {current_time}.", "Anything else you want to check?")

    # Weather
    if "weather" in ui:
        return add_question("I can't fetch live weather, but it seems like a good day!", "How’s the weather in your place?")

    # Thanks
    if "thank" in ui:
        return add_question("You're welcome!", "Need help with something else?")

    # Help
    if "help" in ui:
        return add_question("Sure! I'm here to help.", "Tell me what's bothering you?")

    # Exit
    if "bye" in ui:
        return "Goodbye! Have a great day!"

    # ------------------------
    #  DEFAULT RESPONSE
    # ------------------------
    return add_question("Sorry, I didn't understand that.", "Can you rephrase your question?")


# Chat loop
while True:
    msg = input("You: ")
    reply = get_response(msg)
    print("Chatbot:", reply)
    if "bye" in msg.lower():break

import spacy
import numpy as np
import joblib
import streamlit as st

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # If the model is not found, download it
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


heart_disease_model = joblib.load("ensemble_model.joblib")

# Define a simple set of rules for the chatbot
chat_rules = {
    "greet": ["hello", "hi", "hey"],
    "farewell": ["bye", "goodbye", "see you"],
    "ask_heart_disease": [
        "what is heart disease",
        "tell me about heart disease",
        "how does heart disease occur",
        "what are the symptoms of heart disease",
        "how to prevent heart disease",
    ],
    "predict_heart_disease": ["predict", "prediction"],
}


# Function to process user input and generate a response
def process_input(user_input):
    user_input_lower = user_input.lower()

    # Check for greetings
    if any(greeting in user_input_lower for greeting in chat_rules["greet"]):
        return "Hello! How can I help you learn about heart disease?"

    # Check for farewell
    elif any(token in user_input_lower for token in chat_rules["farewell"]):
        return "Goodbye! If you have more questions, feel free to ask."

    # Check for heart disease queries
    for question in chat_rules["ask_heart_disease"]:
        if question in user_input_lower:
            return get_answer_for_question(user_input_lower)

    # Check for heart disease prediction
    if any(phrase in user_input_lower for phrase in chat_rules["predict_heart_disease"]):
        return predict_heart_disease(user_input)

    # Handle unrecognized input
    return "I'm sorry, I didn't understand that. Could you please rephrase or ask another question?"


# Function to get answers for specific questions
def get_answer_for_question(question):
    if "how does heart disease occur" in question:
        return "Heart disease can occur due to factors such as high blood pressure, high cholesterol, smoking, and a sedentary lifestyle. Genetics also play a role."

    if "what are the symptoms of heart disease" in question:
        return "Common symptoms include chest pain, shortness of breath, fatigue, and irregular heartbeats. However, symptoms can vary."

    if "how to prevent heart disease" in question:
        return "To prevent heart disease, maintain a healthy diet, exercise regularly, avoid smoking, limit alcohol intake, and manage stress. Regular check-ups are also important."

    # Default response if the question is not recognized
    return "I'm sorry, I don't have information on that specific question. Please ask another question about heart disease."

import streamlit as st
import numpy as np


import streamlit as st
import numpy as np

def predict_heart_disease(user_input):
    try:
        # Initialize questions and answers
        questions = [
            "Please enter your age:",
            "Please enter your chest pain level (Typical Angina, Atypical Angina, Non-Anginal Pain, Asymptomatic):",
            "Please enter your resting blood pressure:",
            "Please enter your cholesterol level:",
            "Please enter your maximum heart rate:"
        ]

        # Initialize index to track the current question
        question_index = st.session_state.get("question_index", 0)

        # Ask questions related to heart disease risk factors
        if question_index < len(questions):
            # Display the current question
            user_answer = st.text_input(questions[question_index])

            # Check if user has provided an answer
            if user_answer.strip():
                # Append question and answer to chat history
                st.session_state.chat_history.append({"user": questions[question_index], "chatbot": user_answer})

                # Increment the question index to proceed to the next question
                question_index += 1

        # Check if all questions have been answered
        if question_index == len(questions):
            # Prepare input features for the model
            features = np.array([
                [int(st.session_state.chat_history[0]["chatbot"]), int(st.session_state.chat_history[1]["chatbot"]),
                 int(st.session_state.chat_history[2]["chatbot"]), int(st.session_state.chat_history[3]["chatbot"]),
                 int(st.session_state.chat_history[4]["chatbot"])]
            ])

            # Make a prediction
            prediction = heart_disease_model.predict(features)

            # Display prediction within the Streamlit app
            if prediction == 1:
                st.error("Chatbot: Based on your inputs, there is a potential risk of heart disease. It is recommended to consult with a healthcare professional for further evaluation.")
            else:
                st.success("Chatbot: Based on your inputs, there is no apparent risk of heart disease. However, it's always a good idea to maintain a healthy lifestyle and consult with a healthcare professional for personalized advice.")

        # Use a button to proceed to the next question
        if question_index < len(questions):
            if st.button("Next"):
                # Update the question index in the session state
                st.session_state.question_index = question_index

                # Clear the user input field after clicking "Next"
                st.session_state.user_input = ""

    except ValueError as e:
        st.error(f"Error: {str(e)}. Please enter valid input values.")

def chatbot_main():
    print("Chatbot: Hello! I'm your heart disease chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip()

        # Check for exit command
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        # Process user input and generate a response
        response = process_input(user_input)
        print("Chatbot:", response)


# Run the chatbot
if __name__ == "__main__":
    chatbot_main()

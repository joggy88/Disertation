import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # If the model is not found, download it
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

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
            return get_answer_for_question(question)

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

    if any(phrase in user_input_lower for phrase in chat_rules["predict_heart_disease"]):
        return initiate_heart_disease_prediction()

    # Default response if the question is not recognized
    return "I'm sorry, I don't have information on that specific question. Please ask another question about heart disease."

# Main loop for user interaction
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

def predict_heart_disease(user_input):
    try:
        # Ask questions related to heart disease risk factors
        age = int(input("Please enter your age: "))
        chest_pain = input("Please enter your chest pain level (Typical Angina, Atypical Angina, Non-Anginal Pain, Asymptomatic): ")
        resting_bp = int(input("Please enter your resting blood pressure: "))
        cholesterol = int(input("Please enter your cholesterol level: "))
        max_heart_rate = int(input("Please enter your maximum heart rate:"))

        # Map chest pain to numerical values
        chest_pain_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
        chest_pain_level = chest_pain_mapping.get(chest_pain, -1)

        # Check for invalid inputs
        if any(value < 0 for value in [age, resting_bp, cholesterol, max_heart_rate]) or chest_pain_level == -1:
            raise ValueError("Invalid input. Please enter valid numerical values.")

        # Prepare input features for the model
        features = np.array([[age, chest_pain_level, resting_bp, cholesterol, max_heart_rate]])

        # Make a prediction
        prediction = heart_disease_model.predict(features)

        # Provide a response based on the prediction
        if prediction == 1:
            return "Based on your inputs, there is a potential risk of heart disease. It is recommended to consult with a healthcare professional for further evaluation."
        else:
            return "Based on your inputs, there is no apparent risk of heart disease. However, it's always a good idea to maintain a healthy lifestyle and consult with a healthcare professional for personalized advice."

    except ValueError as e:
        return f"Error: {str(e)}. Please enter valid input values."


# Run the chatbot
if __name__ == "__main__":
    chatbot_main()

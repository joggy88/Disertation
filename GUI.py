import streamlit as st
import joblib
import feedparser




def get_heart_disease_news():
    rss_feed_url = "https://www.news-medical.net/medical/news"  # Replace with the actual RSS feed URL
    feed = feedparser.parse(rss_feed_url)
    return feed.entries

# Load the trained SVC model
model = joblib.load('ensemble_model.joblib')


def predict_with_sliders():
    st.write("Input your health parameters to get a risk assessment for heart disease.")

    # User Input
    age = st.slider("Age", min_value=20, max_value=80, value=40)
    chest_pain = st.selectbox("Chest Pain Level", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    resting_bp = st.slider("Resting Blood Pressure (mm Hg)", min_value=90, max_value=200, value=120)
    cholesterol = st.slider("Cholesterol Level (mg/dL)", min_value=100, max_value=400, value=200)
    max_heart_rate = st.slider("Max Heart Rate", min_value=70, max_value=220, value=120)

    # Convert categorical chest pain to numerical
    chest_pain_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
    chest_pain_numeric = chest_pain_mapping[chest_pain]

    # Make prediction
    if st.button("Predict"):
        features = [[age, chest_pain_numeric, resting_bp, cholesterol, max_heart_rate]]
        prediction = model.predict(features)

        # Display prediction within the Streamlit app
        if prediction[0] == 1:
            st.error("You may have heart disease. Please consult a healthcare professional.")
        else:
            st.success("You are likely healthy. Keep up the good work!")
def main():

    st.warning(
        "Heart disease predictions in this app are based on user inputs and should not substitute professional medical advice. It is recommended to consult with healthcare experts for further tests and evaluation before confirming the accuracy of the prediction.")

    # Sidebar Menu
    menu = st.sidebar.selectbox("Select Menu",
                                ["Home", "Heart Disease Prediction", "News About Heart Disease", "Ethical Considerations"])

    if menu == "Home":
        st.title("Heart Disease Prediction App")
        st.markdown("Welcome to the Heart Disease Prediction App! Use the menu on the left to navigate.")
        # Add image to the header
        image_path = "heart.png"
        st.image(image_path, use_column_width=True)
    # Prediction Menu
    elif menu == "Heart Disease Prediction":
        st.title("Heart Disease Prediction")
        st.write("Input your health parameters to get a risk assessment for heart disease.")
        image_path = "original.jpg"
        st.image(image_path, use_column_width=True)
        predict_with_sliders()

    elif menu == "News About Heart Disease":
        st.subheader("News About Heart Disease")
        image_path = "news.jpg"
        st.image(image_path, use_column_width=True)
        st.write(
            "To read American Heart Association (AHA) News about heart disease, click [here](https://newsroom.heart.org/search?ct=releases).")
        st.write(
            "To read Centers for Disease Control and Prevention (CDC) News about heart disease, click [here](https://www.cdc.gov/media/index.html).")
        st.write("To read MedlinePlus News about heart disease, click [here](https://medlineplus.gov/rss.html).")
        st.write(
            "To read News Medical Life Sciences about heart disease, click [here](https://www.news-medical.net/medical/news).")
        st.write(
            "To read Science Daily News about heart disease, click [here](https://www.sciencedaily.com/news/health_medicine/heart_disease/).")
        st.write(
            "To read British Heart Foundation News about heart disease, click [here](https://www.bhf.org.uk/what-we-do/news-from-the-bhf).")
        st.write(
            "To read Independent News about heart disease, click [here](https://www.independent.co.uk/topic/heart-disease).")
        st.write(
            "To read New Scientist News about heart disease, click [here](https://www.newscientist.com/article-topic/heart-disease/).")
        st.write(
            "To read Health Gov News about heart disease, click [here](https://health.gov/news/category/news-announcements).")
    # Ethical Considerations Menu
    elif menu == "Ethical Considerations":
        st.subheader("Ethical Considerations")

        # Add an image related to ethical considerations
        image_path = "ethical.jpg"
        st.image(image_path, use_column_width=True)

        # Provide information about ethical considerations
        st.write("### Data Privacy and Security:")
        st.write(
            "Our app takes data privacy and security seriously. User data is collected solely for the purpose of heart disease prediction and is stored securely. We implement industry-standard encryption and access controls to protect user information.")

        st.write("### Informed Consent:")
        st.write(
            "Before using our app, users are required to provide informed consent. This includes understanding how their data will be used, what information will be collected, and the purpose of the heart disease prediction. Users can review and agree to our privacy policy during the onboarding process.")

        st.write("### Algorithm Transparency:")
        st.write(
            "We are committed to transparency in our algorithm. While the details of our proprietary algorithm are confidential, we provide a high-level overview of the factors considered in our heart disease prediction. We aim to demystify the prediction process as much as possible.")

        st.write("### Bias and Fairness:")
        st.write(
            "Efforts are made to mitigate biases in our algorithm to ensure fairness in predictions. We regularly assess and address potential biases in the data used for training the model. Our goal is to provide accurate and unbiased predictions for all users.")

        st.write("### User Empowerment:")
        st.write(
            "Users are empowered with information about the limitations of the prediction model. We emphasize that our app is a tool for informational purposes and not a substitute for professional medical advice. Users are encouraged to consult with healthcare professionals for a comprehensive assessment of their health.")

        st.write("### Accessibility and Inclusivity:")
        st.write(
            "We are committed to making our app accessible to all users. Efforts are made to ensure inclusivity in design, considering different user abilities and needs. We welcome feedback on accessibility improvements to enhance the user experience for everyone.")

        st.write("### Regulatory Compliance:")
        st.write(
            "Our app complies with relevant data protection and privacy regulations, including [mention specific regulations]. We adhere to best practices in the industry to safeguard user data and ensure legal compliance. Our commitment to regulatory standards is unwavering.")

        st.write("### Contact Information:")
        st.write(
            "For any questions, concerns, or to report issues related to ethics or privacy, users can contact our support team at [6adeoh78@solent.ac.uk, +447770230304]. We value user feedback and are dedicated to addressing inquiries promptly.")


# Run the app
if __name__ == "__main__":
    main()

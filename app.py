import streamlit as st
import pickle

#========================loading the saved files==================================================
model = pickle.load(open('logistic_regression.pkl', 'rb'))
feature_extraction = pickle.load(open('feature_extraction.pkl', 'rb'))

def predict_mail(input_text):
    input_user_mail = [input_text]
    input_data_features = feature_extraction.transform(input_user_mail)
    prediction = model.predict(input_data_features)
    return prediction

# Streamlit code for the UI
def main():
    st.title("Spam Mail Detection")
    st.write("Enter an email message to classify it as spam or not spam.")

    # Text input for the email message
    mail = st.text_area("Email Text")

    if st.button("Classify"):
        if mail:
            predicted_mail = predict_mail(input_text=mail)
            if predicted_mail[0] == 1:
                st.error("This email is classified as Spam.")
            else:
                st.success("This email is classified as Not Spam.")
        else:
            st.warning("Please enter the text of the email.")

if __name__ == '__main__':
    main()

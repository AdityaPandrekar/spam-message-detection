import streamlit as st
import sklearn
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
    st.title("Spam Mail/Message Detection")
    st.write("Enter your message to check whether it's spam or not.")

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

    st.markdown("---")  # Add a horizontal line to separate the content

    st.markdown(
    """
    ### Credits

    This app was developed by [Aditya Pandrekar](https://yourwebsite.com).  
    Special thanks to [Knowledge Doctor](https://www.youtube.com/@knowledgedoctor3849).

    Powered by [Streamlit](https://streamlit.io/) and [GitHub](https://github.com/).

    [![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-brightgreen?logo=github)](https://github.com/AdityaPandrekar/spam-message-detection)
    """
    )

if __name__ == '__main__':
    main()

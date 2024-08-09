import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

def main():
	st.title("Spam Message/Mail Detection")
	st.write("Build with Streamlit & Python")
	activites=["Classification", "About"]
	choices=st.sidebar.selectbox("Select Activities",activites)
	if choices=="Classification":
		st.subheader("Classification")
		msg=st.text_input("Enter a text")
		if st.button("Process"):
			print(msg)
			print(type(msg))
			data=[msg]
			print(data)
			vec=cv.transform(data).toarray()
			result=model.predict(vec)
			if result[0]==0:
				st.success("This is Not A Spam Email")
			else:
				st.error("This is A Spam Email")
	else:
		st.markdown(
    	"""
    	### Credits

    	This app was developed by [Aditya Pandrekar].    
    	Powered by [Streamlit](https://streamlit.io/) and [GitHub](https://github.com/).

    	[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-brightgreen?logo=github)](https://github.com/	AdityaPandrekar/spam-message-detection)
    	"""
		)
					
main()

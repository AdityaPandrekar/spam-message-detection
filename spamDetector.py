import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

def main():
	st.title("Spam Message/Mail Detection")
	st.write("Build with Streamlit & Python")
	activites=["Classification"]
	choices=st.sidebar.selectbox(activites)
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
					
main()

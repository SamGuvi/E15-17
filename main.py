import streamlit as st

st.title("Streamlit  Demo")

Name=st.text_input("Enter your Channel Name")

if st.button("Submit"):
    st.write("Hello",Name, 'Welcome to Streamlit Demo')
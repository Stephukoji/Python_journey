import streamlit as st

st.title("Fun Interactive Survey")

name = st.text_input("What is your name?")
nickname = st.text_input("What do your friends call you?")
occupation = st.text_input("What do you do for a living?")
feedback = st.text_area("What do you think about my code?")

if st.button("Submit"):
    st.write(f"Your name is {name}, but your friends call you {nickname}.")
    st.write("I bet you love that!")
    st.write(f"{occupation}? That's cool!")
    st.write("Thanks for your feedback, it means a lot to me!")

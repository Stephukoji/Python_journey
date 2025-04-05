import streamlit as st

st.title("Hey there! 👋 Let's get to know you a bit")

# Ask for name
name = st.text_input("What is your name?")
if name:
    st.write(f"Your name is {name}")

# Ask for nickname
nickname = st.text_input("What do your friends call you?")
if nickname:
    st.write(f"But your friends call you {nickname}. I bet you love that!")

# Ask for occupation
occupation = st.text_input("What do you do for a living?")
if occupation:
    st.write(f"That's cool!")

# Ask for feedback
feedback = st.text_area("What do you think about my codes?")
if feedback:
    st.write("Thanks for your feedback — it means a lot to me! 💬")

import streamlit as st

st.write("This story is only a non-fiction work. If it bears any resemblance to a real person, it is purely coincidental.")

st.markdown("**⚠️ Warning: Rated 18+**", unsafe_allow_html=True)

st.write("David is a teenager with a head for education and a naughty heart.")
st.write("He is a 2nd year computer science student at Abraka University.")

interact = st.text_input("What do you think of David?")
if interact:
    st.write(f"{interact}, hmm! You might be right.")

proceed = st.text_input("Do you want me to continue the story of David?")
if proceed:
    if "yes" in proceed.lower() and "no" not in proceed.lower():
        st.write("Alright, let's go on...")
        st.write("Stay tuned 😂")
    else:
        st.write("Okay, goodbye.")

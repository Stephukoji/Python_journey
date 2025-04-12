 st.write("This story is only a non-fiction work, if it bears any resemblance to an real person, it is purely coincedental.")
st.write("\033[31m","warning:", "\033[0m", "rated 18+")
st.write()
st.write("David is a teenager with head for education and a naughty heart")
st.write("he is a 2nd year computer science student at Abraka University")
interact= st.text_input("what do you think of David?")
st.write(interact, ",", "hmm! you might be right", ".")
proceed =st.text_input ("do you want me to continue the story of David?")
if "yes" in proceed and "no" not in proceed:
  st.write("alright, let's go on....")
  st.write("stay tuned",  "😂")
else:
  st.write ("okay, goodbye")
  exit()

import streamlit as st

# Initialize scores
a, b, c, d = 0, 0, 0, 0

st.title("🔥 Which Warrior Personality Matches You? ⚔️")

st.write("Answer the questions below to see which legendary warrior you resemble!")

# Question 1
qs1 = st.radio("What motivates you the most?", [
    "A) Protecting the people I care about and never giving up!",
    "B) Proving that I am the best through skill and hard work.",
    "C) Gaining ultimate power and shaping the world my way.",
    "D) Learning, guiding, and becoming a wise leader."
], index=None)

if qs1:
    if qs1.startswith("A"):
        a += 1
    elif qs1.startswith("B"):
        b += 1
    elif qs1.startswith("C"):
        c += 1
    elif qs1.startswith("D"):
        d += 1

# Question 2
qs2 = st.radio("How do you handle challenges?", [
    "A) Face them head-on with pure determination.",
    "B) Stay calm, think, and then act.",
    "C) Overpower anything in my way.",
    "D) Outsmart the challenge and find a clever solution."
], index=None)

if qs2:
    if qs2.startswith("A"):
        a += 1
    elif qs2.startswith("B"):
        b += 1
    elif qs2.startswith("C"):
        c += 1
    elif qs2.startswith("D"):
        d += 1

# Question 3
qs3 = st.radio("Which personality trait fits you best?", [
    "A) Energetic and never giving up.",
    "B) Mysterious and focused.",
    "C) Powerful and intimidating.",
    "D) Calm and disciplined."
], index=None)

if qs3:
    if qs3.startswith("A"):
        a += 1
    elif qs3.startswith("B"):
        b += 1
    elif qs3.startswith("C"):
        c += 1
    elif qs3.startswith("D"):
        d += 1

# Question 4
qs4 = st.radio("How do you deal with failure?", [
    "A) Keep trying no matter what.",
    "B) Take it as motivation to train harder.",
    "C) Use it as fuel for revenge and dominance.",
    "D) Learn from it and improve myself."
], index=None)

if qs4:
    if qs4.startswith("A"):
        a += 1
    elif qs4.startswith("B"):
        b += 1
    elif qs4.startswith("C"):
        c += 1
    elif qs4.startswith("D"):
        d += 1

# Question 5
qs5 = st.radio("What kind of fighter would you be?", [
    "A) A fearless warrior who never backs down.",
    "B) A skilled duelist with precision and control.",
    "C) A powerful force, feared by all.",
    "D) A master strategist who wins with intelligence."
], index=None)

if qs5:
    if qs5.startswith("A"):
        a += 1
    elif qs5.startswith("B"):
        b += 1
    elif qs5.startswith("C"):
        c += 1
    elif qs5.startswith("D"):
        d += 1

# Question 6
qs6 = st.radio("What’s your approach to leadership?", [
    "A) Inspire others with my energy and passion.",
    "B) Lead by example and let my skills speak for me.",
    "C) Take control and establish my authority.",
    "D) Guide and mentor others with wisdom."
], index=None)

if qs6:
    if qs6.startswith("A"):
        a += 1
    elif qs6.startswith("B"):
        b += 1
    elif qs6.startswith("C"):
        c += 1
    elif qs6.startswith("D"):
        d += 1

# Question 7
qs7 = st.radio("How do you handle enemies or opponents?", [
    "A) Try to turn them into friends.",
    "B) Defeat them with skill and move forward.",
    "C) Crush them and make sure they never rise again.",
    "D) Outsmart them and avoid unnecessary fights."
], index=None)

if qs7:
    if qs7.startswith("A"):
        a += 1
    elif qs7.startswith("B"):
        b += 1
    elif qs7.startswith("C"):
        c += 1
    elif qs7.startswith("D"):
        d += 1

# Question 8
qs8 = st.radio("What’s your dream role in life?", [
    "A) Becoming a great leader who protects everyone.",
    "B) Becoming the strongest and most skilled individual.",
    "C) Gaining ultimate power and rewriting the rules.",
    "D) Becoming a wise mentor and teacher."
], index=None)

if qs8:
    if qs8.startswith("A"):
        a += 1
    elif qs8.startswith("B"):
        b += 1
    elif qs8.startswith("C"):
        c += 1
    elif qs8.startswith("D"):
        d += 1

# Determine the result
if max(a, b, c, d) == a:
    st.subheader("🥇 You are a Brave Hero! 🔥")
    st.write("You are energetic, determined, and never give up! You believe in protecting others and inspiring those around you.")
    st.image("Nprofile2.jpg", width=200)


    # st.image("https://upload.wikimedia.org/wikipedia/en/9/97/Naruto_Uzumaki.png", width=200)

elif max(a, b, c, d) == b:
    st.subheader("🥇 You are a Skilled Warrior! ⚔️")
    st.write("You are intelligent, precise, and always improving. You seek perfection in everything you do.")
    # st.image("https://upload.wikimedia.org/wikipedia/en/d/d8/SasukeUchiha.png", width=200)
    st.image("sasuke.jpeg", width=200)

elif max(a, b, c, d) == c:
    st.subheader("🥇 You are a Powerful Overlord! 🔥")
    st.write("You are strong, ambitious, and not afraid to take control. You have a vision for the future and will do anything to make it happen.")
    # st.image("https://static.wikia.nocookie.net/naruto/images/4/4d/Madara_Uchiha.png", width=200)
    st.image("madara.jpg", width=200)

elif max(a, b, c, d) == d:
    st.subheader("🥇 You are a Wise Master! 📖")
    st.write("You are calm, disciplined, and always thinking ahead. You prefer strategy over brute force and value intelligence above all.")
    # st.image("https://upload.wikimedia.org/wikipedia/en/7/76/Kakashi_Hatake.png", width=200)
    st.image("kakashi.jpg", width=200)
st.write("💡 **Share your results with your friends and see which warrior they are!**")

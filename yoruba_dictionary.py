import streamlit as st

st.title("Yoruba Dictionary")

yoruba_dict = {
"E kaasan": "Good afternoon",
    "Omi": "Water",
    "Ore": "Friend",
    "Ounje": "Food",
    "Ile": "House",
    "Iwe": "Book",
    "Iya": "Mother",
    "Oko": "Vehicle",
    "Baba": "Father",
    "Omo": "Child",
    "Owo": "Money",
    "Ojo": "Day",
    "Osan": "Orange",
    "Aso": "Cloth",
    "Ina": "Fire",
    "Ayo": "Joy",
    "Ibanuje": "Sadness",
    "E kaaaro": "Good Morning",
    "Ona": "Road",
    "Eru": "Fear",
}

word = st.text_input("Enter your word:")


if st.button("Translate"):
    if word in yoruba_dict:
        st.success(f"Your English translation is: {yoruba_dict[word]}")
    else:
        st.error("Word wasn't found")

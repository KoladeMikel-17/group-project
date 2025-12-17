yoruba_dict = {
    "E kaasan": "Good afternoon",
    "omi": "Water",
    "ore": "Friend",
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
    "Ina":"Fire",
    "Ayo": "Joy",
    "Ibanuje": "Sadness",
    "E kaaaro": "Good Morning",
    "Ona": "Road",
    "Eru": "Fear"
}

word = input("Enter your word: ")

if word in yoruba_dict:
    print("Your english translation is: ", yoruba_dict[word])
else:
    print("Word wasn't found")
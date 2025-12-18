Igbo_dictionary={
    "Ututu Oma":"Good Morning",
    "Ehihie Oma": "Good Afternoon",
    "Mmiri": "Water",
    "Enyi": "Friend",
    "Nri": "Food",
    "Ulo": "House",
    "Akwukwo": "Book",
    "Nne": "Mother",
    "Ugboala": "Vehicle",
    "Nna": "Father",
    "Nwa": "Child",
    "Ego": "Money",
    "Ubochi": "Day",
    "Oronji": "Orange",
    "Uwe": "Cloth",
    "Oku": "Fire",
    "Onu": "Joy",
    "Mwute": "Sadness",
    "Uzo": "Road",
    "Egwu": "Fear",
}
word = input("Enter your word: ")

if word in Igbo_dictionary:
    print("Your English Translation is: ", Igbo_dictionary [word] )
else: print ("word wasn't found")
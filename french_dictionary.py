# English to French Dictionary Program

dictionary = {
    "good morning": "bonjour",
    "good afternoon": "bon après-midi",
    "water": "eau",
    "friend": "ami",
    "food": "nourriture",
    "house": "maison",
    "book": "livre",
    "mother": "mère",
    "vehicle": "véhicule",
    "father": "père",
    "child": "enfant",
    "money": "argent",
    "day": "jour",
    "orange": "orange",
    "cloth": "tissu",
    "fire": "feu",
    "joy": "joie",
    "sadness": "tristesse",
    "road": "route",
    "fear": "peur"
}

word = input("Enter an English word: ").lower()

if word in dictionary:
    print("French translation:", dictionary[word])
else:
    print("Word not found in dictionary")
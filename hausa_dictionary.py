hausa_dictionary ={
    "good morning": "ina kwana",
    "good afternoon": "ina wuni",
    "water": "ruwa",
    "friend": "aboki",
    "food": "abinci",
    "house": "gida",
    "book": "littafi",
    "mother": "uwa",
    "vehicle": "mota",
    "father": "uba",
    "child": "yaro",
    "money": "kudi",
    "day": "rana",
    "orange": "lemu",
    "cloth": "tufafi",
    "fire": "wuta",
    "joy": "farin ciki",
    "sadness": "bakin ciki",
    "road": "hanya",
    "fear": "tsoro",
    }
    def translate(word):
        """
        Translate an English word to hausa.
        Returns the Hausa translation if found,
        otherwise returns a 'word not found' message 
        """
        word_lower = word.lower() # make input lowercase
        if word_lower in hausa_dictionary:
            return hausa_dictionary[word_lower]
            else:
                return "word not found in Hausa dictionary"
                if __name__ == "__main__":
                    while True:
                        word = input("Enter an English word to translate to Hausa (or 'exit' to quit): ").lower()
                        if word == "exit":
                            print("Goodbye")
                            break
                            print(f"Hausa translation: {translate(word)}")
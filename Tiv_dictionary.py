Tiv_dictionary = {
     "M ngu u wan" : " Good morning",
     "M ngu u sha" : "Good afternoon",
     "Ame" : "Water",
     "Or" : "Friend",
     "Nyam" : "Food",
     "Ior" : "House",
     "Buku" : "Book",
     "Iye" : "Mother",
     "Moto" : "Vehicle",
     "Ter" : "Father",
     "Wan" : "Child",
     "Kpen" : "Money",
     "Usha" : "Day",
     "Orinji" : "Orange",
     "Anger" : "Cloth",
     "Utem" : "Fire",
     "Mrumun" : "Joy",
     "Mnyian" : "Sadness",
     "Ortom" : "Road",
     "Ivungu" : "Fear",
 }
word = input("Enter your word: ")

if word in Tiv_dictionary:
     print("Your English translation is: ", Tiv_dictionary[word])
else:
     print("word wasn't found")
import random
word_bank=[
    "Apple", "Ball", "Cat", "Dog", "Egg", "Fish", "Goat", "Hat", "Ice", "Jar",
    "Kite", "Lamp", "Map", "Nest", "Orange", "Pen", "Queen", "Rain", "Sun", "Tree",
    "Umbrella", "Van", "Wind", "Yarn", "Zoo", "Book", "Cup", "Door", "Ear", "Fox",
    "Grapes", "House", "Ink", "Jug", "Key", "Leaf", "Moon", "Net", "Owl", "Pig",
    "Quilt", "Ring", "Star", "Top", "Umbra", "Vest", "Wagon", "Box", "Yell", "Zip"
]
word=random.choice(word_bank)
word=word.lower()
guess_word=["."]*len(word)
attempts=10
while attempts>0:
    print("\n Current word: ","_".join(guess_word))
    guess=input("Guess a letter:    ")
    guess=guess.lower()
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guess_word[i]=guess
        print("Good guess")
        
    else:
        attempts=attempts-1
        print(f"Wrong guess \n Attempts left={attempts}")
    if '.' not in guess_word:
        print("\nCongratulations!! You guessed the word: " , word)
        break
else:
  print("\n You have run out of attempts! The word was: " , word)
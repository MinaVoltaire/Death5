import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

blanks = []
for line in chosen_word :
    blanks.append("_ ")
print("".join(blanks))

random_word = []
for letter in chosen_word:
    random_word.append(letter)
death = 0
lives = 6
    
while not random_word == blanks or death == lives:
    player_input = input("Guess a letter: ").lower()
    print(death)
    for x in range(len(random_word)):
        if random_word[x] == player_input:
            blanks[x] = player_input
        else:
            death += 1
    print(''.join(blanks))
    print(death)
    print('debug')
    print(f"Lives left: {lives - death}")
    


        
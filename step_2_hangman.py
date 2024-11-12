import random
hangman = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
stage_0 = '''
     _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
'''
stage_1 = '''
     _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
'''
stage_2 = '''
_______
     |/      |
     |      (_)
     |      \|
     |      
     |      
     |
    _|___
'''
stage_3 = '''
_______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
'''
stage_4 = '''
_______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
'''
stage_5 = '''
_______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
'''
stage_6 = '''
    _______
        |/      |
        |      (_)
        |      \|/
        |       |_
        |      / /
        |
       _|___
'''

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(hangman)
print(stage_0)
placeholder = []
for line in chosen_word :
    placeholder.append("_ ")
print("".join(placeholder))
random_word = []
for letter in chosen_word:
    random_word.append(letter)
wrong_letters = []
death = 0
lives = 6
    
while not random_word == placeholder:
    player_input = input("\nGuess a letter: ").lower()

    for x in range(len(random_word)):
        if random_word[x] == player_input:
            placeholder[x] = player_input
    if player_input in wrong_letters:
        print("You've already type that letter.")
    elif player_input not in random_word:
        death += 1
        wrong_letters.append(player_input)
    print(''.join(placeholder))
    print("")
    print(f"Lives left: {lives - death}")
    if death == 0:
        print(stage_0)
    if death == 1:
        print(stage_1)
    if death == 2:
        print(stage_2)
    if death == 3:
        print(stage_3)
    if death == 4:
        print(stage_4)
    if death == 5:
        print(stage_5)
    if death == 6:
        print(stage_6)
        print("You Lose!")
        break
if random_word == placeholder:
    print("You win!")
          
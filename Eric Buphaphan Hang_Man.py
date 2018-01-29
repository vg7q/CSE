#This is a guid of how to make Hang_Man
"""
1.Make a word bank - 10 items
2.Select a random item to guess
3.Hide the word (use *)
4.Reveal Letters based on input
5.Creats win and lose conditions
"""
import random
import string
alphabet = string.ascii_lowercase
word_bank = ['Gum', 'Flame', 'Yami', 'Bari', 'Gura', 'Goro', 'light', 'ice', 'venom', 'ope']
word = list(random.choice(word_bank))
guesses_left = 10
regular_word = random.choice(word_bank).lower()
guesses = []
hidden_word = ('*' * len(regular_word))
print(hidden_word)

while guesses_left > 0:
    print(guesses)
    print("the word is %s letters long" % len(regular_word))
    player_guess = input("take a guess >_").lower()
    guesses.append(player_guess)
    if player_guess not in regular_word:

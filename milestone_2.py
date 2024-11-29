#%%
import random

word_list = ["banana", "raspberry", "blueberry", "watermelon", "mangosteen"]

print(word_list)
# %%

word = random.choice(word_list)

print(word)
# %%
guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
  print("Good guess!")
else:
  print("Oops! That is not a valid input." )
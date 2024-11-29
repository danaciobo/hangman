#%%
import random

word_list = ["banana", "raspberry", "blueberry", "watermelon", "mangosteen"]

def get_random_word(list):
  print(random.choice(list))
  return random.choice(list)
# %%
def is_letter():
  while True:
    guess = input("Please enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
      print("Good guess!")
      return guess
    else:
     print("Oops! That is not a valid input." )

get_random_word(word_list)
is_letter()
#%%
import random

word_list = ["banana", "raspberry", "blueberry", "watermelon", "mangosteen"]

def get_random_word(list):
  print(random.choice(list))
  return random.choice(list)
# %%
random_word = get_random_word(word_list)

def ask_for_input():

  guess = input("Please enter a single letter: ")
  while True:
    if len(guess) == 1 and guess.isalpha():
      print(f"{guess} is a valid letter!")
      check_guess(guess, random_word)
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character." )


def check_guess (guess, random_word):
  if guess.lower() in random_word:
    print(f"Good guess! {guess} is in the word.")
  else:
    print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()

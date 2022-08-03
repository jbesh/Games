# Wordle Solver by Jared Beshgetoorian
# words.txt file from https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b

potential = [] #potential words

file = open("words.txt", "r")
words = file.read().splitlines()
file.close()

not_included = input("Letters not included (gray, no spaces or commas, ex. sorbcjt): ")
included = input("Letters included (yellow and green, no spaces or commas, ex. ael): ")
exact = input("Exact order known (green, 0 for grey or yellow, ex. a00le): ")

for word in words: #all valid wordle words
  for letter in not_included: #letter that is not in the wordle word
    if letter in word:
      break
  else:
    for letter in included: #letter that is in the wordle word
      if letter not in word:
        break
    else:
      index = 0
      for letter in exact: #compare letter of potential word to letter of actual word using index
        if letter != 0: #skip if we do not know it
          if letter is not exact[index]:
            break
        index += 1
      else:
        potential.append(word)

print(potential) #print the potential wordle words based on your parameters
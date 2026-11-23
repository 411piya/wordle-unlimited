import random
file1 = open("Wordle.txt","r")
text = file1.read()
word = random.choice(text.split())
my_word = list(word)
my_word.pop(6)
my_word.pop(0)
my_word.pop(5)
file1.close()
line_split = ["_","_","_","_","_"]
guess = " "
guess_split = []
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
print(my_word)
a = 0
guesses = 0
win = False
def hint():
    global my_word
    global line_split
    global guesses
    global guess_split
    global win
    if guesses == 5 and win == False:
        for i in range(len(line_split)):
            if line_split[i] == "_":
                print(f"This is your hint since you kinda suck. The letter {my_word[i]} is in the {i + 1} position ")
                guesses = 0
                break
check_right = 0
print("This is a game of modified wordle. Guess the 5 letter word using input")
while guess_split != my_word:
    line_split = ["_","_","_","_","_"]
    guess_split = []
    while True:
        if check_right == 0:
            guess = input("take a guess.")
        else:
            guess = input("Wrong type of input. must be a string and 5 letters long ")
        if type(guess) == str and len(guess) == 5:
            break
        check_right += 1
    guesses += 1
    for i in guess:
        guess_split.append(i)

    for i in range(len(guess_split)):
        if guess_split[i] == my_word[i]:
            line_split.pop(i)
            line_split.insert(i,my_word[i])
            print(line_split)
        else:
            for j in range(len(guess_split)-1):
                if guess_split[i] == my_word[j]:
                    print(guess_split[i],"is in the word but it is not in the right place")
                    guess_split.pop(i)
                    guess_split.insert(i,"_")
    hint()
print("YOU WINN YAYYY")
win = True
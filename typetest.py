import random
import time

#filename="/usr/share/dict/words"
filename="./wordlist.txt"
with open(filename) as f:
    words = f.readlines()

# remove whitespace
words = [word.strip() for word in words]
# remove words that are all caps, but keep words with only the first letter capitalized
words = [word for word in words if not word.isupper()]

print("Welcome to the typing test!")
print("You will type n words as fast as you can.")
choice=input("Choose a difficulty: (1) Easy (2) Medium (3) Hard (4) Insane (5) Random:")

numwords=input("Choose a word count: (1) 10 (2) 20 (3) 50 (4) 100: ")

if numwords == "1":
    numwords = 10
elif numwords == "2":
    numwords = 20
elif numwords == "3":
    numwords = 50
elif numwords == "4":
    numwords = 100
else:
    print("invalid choice, as punishment 1000 words it is!")
    numwords = 1000
if choice == "5":
    choice = random.randint(1,5)
if choice=="1":
    words = [word for word in words if "'" not in word and word.islower() and not any(char.isdigit() for char in word) and len(word) <= 5]
elif choice=="2":
    # remove all words longer than 7 characters
    words = [word for word in words if "'" not in word and word.islower() and not any(char.isdigit() for char in word) and len(word) <= 7]
elif choice=="3":
    words = [word for word in words if word.islower() and "'" not in word]

random_words = random.sample(words, numwords)
print("Type the following words as fast as you can!")
print("Press enter to start")
start = input()
for i in random_words:
    print(i, end=" ")
print()
start_time = time.time()
end = input()
end_time = time.time()
total_time = end_time - start_time
if total_time > 3:
    total_time=total_time-1.5
print(f"Total time: {total_time} seconds")

# now calculate accuracy and characters per minute
# first, get the words the user typed
user_words = end.split()
# now, compare the user's words to the random words
correct = 0
for i in range(len(user_words)):
    if user_words[i] == random_words[i]:
        correct += 1
accuracy = correct / len(random_words) * 100
print(f"Accuracy: {accuracy}%")
# now calculate characters per minute
# first, get the total number of characters
total_chars = len(end)
# now calculate characters per minute
chars_per_minute = total_chars / total_time * 60
# now calculate words per minute
words_per_minute = len(random_words) / total_time * 60 *accuracy/100
print(f"Characters per minute: {chars_per_minute}")
print(f"Words per minute(accuracy adjusted): {words_per_minute}")
words_per_minute = len(random_words) / total_time * 60
print(f"Words per minute(unadjusted): {words_per_minute}")
# print incorrect words the user typed in bold
print("Incorrect words:")
for i in range(len(user_words)):
    if user_words[i] != random_words[i]:
        print(random_words[i], end=" ")
print()

print("Hello World")

userInput = "Enter your username"

print (userInput)

vowels="AEIOUaeiou"

displayVowels= ""

displayConsonants=""

for letter in userInput:
    print ("letter:" + letter)
    if letter in vowels:
        displayVowels= displayVowels + letter
    else:
        displayConsonants = displayConsonants + letter

print ("vowels:" + displayVowels)
print ("consonants: " + displayConsonants)
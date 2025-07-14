#Task 1: Hello
def hello():
    return "Hello!"

#Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"
greet("DaiGianna")

#Task 3: Calculator
def calc(value1, value2, operation="multiply"):
    try:
        value1=float(value1)
        value2=float(value2)
    except ValueError:
        return "You can't multiply those values!"

    if operation == "add":
        result = value1+value2
    elif operation == "subtract":
        result = value1-value2
    elif operation == "int_divide":
        if value2 == 0:
            result = "You can't divide by 0!"
            return result
        result = value1//value2
    elif operation == "divide":
        if value2 == 0:
            result = "You can't divide by 0!"
            return result
        result = value1/value2
    elif operation == "modulo":
        if value2 == 0:
            result = "You can't divide by 0!"
            return result
        result = value1%value2
    elif operation == "multiply":
        result = value1*value2
    elif operation == "power":
        result = value1**value2
    else:
        result = "Error"
    return result


#Task 4: Data Type Conversion
def data_type_conversion(value, dataType):
    if dataType == "float":
        try:
            value = float(value)
        except ValueError:
            return f"You can't convert {value} into a {dataType}."
    elif dataType == "str":
        value = str(value)
    elif dataType == "int":
        try:
            value = int(value)
        except ValueError:
            return f"You can't convert {value} into a {dataType}."
    else:
        value = f"You can't convert {value} into a {dataType}."
    return value

#Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args)/len(args)
    except (ValueError, TypeError, ZeroDivisionError) as error:
        return "Invalid data was provided."
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

#Task 6: Use a For Loop with a Range
def repeat(string1, count1):
    newString = ""
    for i in range(count1):
        newString += string1
    return newString

#Task 7: Student Scores, Using **kwargs
def student_scores(bestOrMean, **kwargs):
    mean = sum(kwargs.values())/len(kwargs.values())
    highestScore = max(kwargs.values())
    bestInList = [key for key, val in kwargs.items() if val == highestScore]
    best = ''.join(bestInList)
    if bestOrMean == "mean":
        return mean
    if bestOrMean == "best":
        return best
    
#Task 8: Titleize, with String and List Operations
def titleize(string1):
    titleizedList = []
    littleWords = ["a","an", "on", "the", "of", "and", "is", "in"]
    splitString = string1.split(" ")

    for i, word in enumerate(splitString):
        word = word.lower()
        if i == 0:
            word = word.capitalize()
            titleizedList.append(word)
        elif i == len(splitString)-1:
            word = word.capitalize()
            titleizedList.append(word)
        elif word in littleWords:
            titleizedList.append(word)
        else:
            word = word.capitalize()
            titleizedList.append(word)
    titleizedString = " ".join(titleizedList)
        
    return titleizedString

#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    normalSecret = secret.lower()
    normalGuess = guess.lower()
    guessList = []
    for character in normalSecret:
        if character in normalGuess:
            guessList.append(character)
        elif character not in normalGuess:
            guessList.append("_")
    guessString = "".join(guessList)
    return guessString

#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    pigList = []
    vowel = ["a", "e", "i", "o", "u"]
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    splitSentence = sentence.split(" ")
    for word in splitSentence:
        wordConsonants = []
        if word[0:2] == "qu":
            word = word.replace("qu","")
            word = word + "qu"
            word = word + "ay"
            pigList.append(word)
        elif word[0] in vowel:
            word = word + "ay"
            pigList.append(word)
        else:
            firstVowelIndex = 0
            for i, character in enumerate(word):
                if i + 1 < len(word) and word[i:i+2] == "qu":
                    firstVowelIndex = i +2
                    break
                elif character in vowel:
                    firstVowelIndex = i
                    break
            leadingConsonants = word[0:firstVowelIndex]
            restOfWord = word[firstVowelIndex:]
            convertedWord = restOfWord + leadingConsonants + "ay"
            pigList.append(convertedWord)
    pigSentence = " ".join(pigList)

    return pigSentence




#Task 8: Titleize, with String and List Operations
def titleize(string1):
    titleizedList = []
    littleWords = ["a","an", "on", "the", "of", "and", "is", "in"]
    splitString = string1.split(" ")

    for i, word in enumerate(splitString):
        word = word.lower()
        if i == 0:
            word = word.capitalize()
            titleizedList.append(word)
        elif i == len(splitString)-1:
            word = word.capitalize()
            titleizedList.append(word)
        elif word in littleWords:
            titleizedList.append(word)
        else:
            word = word.capitalize()
            titleizedList.append(word)
    titleizedString = " ".join(titleizedList)
        
    return titleizedString
import copy

DEBUG = True
global END
END = False

class Door:
    def __init__(self, size, words):
        self.size = size
        self.words = words

    def print(self):
        print("Size:", self.size, " \nWords:", self.words)

def readFile(filename):
    file = open(fileName, "r")
    lines = []
    for line in file.readlines():
        lines.append(line.rstrip('\n'))
    file.close()
    return lines

def parseInput(lines):
    i = 0
    length = int(lines[i])
    doors = []
    for doorIndex in range(length):
        i += 1
        numberOfWords = int(lines[i])
        words = []
        for wordIndex in range(numberOfWords):
            i += 1
            words.append(lines[i])
        door = Door(numberOfWords, words)
        doors.append(door)
    return doors

def firstChar(text):
    return text[0]

def lastChar(text):
    return text[-1]

def wordFollows(text, word):
    return lastChar(text) == firstChar(word)

def wordPrecedes(text, word):
    return lastChar(word) == firstChar(text)

def addWord2String(text, word):
    if wordFollows(text, word):
        text = text + word
    elif  wordPrecedes(text, word):
        text = word + text
    return text

def words2add(text, words):
    wordsToAdd = []
    for word in words:
        if wordPrecedes(text, word) or wordFollows(text, word):
            wordsToAdd.append(word)
    return wordsToAdd

def solve(text, words):
    global END
    if END:
        return False

    # vsechny pridany
    if len(words) == 0:
        if DEBUG:
            print(text)
        return True
    
    words = mergeTrivial(words)

    if solitaryExist(words):
        if DEBUG:
            print("Soliter!", text, words)
        END = True
        return False

    # zadny nelze pridat
    wordsToAdd = words2add(text, words)
    if len(wordsToAdd) == 0:
        if DEBUG:
            print(text, "to go:", len(words))
            print(words)
            print(allStarts(words))
            print(allEnds(words))
        return False
    
    text = firstChar(text) + lastChar(text)
    for word in wordsToAdd:
        textCopy = copy.deepcopy(text)
        wordsCopy = copy.deepcopy(words)
        wordsCopy.remove(word)
        textCopy = addWord2String(textCopy, word)
        if solve(textCopy, wordsCopy):
            return True
        else:
            continue
    return False

def shortenWords(words):
    shorts = []
    for word in words:
        short = firstChar(word) + lastChar(word)
        shorts.append(short)
    return shorts

def allStarts(words):
    start = {}
    for word in words:
        char = firstChar(word)
        if char in start.keys():
            start[char] = start[char]+1
        else:
            start[char] = 1
    return start

def allEnds(words):
    ends = {}
    for word in words:
        char = lastChar(word)
        if char in ends.keys():
            ends[char] = ends[char]+1
        else:
            ends[char] = 1
    return ends

def mergeWordsWithLetter(words, char):
    start = ""
    end = ""
    for word in words:
        if firstChar(word) == char:
            end = word
            words.remove(word)
            break

    for word in words:
        if lastChar(word) == char:
            start = word
            words.remove(word)
            break

    words.append(start+end)
    return words

def mergeTrivial(words):
    singleLetters = []
    dictionary = allStarts(words)
    for char in dictionary:
        if dictionary[char] == 1:
            singleLetters.append(char)
    if len(singleLetters) == 0:
        return words
    
    if 0 and DEBUG:
        print("Singles:", len(singleLetters))
    dictionary = allEnds(words)
    for char in singleLetters:
        if char in dictionary.keys():
            words = mergeWordsWithLetter(words, char)
    return words

def solitaryExist(words):
    starts = allStarts(words).keys()
    ends = allEnds(words).keys()
    if 0 and DEBUG:
        print("Starts:", starts)
        print("Ends:", ends)
    for word in words:
        if not lastChar(word) in starts and not firstChar(word) in ends:
            return True
    return False

def isValidWordFootballSequnce(words):
    words = shortenWords(words)
    if DEBUG:
        print(words)

    text = words.pop(0)
    return solve(text, words)

if __name__ == '__main__':
    #fileName = "positive.txt"
    fileName = "large.txt"
    #fileName = "small.txt"
    outputName = "vysledky.txt"
    output = open(outputName, "w")
    lines = readFile(fileName)
    doors = parseInput(lines)
    for door in doors:
        #if DEBUG:
        #    door.print()
        END = False
        valid = isValidWordFootballSequnce(door.words)
        print(door.size, valid)
        output.write(str(door.size))
        output.write(" ")
        output.write(str(valid))
        output.write("\n")
    output.close()

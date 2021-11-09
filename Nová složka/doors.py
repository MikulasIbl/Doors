import copy

class Door():
    def __init__ (self, doors_number, words):
        self.doors_number= doors_number
        self.words = words

    def print(self):
        print("DoorNumber:", self.doors_number, " \nWords:", self.words)

def SplitEveryThink (lines):
    i = 0
    test_number = int(lines[i])
    doors = []
    for j in range(test_number):
        i += 1
        doors_number = int(lines[i])
        words = []
        for k in range(doors_number):
            i += 1
            words.append(lines[i])
        door = Door(doors_number, words)
        doors.append(door)
    return doors

def solve(words):
    words = FirstLast(words)
    
    return True

def FirstLast(words):
    new_words = []
    for word in words:
        word = word[0] + word[-1]
        new_words.append(word)
    return new_words

if __name__ == '__main__':
    file_out = open("vysledky.txt", "w")
    file_in = "small.txt"
    #file_in = "large.txt"
    #file_in = "positive.txt"
    #file_in = "negative.txt"
    file = open(file_in, 'r',  encoding='utf-8')
    lines = file.read().split('\n')
    file.close()
    doors = SplitEveryThink(lines)
    for door in doors:
        #door.print()
        file_out.write(str(door.doors_number))
        if solve(door.words):
            file_out.write(" True\n")
        else:
            file_out.write(" False\n")
    file_out.close()
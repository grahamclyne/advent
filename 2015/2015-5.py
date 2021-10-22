def isVowel(x):
    if x in ['a', 'e', 'i', 'o', 'u']:
        return True

def containsDouble(x):
    for i in range(0, len(x)-1):
        if(x[i] == x[i+1]):
            print(x)
            return False
    return True

def isNiceString(string):
    vowels = len(list(filter(lambda x: isVowel(x), string)))
    if ("ab" in string) or ("cd" in string) or ('pq' in string) or ('xy' in string) or vowels < 3 or containsDouble(string):
        return False
    else: 
        return True

def repeatRule(string):
    for i in range(len(string)-2):
        if(string[i] == string[i+2]):
            return True
    return False


def overLapRule(string):
    print(string)
    for first_letter in range(len(string)):
        pair = string[first_letter:first_letter+2]
        remaining = string[first_letter+2:len(string)]
        print(pair, remaining)
        if pair in remaining:
            print(string)
            return True
    return False


def isNiceString2(string):
    if repeatRule(string) and overLapRule(string):
        return True
    else:
        return False

file = open('input5')
input = file.readlines()
trimmed = list(map(lambda x: x.rstrip(),input))
nice_strings = list(filter(lambda x: isNiceString2(x) == True, trimmed))
print(len(nice_strings))

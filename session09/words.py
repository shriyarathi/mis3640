fin = open('session09/words.txt')
# line = fin.readline()

# print(line)

# line = fin.readline()
# word = line.strip
# print(word)


#for line in fin: 
 #   word = line.strip()
#  print(word)



def read_long_words():
    """
    prints only the words with more than 20 characters
    """

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

    


read_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
for line in word:
            if line.find('e') == -1:
                print line
 



print(has_no_e('Babson'))
print(has_no_e('College'))


def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    pass


print(avoids('Babson', 'ab'))
print(avoids('College', 'ab'))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
for letter in word:
        if letter not in available:
            return False
    return True


print(uses_only('Babson', 'aBbsonxyz'))
print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
   for word in required:
        if letter not in word:
            return False
    return True


print(uses_all('Babson', 'abs'))
print(uses_all('college', 'abs'))


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
 before = word[0]
    for letter in word:
        if letter < before:
            return False
    return True


print(is_abecedarian('abs'))
print(is_abecedarian('college'))

#2.1 & 2.2 

def is_abecedarian(word):
    if len(word) <= 1:
        return True
        #If the legth of the word is less than one, there is no adjacent letter to compare to
    if word[0] > word[1]:
        return False


def is_abecedarian(word):
    c = 0
    while c < len(word)-1:
        if word[c+1] < word[c]:
            return False
        c == C+1 
    return True


fin = open('session09/words.txt')

def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """

print(uses_all('Babson', 'aeoiu'))
print(uses_all('Babesonious', 'aeoiu' ))

def find_words_using_all_vowels():
    fin = open('session09/words.txt')  

    counter = 0
    for line in fin:
        counter_total += 1
        word = line.strip()
        if uses_all(word, 'aeiou'):
            print(word)
            counter += 1
    return counter

    print('The number of words that uses all the vowels', find_words_using_all_vowels())


    def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    before = word[0]
    for letter in word:
        if letter < before:
            return False
        before = letter
    return True


print(is_abecedarian('abs'))
print(is_abecedarian('college'))


def find_abecedarian_words():
    fin = open('session09/words.txt')
    counter = 0 
    for line in fin:
        counter +=1
        word = line.strip()
        if letter < before:
            return False
        before = letter
    return True

print (find_abecedarian_words())
        


    return counter 




def find_abecedarian_words():
    fin = open('session09/words.txt')
    counter = 0 
    current_longest_word = ''
    for line in fin:
            word = line.strip()
        if is_abecedarian(word):
            # print (word)
            counter +=1
            if len(word)> len(current_longest_word):
                current_longest_word = word 
        
    return counter, current_longest_word


print(find_abecedarian_words())



















           
   



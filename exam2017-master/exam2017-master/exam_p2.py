import string

### DO NOT MODIFY THIS FUNCTION ###
def load_wordlist(file_name):
    '''
    '''
    print('Loading word list from file...')
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


### DO NOT MODIFY THIS FUNCTION ###
def is_a_valid_word(word_list, word):
    '''    
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### DO NOT MODIFY THIS FUNCTION ###
def get_joke_string():
    """
    Returns: an article in encrypted text.
    """
    f = open("joke.txt", "r", encoding = 'utf-8') #can't read the apostrophe without this
    joke = str(f.read())
    f.close()
    return joke

WORDLIST_FILENAME = 'words.txt'


class Text(object):

    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Text object
        '''
        self.text = text
        self.valid_words = load_wordlist(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_text(self):
        '''
        Returns: self.text
        '''
        return self.text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]


    ### YOU NEED TO MODIFY THIS METHOD ###
    def create_moved_dict(self, move):
        '''
        Creates a dictionary that maps every letter to a
        character moved down the alphabet by the input move. 

        move: an integer, 0 <= move < 26

        Returns: a dictionary

        Example: an_instance_of_Text.create_moved_dict(2) would generate
        {'a': 'c', 'b': 'd', 'c':'e', ...}  
        '''
        self.alphabetLower = "abcdefghijklmnopqrstuvwxyz"
        self.alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.move_dict = {}

        for char in self.alphabet.Lower:
            self.move_index = self.alphabetUpper.index(char) = move 
            self.move_dict[char] = self.move_dict[self.alphabetUpper]


    ### YOU NEED TO MODIFY THIS METHOD ###
    def apply_move(self, move):
        '''
        Applies the cipher to self.text with the input move       

        move: an integer, 0 <= move < 26

        Returns: the text (string) in which every character is moved
             down the alphabet by the input move
        '''
        pass 

        move_text = ''

        for c in slef.text:
            if c in string...:
                c = move_dict[c]
            move_text +=c 


class PlainText(Text):

    ### YOU NEED TO MODIFY THIS METHOD ###
    def __init__(self, text, move):
        '''
        Initializes a PlainText object        

        text: a string
        move: an integer

        A PlainText object inherits from Text and has five attributes:
            self.text (string, determined by input text)
            self.valid_words (list, determined using helper function load_wordlist)
            self.move (integer, determined by input move)
            self.encrypting_dict (dictionary, built using move)
            self.encrypted_text (string, created using move)

        Note: you must use the parent class constructor(__init__ function) 
        so less code is repeated
        '''
        pass  # delete this line and replace with your code here


    ### YOU NEED TO MODIFY THIS METHOD ###
    def get_move(self):
        '''
        Used to safely access self.move outside of the class

        Returns: self.move
        '''
        pass  # delete this line and replace with your code here


    ### YOU NEED TO MODIFY THIS METHOD ###
    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        pass  # delete this line and replace with your code here


    ### YOU NEED TO MODIFY THIS METHOD ###
    def get_encrypted_text(self):
        '''
        Used to safely access self.encrypted_text outside of the class

        Returns: self.encrypted_text
        '''
        pass  # delete this line and replace with your code here


    ### YOU NEED TO MODIFY THIS METHOD ###
    def change_move(self, move):
        '''
        Changes self.move of the PlainText and updates other 
        attributes determined by move (ie. self.encrypting_dict and 
        encrypted_text).

        move: an integer, 0 <= move < 26

        Returns: nothing
        '''
        pass  # delete this line and replace with your code here


class CipherText(Text):

    
    ### YOU NEED TO MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a CipherText object

        text: a string

        a CipherText object has two attributes:
            self.text (string, determined by input text)
            self.valid_words (list, determined using helper function load_wordlist)
        '''
        pass  # delete this line and replace with your code here


    ### YOU NEED TO MODIFY THIS METHOD ###
    def decrypt_text(self):
        '''
        Decrypt self.text by trying every possible move value
        and find the "best" one. We will define "best" as the move that
        creates the maximum number of real words when we use apply_move(move)
        on the text. If s is the original move value used to encrypt
        the text, then we would expect 26 - s to be the best move value 
        for decrypting it.

        Returns: a tuple of the best move value used to decrypt the text
        and the decrypted  text using that move value. Check out the
        test case in main function below.

        '''
        pass  # delete this line and replace with your code here



### DO NOT MODIFY THIS FUNCTION ###
def decrypt_joke():
    joke = CipherText(get_joke_string())
    return joke.decrypt_text()


### DO NOT MODIFY THIS FUNCTION ###
def main():
    # Example test case (PlainText)
    plaintext = PlainText('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_encrypted_text())

    # Example test case (CipherText)
    ciphertext = CipherText('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_text())

    print(decrypt_joke())

if __name__ == '__main__':
    main()

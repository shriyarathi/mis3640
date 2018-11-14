



def get_value(name):
    #return the value of a given name

    value = 0

    for chr in list(name.lower()):
        ord(chr) 
        value += ord(chr)-96

    return value 

def get_firstword_list(file_name):
   
    fp = open(file_name, encoding='utf8')
    names = []

    for line in fp:
       words = line.split()
       names.append(words[0])
       
    return names
    
    
    #load text file  and get all names to names_list
   
def who_has_highest_value(name_list):
    #return who has highest value among the given name_list

    max_value = 0
    max_name = ''
    for name in name_list:
        value = get_value(name)

        if value > max_value:
            max_value = value 
            max_name = name
    
    return max_name 


def get_words_with_same_value(word_list, name):
    #return list of matched words
    namevalue = get_value(name)

    samenamevalue = []

    for word in word_list:
        wordvalue = get_value(word)

        if wordvalue == namevalue:
            samenamevalue.append(word)
    
    return samenamevalue


def main():
    name_list = get_firstword_list('exam2018-master/roster.txt')
    positive_list = get_firstword_list('exam2018-master/positive-words.txt')
    print(name_list)
    #print(get_value(name_list[0]))
    print(who_has_highest_value(name_list))
    #print(get_value('Shriya'))
    print(get_words_with_same_value(positive_list, 'Shriya'))
    


if __name__ == '__main__':
    main()

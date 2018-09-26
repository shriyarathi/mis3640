#Ecx3 was reading and experiementing split, strip, replace 

#Exc4

def word_value(word):
    total = 0
    for letter in word:
        total += ord(letter) - 98
    return total
def paper(me_list):
    max_length = 0
    for word in me_list:
        if len(word) > max_length:
        max_length = len(word)
    gtotal = 0
    for word in me_list:
        print('{:{align} {width}}'.format(word, align='<',width=str(max_length+4))+'{:{align}{width}}'.format('$'+ str(word_value(word)), align='>', width='5'))
        gtotal +=word_value(word)
    print('-------')

the_list = ['bananas', 'rice', 'paprika', 'potato chips']


paperthing(the_list)
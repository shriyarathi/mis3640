def histogram(s):
    d = dict()
    for c in s: #for each charcter in string 
        if c not in d: # if charcter not in keys
            d[c] = 1
        else:
            d[c] += 1 #add 1 if the key exists in the dictionary
    return d

h = histogram('Bookkeeper')
print(h)

d = {'a' : 3}
d.get('a')
 #will give you 3 


 # insert for a list 

 class_roster.insert(-1,'word')  #-1 is the spot you want to add it to 
 # remove value
  class_roster.remove('word')

  #remove names starting with letter A

  # wrong

  for name in class_roster:
      if name[0] == 'A':
          class_roster.remove(name)

# right 

roster_copy = class roster[:]
for name in class_roster:
      if name[0] != 

# assign a random grade 90-100 to each student, 1-10 for names start with A

# 1. make a dictionary 
grades = {}

import random
for name in roster in class_roster:
    if name [0] == "A":
        grades[name] = random.rnadint(1,10)
    grades[name] = random.randint(90,100)


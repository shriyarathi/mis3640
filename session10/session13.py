import random

class_roster = {'Jonathan Beltran': 0, 'Allison Fernandez': 1, 'Siddhanth Goyal': 0, 'Jingyu He': 0, 'Defne Ikiz': 0, 'Zirui Jiao': 0, 'Pranjal Joshi': 0, 'Dong Hyun Kim': 0, 'Ha Min Ko': 0, 'Kyle Lawson': 0, 'Christine Lee': 1, 'Connie Li': 1,
               'Qinyi Li': 0, 'Matthew Michalke': 0, 'Ho Wang Alastair Ng': 1, 'Jonghyun Park': 0, 'Alden Pexton': 2, 'Shriya Rathi': 2, 'Waylon Ryan': 1, 'Christian Thompson': 3, 'Angela Tsung': 2, 'Aaron Wendell': 0, 'Sarah Zazyczny': 0, 'Shiyue (Shirley) Zong': 0}
            
        min_times = min(class_roster.values())
        print(min_times)

        pool = []   #making a new list of minumum values 

        for name in class_roster:
            if class_roster[name] == min_times:  # names thhat have been called a minumum amount of times
                pool.append(name)  #adding name to the pool list

       

        class_roster['Dong Hyun Kim'] += 1 # this adds 1 to this persons count 

        print(class_roster)
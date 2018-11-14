import pickle
t1 = [1, 2, 3]

f = open('save.p', 'wb')
s = pickle.dump(t1,f)
f.close()

t2 = pickle.loads(open('save.p', 'rb'))
print(t2)
def replace_even(data):
   for i in range(0,len(data),2):
       data[i] = 0

ONE_TEN = [1,2,3,4,5,6,7,8,9,10]
replace_even(ONE_TEN)
print(ONE_TEN)

# Expected output:
# [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]


def remove_middle(data):
        if len(data) % 2 == 0:
            middle1 = int(len(data)/2)
            middle2 = int(len(data)/2-1)
            del data[middle1]
            del data[middle2]
        else:
            middle = data(int(len(data)/2))
            del data[middle]

# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# remove_middle(ONE_TEN)
print(ONE_TEN)

# # Expected output:
# [1, 2, 3, 4, 7, 8, 9, 10]

def insert_integer(data, number):

    for n in range(0, len(data)):
       if (data[n] >= number):
           data.insert(n, number)
           break
    return data 
bisect.insort(data, 2015)

print(new_data)

# Expected output:
# [1, 3, 40, 75, 90, 2000, 2001, 2015, 2016]

def print_hist(data):
   for item in sorted(data):
    print(item,'*'*data[item])

letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
print_hist(letter_counts)
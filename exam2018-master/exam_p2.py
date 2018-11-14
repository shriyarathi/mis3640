import csv


def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)

        return (your_list)
  
    
def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """

    file_name = 'exam2018-master/babynames/yob' + str(year) + '.txt'

    nameslist = process_file(file_name) 

    totalbirths = 0

    for name in nameslist:
        totalbirths += int(name[2])

    return totalbirths
            

def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    totalb = total_births(year) 

    file_name = 'exam2018-master/babynames/yob' + str(year) + '.txt'

    nameslist = process_file(file_name) 

    for namegenbirth in nameslist:
        if namegenbirth[0] == name and namegenbirth[1] == gender:
            return float(namegenbirth[2])/float(totalb)

def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    maxprop = float(0) 
    maxyear = 0

    for year in range(1880, 2010):
        prop = proportion(name, gender, year)

        if prop > maxprop:
            prop = maxprop
            maxyear = year 

    return year 



def main():
    #print(process_file('exam2018-master/babynames/yob1880.txt'))
    print(total_births(1981))
    print(proportion('Sarah', 'F', 1981))
    print(highest_year('Sarah', 'F'))
    



if __name__ == '__main__':
    main()

from BabsonPerson import BabsonPerson
from Person import Person


class Professor(BabsonPerson):
    
    def __init__(self, name, salary,age):
        BabsonPerson.__init__(self, name)
        self.salary = salary
        self.age = age

    def getClass(self):
        return self.salary

    def speak(self, utterance):
        return BabsonPerson.speak(self, " Hi, " + utterance)


class Grad(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)


def main():
    s1 = UG('Christian Thompson', 2019)
    s2 = UG('Sarah Zazyczny', 2019)
    s3 = UG('Zirui Jiao', 2020)
    s4 = Grad('Matt Damon')

    studentList = [s1, s2, s3, s4]

    print(s1)

    print(s1.getClass())

    print(s1.speak('where is the quiz?'))

    print(s2.speak('I have no clue!'))

    print(s4.speak('I am not sure why I am here.'))

    # print(isStudent(s1))

    # p1 = Person('Taylor Swift')
    # print(isStudent(p1))

if __name__ == '__main__':
    main()
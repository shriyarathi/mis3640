class Exercise:
    """
    Represents the list of exercises.

    attributes: muscle, name, calorie
    """
 
    def __init__(self, muscle, calorie):
        """
        method that initializes some attributes. 
        One of the attributes has to be an empty list.
        """
        self.muscle = muscle
        self.exercise = []    # creates a new empty list for each exer
        self.calorie = calorie
    def add_exercise(self, exercise):
        """
        Some other methods that reasonably represent the thing's actions, 
        inclduing one method that takes an object of any type and adds it to the attribute of type list.

        """
        self.exercises.append(exercise)
            
    def __str__(self):
        """
        return string representation 
        """
        return 'This is my first exercise{} that will burn {}'.format(self.muscle, self.calorie)

    def __add__(self, other):
        """
        A special method that overloads the one type of operators.

        """

        fullbody = Exercise(self.muscle + other.muscle)
        return fullbody
    

    
    

core = Exercise('Core')
upper = Exercise('Upper')
lower = Exercise('Lower')

core.add_exercise('Crunch')
upper.add_exercise('Push Up')
lower.add_exercise('Squat')

# core.exercise
# upper.exercise
# lower.exercise



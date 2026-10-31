# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth = date(2007, 2, 3)):
        """
        Initializes a new Person object, given values for a name and date of birth.
        """
        if (not (isinstance(name, str) and isinstance(birth, date))):
            raise TypeError("One or more fields are not of the correct datatype.")
        elif (len(name) == 0):
            raise ValueError("You must provide a non-empty name.")
        else:
            self.name = name
            self.birth = birth

    def initials(self):
        """
        Returns a shortened version of the Person's name, 
        where the first letter in every component is capitalized and joined with no delimiter.
        """
        components = self.name.split(" ")

        initials = "".join([c[0].upper() for c in components])
        return initials
    
    def is_birthday(self):
        """
        Checks if today is the Person's birthday (the day and month attributes of both are equal).
        """
        dateToday = date.today()

        isDay = dateToday.day == self.birth.day
        isMonth = dateToday.month == self.birth.month

        return isDay and isMonth
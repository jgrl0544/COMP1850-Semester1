# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, dob = date(2007, 2, 3)):
        """
        Initializes a new Person object, given values for a name and date of birth.
        """
        if (not (isinstance(name, str) and isinstance(dob, date))):
            raise TypeError("One or more fields are not of the correct datatype.")
        elif (len(name) == 0):
            raise ValueError("You must provide a non-empty name.")
        else:
            self.name = name
            self.dob = dob

    def initials(self):
        """
        Returns a shortened version of the Person's name, 
        where the first letter in every component is capitalized and joined with no delimiter.
        """
        components = self.name.split(" ")

        initials = "".join([c[0].upper() for c in components])
        return initials
    
    def isBirthday(self):
        """
        Checks if today is the Person's birthday (the day and month attributes of both are equal).
        """
        dateToday = date.today()

        isDay = dateToday.day == self.dob.day
        isMonth = dateToday.month == self.dob.month

        return isDay and isMonth
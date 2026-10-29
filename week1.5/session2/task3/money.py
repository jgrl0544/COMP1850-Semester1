# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """

        if not (isinstance(pounds, int) and isinstance(pence, int)):
            raise TypeError("Only integer values can be supplied to Money objects.")

        if not (pounds >= 0 and 99 >= pence >= 0):
            raise ValueError("Invalid values have been supplied to this Money object.")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        return f"£{self.pounds}.{self.pence:02}"

    def __add__(self, other : Money):
        """
        Adds this Money to another Money, returning the total.
        """
        PENCE_PER_POUND = 100

        totalPence = self.pence + other.pence
        remainingPence = totalPence % PENCE_PER_POUND 
        poundsFromPence = totalPence // PENCE_PER_POUND
        totalPounds = self.pounds + other.pounds + poundsFromPence

        return Money(totalPounds, remainingPence)

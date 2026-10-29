# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        self.data.clear()
        with open(filename, "r") as f:
            for line in f:
                line = line.strip("\n")
                self.data.append(line)

    def __len__(self):
        """
        Returns the size of this Dataset.
        """

        return len(self.data)

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """

        return self.data[index]

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        
        numData = [float(x) for x in self.data]
        return sum(numData) / self.__len__()

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        
        numData = [float(x) for x in self.data]
        sortedData = sorted(numData)
        print(sortedData)
        lenData = self.__len__()

        if (lenData % 2 == 1):
            index = round(lenData / 2)
            return sortedData[index]
        
        else: 
            smallerIndex = round(lenData / 2) - 1
            largerIndex = round(lenData / 2)
            total = sortedData[smallerIndex] + sortedData[largerIndex]
            return total / 2            

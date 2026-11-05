from image import Image

class LUT:
    """
    A generic Lookup Table.
    """

    def __init__(self, data : list):
        """
        Creates a Lookup Table.
        """
        self._data = data

    def __getitem__(self, key):
        """
        Returns the value represented by this key in this table.
        """
        return self._data[key]

    def display(self):
        for i in range(len(self._data)):
            print(f"Index {i} has value {self[i]}")

    def apply(self, image : Image):
        """
        Applies the LUT to a copy of the image provided.
        """
        copy = image.copy()
        self.apply_in_place(copy)
        return copy

    def apply_in_place(self, image):
        """
        Directly applies the LUT to the image provided.    
        """
        for i in range(len(image.pixels)):
            val = image.pixels[i]
            image.pixels[i] = self[val]

class InverterLUT(LUT):
    """
    A Lookup Table where each index represents the inverted value (length - index). 
    """

    def __init__(self, elementSize):
        """
        Creates an Inverter LUT. 
        """
        super().__init__(self._create_list(elementSize))

    def _create_list(self, length):
        return [length - x for x in list(range(length))]

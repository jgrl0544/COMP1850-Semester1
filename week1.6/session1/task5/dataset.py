# Week 1.6, Session 1: Task 5

from datetime import datetime

from feed import QuakeFeed
from quake import Quake


class QuakeDatasetError(Exception):
    """
    An exception type for errors involving QuakeDataset.
    """


class QuakeDataset:
    """
    An earthquake dataset obtained from a USGS data feed.
    """

    def __init__(self, feed):
        """
        Creates an empty dataset, linked to a specific data feed.
        """
        if not isinstance(feed, QuakeFeed):
            raise TypeError("feed must be specified as a QuakeFeed object")

        self.feed = feed
        self.data = []

    def read_feed(self):
        """
        Refreshes this dataset with data from the linked feed.

        The new data replaces any existing data.
        """
        # Write code here to replace existing data with new earthquake data.
        # Use the value returned by the feed's reader() method as the
        # subject of a for loop.

        reader = self.feed.reader()

        for sQuake in reader:
            self.data.append(
                Quake(
                    datetime.fromisoformat(sQuake.get("time")),
                    float(sQuake.get("longitude")),
                    float(sQuake.get("latitude")),
                    float(sQuake.get("depth")),
                    float(sQuake.get("mag"))
                ))


    def __len__(self):
        """
        Returns the size of this dataset.
        """
        return len(self.data)
        # Write code here that returns the number of quakes downloaded

    def __str__(self):
        """
        Returns information on this dataset as a string.
        """
        return f"{len(self)} quakes from {self.feed}"
        # Write code here to create and return a string representation
        # (Include number of quakes and details of the feed that was used)

    def mean_depth(self):
        """
        Returns the mean depth of the quakes in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.depth for quake in self.data)
        return total / len(self.data)

    def mean_magnitude(self):
        """
        Returns the mean magnitude of the quakes in this dataset.
        """

        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.magnitude for quake in self.data)
        return total / len(self.data)

    def deepest_quake(self):
        """
        Returns details of the shallowest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        shallowest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth < shallowest.depth:
                shallowest = quake
        return shallowest
    
    def deepest_quake(self):
        """
        Returns details of the deepest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        deepest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth > deepest.depth:
                deepest = quake
        return deepest

    def weakest_quake(self):
        """
        Returns details of the strongest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        strongest = self.data[0]
        for quake in self.data[1:]:
            if quake.magnitude > strongest.magnitude:
                strongest = quake
        return strongest
    
    def weakest_quake(self):
        """
        Returns details of the weakest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        weakest = self.data[0]
        for quake in self.data[1:]:
            if quake.magnitude < weakest.magnitude:
                weakest = quake
        return weakest

    def get_all_quakes_near(self, longitude : float, longitude_proximity : float, latitude : float, latitude_proximity : float):
        boundDataSet = [q for q in self.data if q.longitude-longitude <= longitude_proximity and q.latitude-latitude <= latitude_proximity]
        print(boundDataSet)
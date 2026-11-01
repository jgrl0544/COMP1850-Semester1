# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like

from quake import Quake
from feed import QuakeFeed
from dataset import QuakeDataset

significanceLevel = input("Please input significance Level: ")
timePeriod = input("Please input time period: ")

quakeFeed = QuakeFeed(significanceLevel, timePeriod)
quakeDataSet = QuakeDataset(quakeFeed)

quakeDataSet.read_feed()
print(quakeDataSet)
print(f"Mean depth was at {quakeDataSet.mean_depth()}")
print(f"Mean magnitude was {quakeDataSet.mean_magnitude()}")

strongest = quakeDataSet.weakest_quake()
print(f"Strongest quake was on {strongest.when.date()}, {strongest.when.time()} at {strongest.magnitude} magnitude.")
print(f"It was at longitude {strongest.longitude} and latitude {strongest.latitude} at a depth of {strongest.depth} km.")
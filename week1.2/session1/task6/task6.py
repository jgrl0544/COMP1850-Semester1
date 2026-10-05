# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

artistsAndSongs = {
    "Artist1" : ["Song1", "Song2", "Song3"],
    "Artist2" : ["Song1", "Song2", "Song3"],
    "Artist3" : ["Song1", "Song2", "Song3"]
}

# Pretty-print the data structure

pprint(artistsAndSongs)

# Display details of one album recorded by a specific artist

# Artist 3's Song2
print(list(artistsAndSongs.get("Artist1"))[1])
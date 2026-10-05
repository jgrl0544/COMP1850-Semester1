# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["City1"] = "River1"
rivers["City2"] = "River2"

# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.values())

# Display all the key:value pairs, as tuples
print(tuple(rivers.items()))

# Delete an entry from the rivers database
del rivers["London"]
# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence



sequence = [] # will probably use a list due to it being a scalable ordered collection until i find another data structure to use.

for step in range(L):
    if (step == 0):
        sequence.append(0)
        continue
    prev = sequence[step - 1]
    diff = prev - step
    if ((diff >= 0) and not (diff in sequence)):
        sequence.append(diff)
    else:
        sequence.append(prev + step)

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

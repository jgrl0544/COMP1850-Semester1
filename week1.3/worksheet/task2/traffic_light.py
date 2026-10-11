"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mohamad Ftayeh
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

# start of my code

ticksPerCycle = sum(states.values())

for systime in range(maxtime):
    loctime = systime % ticksPerCycle # distance along current cycle
    currentState = ""

    for s, dur in states.items():
        loctime -= dur
        if (loctime < 0):
            currentState = s 
            break        

# end of my code

    print(f"Time {systime:03} State {currentState}")
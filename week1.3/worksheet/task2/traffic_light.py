"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Amaan 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)
statetime = 0

state = "red"

print(f"Time {systime:03} State {state}")
while systime < maxtime:
    systime = systime + 1
    statetime = statetime + 1
    if state == "red" and statetime >= 4:
        state = "red_amber" 
        statetime = 0 
    elif state == "red_amber" and statetime >= 3:
        state = "green"
        statetime = 0
    elif state == "green" and statetime >= 5:
        state = "amber"
        statetime = 0
    elif state == "amber" and statetime >= 3:
        state = "red"
        statetime = 0
    print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14
#!/usr/bin/env python

def getAssignmGrades():
    # ---- for loop to take percentages achieved for
    # each assignment
    for count in range(1, assignmNum):
        assignmGrades[0] = input("enter the grade as a percent for assignment "
                + str(count) + ": ")
return

def getAssignmNum():
    # take user input for number of assignments
    # they have completed so far
    assignmNumInput = input("enter the number of assignments completed: ")
    assignmNum = int(assignmNumInput)

    assignmGrades = [assignmNum]
return

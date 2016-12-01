#!/usr/bin/env python

def getAssignmGrade(assignmGrade, assignmWeight, assignmNum):
    # ---- for loop to take percentages achieved for
    # each assignment
    for count in range(0, assignmNum):
        assignmGrade.append(input("enter the grade as a percent for assignment "
                + str(count) + ": "))
        assignmWeight.append(input("enter the weighting for the above"
                + "assignment: "))
    return

# ---- function to ask user for the number of assignments they have
# completed for the module
def getAssignmNum():
    # take user input for number of assignments
    # they have completed so far
    assignmNumInput = input("enter the number of assignments completed: ")
    assignmNum = int(assignmNumInput)

    assignmGrade = [assignmNum]
    assignmWeight = [assignmNum]

    getAssignmGrade(assignmGrade, assignmWeight, assignmNum)
    return

def divideByOneHundred(weight):
    return grade / 100

# start the program
getAssignmNum()

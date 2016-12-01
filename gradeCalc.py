#!/usr/bin/env python

def divideByOneHundred(weight):
    return weight / 100

# ---- function that gets assignment grades and weighting
# for the number of assignments given
def getAssignmInfo(assignmNum):

    assignmGrade = []
    assignmWeight = []

    # --- for loop to take percentages achieved for
    # each assignment
    for count in range(0, assignmNum):
        grade = input("enter the grade as a percent for assignment "
            + str(count+1) + ": ")

        assignmGrade.append(int(grade))

        weight = input("enter the weighting for the above assignment: ")
        assignmWeight.append(int(weight))

    for count in range(0, assignmNum):
        assignmWeight[count] = divideByOneHundred(assignmWeight[count])
        print(assignmWeight[count])
    return

# ---- function to ask user for the number of assignments they have
# completed for the module
def getAssignmNum():
    # take user input for number of assignments
    # they have completed so far
    assignmNumInput = input("enter the number of assignments completed: ")
    assignmNum = int(assignmNumInput)

    getAssignmInfo(assignmNum)
    return

# start the program
getAssignmNum()

#!/usr/bin/env python

# FIELDS
assignmGrade = []
assignmWeight = []
controlFlow = 0

def gradeCalc():
    assignmTotal = []
    assignmNum = getAssignmNum()
    for count in range(0, assignmNum):
        getAssignmInfo(count)
        divideByOneHundred(count)
        assignmTotal.append(multiply(count))

    sumOfResults = sum(assignmTotal)
    examWeight = getExamWeight()
    desiredGrade = getDesiredGrade()
    total = finalCalculation(examWeight, desiredGrade, sumOfResults)
    print("Your required percentage is: " + format(total,'.2f') + "%")

    return

# ---- function to divide weighting by 100
def divideByOneHundred(assignmNum):
    return assignmWeight[assignmNum] / 100

# ---- function to calculate the required percentage
# in the exam
def finalCalculation(examWeight, desiredGrade, sumOfResults):
    return (desiredGrade - sumOfResults) / examWeight

# ---- function to multiply the grade by the
# assignment's weight
def multiply(assignmNum):
    return assignmGrade[assignmNum] * assignmWeight[assignmNum]

# ---- function to ask user for the grade they desire
def getDesiredGrade():
    desiredGrade = input("\nenter the grade you desire to "
            + "achieve in the module: ")
    return int(desiredGrade)

# ---- function to ask user for the weighting of the exam
def getExamWeight():
    examWeight = input("\nenter the weighting of the exam: ")
    return int(examWeight)

# ---- function that gets assignment grades and weighting
# for the number of assignments given
def getAssignmInfo(assignmNum):

    grade = input("\nenter the grade as a percent for assignment "
    + str(assignmNum+1) + ": ")

    assignmGrade.append(int(grade))

    weight = input("\nenter the weighting for the above assignment: ")
    assignmWeight.append(int(weight))

    return

# ---- function to ask user for the number of assignments they have
# completed for the module
def getAssignmNum():
    # take user input for number of assignments
    # they have completed so far
    assignmNumInput = input("enter the number of assignments completed: ")
    assignmNum = int(assignmNumInput)

    return assignmNum

# start the program
gradeCalc()

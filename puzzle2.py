import copy
def intcodeComputer(intcode):
    if isinstance(intcode, list):
        for index in range(0,len(intcode),4):
            if intcode[index] == 1:
                intcode[intcode[index+3]] = intcode[intcode[index+1]] + intcode[intcode[index+2]]
            elif intcode[index] == 2:
                intcode[intcode[index+3]] = intcode[intcode[index+1]] * intcode[intcode[index+2]]
            elif intcode[index] == 99:
                return(intcode)
        return(intcode)
    else:
        print("Bad Intcode op")

memoryState = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]

def findNounVerb(intcode):
    for i in range(0,100):
        for j in range(0,100):
            stateMemeory = intcode.copy()
            stateMemeory[1] = i
            stateMemeory[2] = j
            newState = intcodeComputer(stateMemeory)
            if newState[0] == 19690720:
                print(newState[1])
                return((100*newState[1])+newState[2])

print(findNounVerb(memoryState))

testState = [1,84,78,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]

print(intcodeComputer(testState))
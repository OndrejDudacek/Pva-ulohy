import os

def readInputFromFile(filePath):
    with open(filePath, 'r') as file:
        size = int(file.readline().strip())
        firstDot = list(map(str, file.readline().strip().split()))
        secondDot = list(map(str, file.readline().strip().split()))

        try:
            firstDot = [int(i) for i in firstDot]
            secondDot = [int(i) for i in secondDot]
        except ValueError:
            return size, "Nespravny vstup", "Nespravny vstup"
    return size, firstDot, secondDot


def readOutputFromFile(filePath):
    with open(filePath, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "Nespravny vstup.":
                return ["Nespravny vstup", "Nespravny vstup"]

            if line.startswith("Delka potrubi:"):
                line = line[len("Delka potrubi:"):].strip()
                pipeLength = float(line)
            if line.startswith("Delka hadice:"):
                line = line[len("Delka hadice:"):].strip()
                hoseLength = float(line)

        return pipeLength, hoseLength


def compareResults(calculated_results, expected_results):
    if calculated_results == ["Nespravny vstup", "Nespravny vstup"] and expected_results == ["Nespravny vstup", "Nespravny vstup"]:
        return True

    if isinstance(calculated_results[0], str) or isinstance(expected_results[0], str):
        return False

    tolerance = 1e-6
    return all(abs(calculated - expected) < tolerance for calculated, expected in zip(calculated_results, expected_results))


def printResultsComparison(fileNumber, calculatedResults, expectedResults):
    print("-----")
    print(f"Results for case {fileNumber}:")
    print(f"Calculated Results: {calculatedResults}")
    print(f"Expected Results: {expectedResults}")
    if compareResults(calculatedResults, expectedResults):
        print("Results match! :)✅")
        print("------------------------------------------")
    else:
        print("Results do not match! :(❌")
        print("------------------------------------------")


def inputCheck(firstDot, secondDot, size):
    if not isinstance(size, (int, float)) or size <= 0:
        return False
    
    for dot in [firstDot, secondDot]:
        if not all(isinstance(coordinate, (int, float)) for coordinate in dot):
            return False
        if not all(0 <= coordinate <= size for coordinate in dot):
            return False
        if any(0 < coordinate < 20 or size - 20 < coordinate < size for coordinate in dot):
            return False
    return True


def oppositeSides(firstDot, secondDot, size):
    if firstDot[0] == abs(secondDot[0] - size) or firstDot[1] == abs(secondDot[1] - size) or firstDot[2] == abs(secondDot[2] - size):
        return True
    return False

def calculateIfClose(firstDot, secondDot, size, difference, index):
    axis = 0
    for i in range(3):
        if index != 999:
            if firstDot[i] not in [0, size] and secondDot[i] not in [0, size] and i != index:
                axis = i
                break
        else:
            if firstDot[i] not in [0, size] and secondDot[i] not in [0, size]:
                axis = i
                break
    hose = ((sum([difference[i] for i in range(3) if i != axis])**2 + difference[axis]**2)**0.5)

    verticalTube = difference[2]
    horizontalTube = difference[0] + difference[1]
    pipe = verticalTube + horizontalTube
    return [pipe, hose]

def calculate(firstDot, secondDot, size):
    pipe = 0
    hose = 0

    difference = [abs(firstDot[0] - secondDot[0]),
                  abs(firstDot[1] - secondDot[1]),
                  abs(firstDot[2] - secondDot[2])]
    
    if oppositeSides(firstDot, secondDot, size):
        """
        updatedFirstDot = [coordinate for coordinate in firstDot if coordinate != 0 and coordinate != size]
        updatedSecondDot = [coordinate for coordinate in secondDot if coordinate != 0 and coordinate != size]

        
        firstDotToEdges = [updatedFirstDot[1], updatedFirstDot[0], size - updatedFirstDot[1], size - updatedFirstDot[0]]
        secondDotToEdges = [updatedSecondDot[1], updatedSecondDot[0], size - updatedSecondDot[1], size - updatedSecondDot[0]]
        distaceIf2D = [abs(updatedFirstDot[0] - updatedSecondDot[0]), abs(updatedFirstDot[1] - updatedSecondDot[1])]
        """
        
        pipeLenghts = []
        hoseLenghts = []

        for y in range(3):
            if firstDot[y] != size or firstDot[y] != 0:
                index = y
                toEdge1 = firstDot[y]
                toEdge2 = size - firstDot[y]

                imaginaryDot1 = firstDot.copy()
                imaginaryDot1[y] = 0

                imaginaryDot2 = firstDot.copy()
                imaginaryDot2[y] = size
                
                pipeLenghts.append(toEdge1 + calculateIfClose(imaginaryDot1, secondDot, size, difference, index)[0])
                pipeLenghts.append(toEdge2 + calculateIfClose(imaginaryDot2, secondDot, size, difference, index)[0])

            """
            if i % 2 == 0:
                pipeLenghts.append(firstDotToEdges[i] + secondDotToEdges[i] + size + distaceIf2D[1])
                hoseLenghts.append(((firstDotToEdges[i] + secondDotToEdges[i] + size)**2 + (distaceIf2D[1])**2)**0.5)
            else:
                pipeLenghts.append(firstDotToEdges[i] + secondDotToEdges[i] + size + distaceIf2D[0])
                hoseLenghts.append(((firstDotToEdges[i] + secondDotToEdges[i] + size)**2 + (distaceIf2D[0])**2)**0.5)
            """

        #hose = min(hoseLenghts)
        pipe = min(pipeLenghts)
    else:
        index = 999
        pipe, hose = calculateIfClose(firstDot, secondDot, size, difference, index)
    return [pipe, hose]

"""
    while stack:
        firstDot, secondDot = stack.pop()
        difference = [abs(firstDot[0] - secondDot[0]),
                      abs(firstDot[1] - secondDot[1]),
                      abs(firstDot[2] - secondDot[2])]

        if oppositeSides(firstDot, secondDot, size):
            updatedFirstDot = [coordinate for coordinate in firstDot if coordinate != 0 and coordinate != size]
            updatedSecondDot = [coordinate for coordinate in secondDot if coordinate != 0 and coordinate != size]

            firstDotToEdges = [updatedFirstDot[1], updatedFirstDot[0], size - updatedFirstDot[1], size - updatedFirstDot[0]]
            secondDotToEdges = [updatedSecondDot[1], updatedSecondDot[0], size - updatedSecondDot[1], size - updatedSecondDot[0]]
            distaceIf2D = [abs(updatedFirstDot[0] - updatedSecondDot[0]), abs(updatedFirstDot[1] - updatedSecondDot[1])]

            pipeLenghts = []
            hoseLenghts = []
            for i in range(4):
                if i % 2 == 0:
                    pipeLenghts.append(firstDotToEdges[i] + secondDotToEdges[i] + size + distaceIf2D[1])
                    hoseLenghts.append(((firstDotToEdges[i] + secondDotToEdges[i] + size)**2 + (distaceIf2D[1])**2)**0.5)
                else:
                    pipeLenghts.append(firstDotToEdges[i] + secondDotToEdges[i] + size + distaceIf2D[0])
                    hoseLenghts.append(((firstDotToEdges[i] + secondDotToEdges[i] + size)**2 + (distaceIf2D[0])**2)**0.5)
            hose = min(hoseLenghts)
            pipe = min(pipeLenghts)
        else:
            if firstDot[0] == secondDot[0] or firstDot[1] == secondDot[1] or firstDot[2] == secondDot[2]:
                continue 
            else:
                axis = 0
                for i in range(3):
                    if firstDot[i] not in [0, size] and secondDot[i] not in [0, size]:
                        axis = i
                        break
                hose = ((sum([difference[i] for i in range(3) if i != axis])**2 + difference[axis]**2)**0.5)

                verticalTube = difference[2]
                horizontalTube = difference[0] + difference[1]
                pipe = verticalTube + horizontalTube

    return [pipe, hose]
"""

def printResults(calculatedResults, size, firstDot, secondDot):

    print("Rozmer mistnosti:")
    print(str(size))
    print("Bod #1:")
    print(" ".join(map(str, firstDot)))
    print("Bod #2:")
    print(" ".join(map(str, secondDot)))
    print("Delka potrubi: " + str(calculatedResults[0]))
    print("Delka hadice: " + str(calculatedResults[1]))


def main():
    for fileNumber in range(7):
        inputFilePath = f"/Users/ondrejdudacek/Documents/Pva ulohy/1/{fileNumber:04d}_in.txt"
        outputFilePath = f"/Users/ondrejdudacek/Documents/Pva ulohy/1/{fileNumber:04d}_out.txt"

        try:
            size, firstDot, secondDot = readInputFromFile(inputFilePath)
            expectedPipeLength, expected_hoseLength = readOutputFromFile(outputFilePath)

            if inputCheck(firstDot, secondDot, size):
                calculatedPipeLength, calculatedHoseLength = calculate(firstDot, secondDot, size)
                calculatedResults = [calculatedPipeLength, calculatedHoseLength]
            else:
                calculatedResults = ["Nespravny vstup", "Nespravny vstup"]

            printResults(calculatedResults, size, firstDot, secondDot)
            printResultsComparison(fileNumber, calculatedResults, [expectedPipeLength, expected_hoseLength])

        except FileNotFoundError:
            print(f"File {inputFilePath} not found!")
            continue


if __name__ == "__main__":
    main()
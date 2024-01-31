# 2.py
import sys

def onLine(firstPoint, secondPoint, thirdPoint):
    if firstPoint[0] == secondPoint[0] == thirdPoint[0] or firstPoint[1] == secondPoint[1] == thirdPoint[1]:
        return True
    elif round(firstPoint[0] - firstPoint[1], 1) == round(secondPoint[0] - secondPoint[1], 1) == round(thirdPoint[0] - thirdPoint[1], 1):
        return True
    return False
 

def overlap(firstPoint, secondPoint, thirdPoint):
    if firstPoint == secondPoint or firstPoint == thirdPoint or secondPoint == thirdPoint:
        return True
    return False


def middlePoint(firstPoint, secondPoint, thirdPoint):
    distances = []
    distances.append((round(firstPoint[0] - secondPoint[0], 1))**2 + (round(firstPoint[1] - secondPoint[1], 1))**2)
    distances.append((round(firstPoint[0] - thirdPoint[0], 1))**2 + (round(firstPoint[1] - thirdPoint[1], 1))**2)
    distances.append((round(secondPoint[0] - thirdPoint[0], 1))**2 + (round(secondPoint[1] - thirdPoint[1], 1))**2)
    maxDistanceIndex = distances.index(max(distances))
    if maxDistanceIndex == 0:
        return thirdPoint
    elif maxDistanceIndex == 1:
        return secondPoint
    elif maxDistanceIndex == 2:
        return firstPoint


def main():
    if len(sys.argv) != 3:
        print("Chybně zadané argumenty!")
        sys.exit(1)
    
    #print("První argument: ", sys.argv[1])

    inputLines = sys.argv[1].strip().split('\n')
    points = [inputLine.split() for inputLine in inputLines]

    #převádění inputu na int nebo float
    try:
        firstPoint, secondPoint, thirdPoint = points
        try:
            firstPoint = [int(firstPoint[0]), int(firstPoint[1])]
            secondPoint = [int(secondPoint[0]), int(secondPoint[1])]
            thirdPoint = [int(thirdPoint[0]), int(thirdPoint[1])]
        except ValueError:
            firstPoint = [float(firstPoint[0]), float(firstPoint[1])]
            secondPoint = [float(secondPoint[0]), float(secondPoint[1])]
            thirdPoint = [float(thirdPoint[0]), float(thirdPoint[1])]
            print("převedeno an float")
    except ValueError:
        print("Input error - špatný input! (try line 14)")
        print("Input:" , sys.argv[1])
        print("----------------------------------------------------------")
        return
    
    # printing results
    print("První bod: ", firstPoint)
    print("Druhý bod: ", secondPoint)
    print("Třetí bod: ", thirdPoint)

    if overlap(firstPoint, secondPoint, thirdPoint):
        print("Nektere body se překryvaji.")
    else:
        if onLine(firstPoint, secondPoint, thirdPoint):
            print("Body lezi na jedne primce.")
            middle = middlePoint(firstPoint, secondPoint, thirdPoint)
            if middle == firstPoint:
                print("Prostredni bod: A")
            elif middle == secondPoint:
                print("Prostredni bod: B")
            elif middle == thirdPoint:
                print("Prostredni bod: C")
        else:
            print("Body nelezi na jedne primce.")
    
    print("----------------------------------------------------------")

if __name__ == "__main__":
    main()

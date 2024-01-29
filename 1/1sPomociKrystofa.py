origin = [100, 100, 0]
destination = [300, 100, 200]
size = 300

def getDistancesToEdges(point, size):
    return [point[0],point[1],size-point[0],size-point[1]]

def checkNearEdge(point, size):
    c = 0
    for coord in point:
        if coord<20 or size-20<coord:
            c += 1
    on_cube = 0 in point or size in point
    return c == 1 and on_cube
    
if len(origin) != 3 or len(destination) != 3:
    print("neplatný vstup")

if not (checkNearEdge(origin, size) and checkNearEdge(destination, size)):
    print("Nevyhovující rozměr")

distances = [abs(a-b) for a,b in zip(origin,destination)] 


if size in distances:
    origin = [i for i in origin if (i!=0) and (i!=size)]
    destination = [i for i in destination if (i!=0) and (i!=size)]

    originDistances = getDistancesToEdges(origin, size)
    destinationDistances = getDistancesToEdges(destination, size)

    distances = [0, 0, 0, 0]
    distancesHose = [0, 0, 0, 0]

    for i in range(4):
        originDistance = originDistances[i]
        destinationDistance = destinationDistances[i]
        pointsDistance = [abs(origin[0]-destination[0]), abs(origin[1]-destination[1])]
        distances[i] = originDistance + destinationDistance + size
        distancesHose[i] =(originDistance + destinationDistance + size) ** 2
        if i%2 == 0:
            distances[i] += pointsDistance[1]
            distancesHose[i] += pointsDistance[1] ** 2
        else:
            distances[i] += pointsDistance[0]
            distancesHose[i] += pointsDistance[0] ** 2

    simpleLength = min(distances)
    hoseLength = min(distancesHose)**0.5

else:
    simpleLength = sum(distances)

    axis = [i for i in range(3) if destination[i] not in [0,size] and origin[i] not in [0,size]][0]
    other = [distances[i] for i in range(3) if i!=axis]

    hoseLength = (sum(other)**2 + distances[axis]**2)**0.5

print(f"Délka potrubí: {simpleLength}")
print(f"Délka hadice: {hoseLength}")
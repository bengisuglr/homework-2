from math import sqrt
coordinate_length = int ( input( "please state how many coordinates will be given: "))
coordinates = []
a=1
while a < coordinate_length+1:
    x= input("enter x" + str(a) + ": ")
    y= input("enter y" + str(a) + ": ")
    coordinate= (float(x), float(y))
    coordinates.append(coordinate)
    a=a+1

print("list of coordinates is", coordinates)

index=0
length = len(coordinates)
x_list = []
while index < length:
    point = coordinates[index]

    x_list.append(point[0])
    index= index+1
print('x coordinates are: ', x_list)
total_x= sum(x_list)
print('total of x coordinates', total_x)
average_x= total_x / len(coordinates)
print('average of x coordinates' ,average_x)


index=0
length = len(coordinates)
y_list = []
while index < length:
    point = coordinates[index]

    y_list.append(point[1])
    index= index+1
print('y coordinates are: ', y_list)
total_y= sum(y_list)
print('total of y coordinates', total_y)
average_y= total_y / len(coordinates)
print('average of y coordinates' ,average_y)

CentreOfMass= (average_x, average_y)
print('centre of the mass is ' ,CentreOfMass)

#list of distances of the coordinates from centre of mass
distance_list= []
index= 0
while index < len(coordinates):
    DistanceFromCentreOfMass = sqrt( ((x_list[index] - CentreOfMass[0])**2)+((y_list[index] - CentreOfMass[1])**2) )
    index= index+1
    distance_list.append(DistanceFromCentreOfMass)
print("List of Distances from Centre of Mass is,", distance_list)

max_distance= max(distance_list)
min_distance= min(distance_list)

print("the max distance is;", max_distance, "the min distance is;", min_distance)

FarthestCoordinate = coordinates[distance_list.index(max_distance)]
NearestCoordinate = coordinates[distance_list.index(min_distance)]

print("the fartest coordinate is;", FarthestCoordinate, "the nearest coordinate is;", NearestCoordinate)



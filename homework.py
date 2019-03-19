coordinate_length = int ( input( "please state how many coordinates will be given" ) )
coordinates = []
a=1
while a < coordinate_length+1:
    x= input("enter x" + str(a) + ":")
    y= input("enter y" + str(a) + ":")
    coordinate= (int(x),int(y))
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
    print(x_list)
total_x= sum(x_list)
print(total_x)
average_x= total_x / len(coordinates)
print(average_x)


index=0
length = len(coordinates)
y_list = []
while index < length:
    point = coordinates[index]

    y_list.append(point[1])
    index= index+1
    print(y_list)
total_y= sum(y_list)
print(total_y)
average_y= total_y / len(coordinates)
print(average_y)

CentreOfMass_tuple= (average_x, average_y)
print(CentreOfMass_tuple)

distance_list= []
import math
for index in range(0,length-1):
    length= len(coordinates)
    point = coordinates[index]
    DistanceFromMass= math.sqrt(sum([(a - b)**2 for a, b in zip(point, CentreOfMass_tuple)]))
    DistanceFromMass



    
coordinates = (10,20,30)
print( 40 in coordinates )

coordinates = list(coordinates)
coordinates.append(40)
print(tuple(coordinates))

coordinates.remove(20)
print(coordinates)


#tuple-unpacking

nooo = (10,20,30)
a,b,c = (10,20,30)


new_tuple = (40,50) + nooo
print(new_tuple)


print(a)
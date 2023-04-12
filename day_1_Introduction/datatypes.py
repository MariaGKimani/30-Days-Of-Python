print(type(5))          #int
print(type(3.14))       #float
print(type(5 -5j))      #complex
print(type("Maria"))    #String (str)
print(type(True))       #boolean (bool)
print(type(["maria","Irene","Gladys","24", True]))     #list
print(type(("maria","irene",224,True)))                #tuple
print(type({"maria","Irene"}))                         #set
print(type({"name": "Maria","age": 22,"weight": 70}))   #dictionary (dict)


# # Given:
# # P (2,3) =(x1,y1)
# # Q (10,8) = (x2,y2)
# c = ((10-2)^2 +(8-3)^2)^ 2 
# print(c)
import math
point1 = (2, 3)
point2 = (10, 8)
euclidean_distance = math.dist(point1, point2)
print(euclidean_distance)



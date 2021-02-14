#creating variable

x =50
type(x)
x = "bird"
type(x) # dynamic typing
x =3.14
type(x)

a,b,c = 10, 15, 20 # assigning multiple values to multiple variable
a

a=b=c = 50 # assigning same value to multiple variables
c

# valid and invalid variable names(identifiers)

are circle =314 # invalid because of space
area-circle=314 # invalid because of hyphen
area.circle=314 # invalid because of dot
5x = 1000 # invalid starting with a number
global - 100 # invalid, global is keyword

# valide identifiers

area_cirlce = 314
_x = 10
x5 = 1000 # invalid

#python keywords

import keyword
print(keyword.kwlist)


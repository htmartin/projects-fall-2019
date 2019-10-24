#!/usr/bin/python

# x,y,z print largest odd number, if nonw odd,print message

x=37
y=41
z=5

if x>y and x>z and x%2 == 1:
  print(x)
elif y>z and y%2 == 1:
  print(y)
elif z%2 == 1:
  print(z)
else:
  print('none are odd')

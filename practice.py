#!/usr/bin/python

#docker run -it --rm -v`pwd`:/tmartin midsw205/base:latest


#Assume that two variables, varA and varB, are assigned values, either numbers or strings. 
#Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:

#"string involved" if either varA or varB are strings

#"bigger" if varA is larger than varB

#"equal" if varA is equal to varB

#"smaller" if varA is smaller than varB

varA = 5
varB= "equal"

if isinstance(varA,str):
	  print("string involved")
elif isinstance(varB,str):
	  print("string involved")
elif varA > varB:
	  print("bigger")
elif varA == varB:
	  print("equal")
elif varA < varB:
	  print("smaller")






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

for n in range (3,5):
	print (n)


mysum =0
for n in range (8,15):
	mysum +=n
	print (n)


mysum =0
for n in range (8,15,2):
	print (n)




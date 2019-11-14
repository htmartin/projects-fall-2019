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

for n in range (3,30,3):
	print (n)


range (3,5)


'123456789'[0:5]
0=1
1=2
2=3
3=4
4=5
5=6
6=7
7=8
8=9
9=


mysum =0
for n in range (1,5,2):
	mysum +=n
	print (mysum)
	


	break



	break

mysum =0
for n in range (8,15,2):
	print (n)





text = input("Type anything... ")
print(5*text)

n=0
while n<5:
	print (n)
	n = n+

n=0
while n<5:
	print (n)
	n = n+1



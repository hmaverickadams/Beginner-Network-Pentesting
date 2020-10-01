#this is a python basic script

strings = "the fav fruit is : " 
print(strings + "apple")
#print("\n")
print( 50 + 50)
print (50 ** 2)
print(50 / 50 * 50 -50 + 50) #Pemdas
print(50 % 5)
print(50 // 6)

print("Fun with variable")

print(len(strings))
print(strings.upper())
print(strings.lower())
print(strings.title())

print("Now its for function")
print("\n")

def myintro():
	name = "Nikhil"
	print("My name is "+name)

myintro()

def multiply(x,y):
	return x * y

print(multiply(7,7))

def sqrt(x):
	return x ** 0.5

print(int(sqrt(81)))	

print("Now its for Boolean Value")
bool1 = True
bool2 = 3*3 == 9
bool3 = 9**2 == 4
print(bool1,bool2,bool3)
print(type(bool1))

#Realtional and boolean operators
check = 7>5
print(check)
arr = ["apple","mango","banana"]
arr.append("Custard")
print(arr)
arr.pop(2)
print(arr,len(arr))

arr = ["apple","mango","banana"]
arr1 = ["Strawwberry","Guava"]
combined = zip(arr,arr1)
print(list(combined))

for i in arr1:
	arr.append(i)

print(arr)	

#Tuples cannot be chganged or modified or immutable

buffer = "A" *100
print(buffer)





		

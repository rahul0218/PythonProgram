'''def main():
	list=[]
	for i in range(int(input("Enter length of array : "))):
		x=input("Enter the "+(str(i+1))+"th element : ")
		list.append(x)
		print(list)
main()'''
#list=[]
def printlist(list):
	#global list
	print(list)
def main():
	#global list
	list=[]
	for i in range(int(input("Enter length of array : "))):
		x=input("Enter the "+(str(i+1))+"th element : ")
		list.append(x)
		printlist(list)
main()

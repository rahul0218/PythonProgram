def printlist(sum,list,avg):
	#print(list)
	print("\n\n-------- Output --------\n");
	for i in range(len(list)):
		print("List's "+(str(i+1))+"th element is : "+(str(list[i])));
	print("\nSum of the "+(str(len(list)))+" elements in the list is : "+(str(sum)))
	print("\nAverage of the "+(str(len(list)))+" elements in the list is : "+(str(avg)))
def avg(sum,list):
	avg=0
	avg=sum/len(list)
	printlist(sum,list,avg)
def sum(list):
	sum=0
	for i in range(len(list)):
		sum=sum+int(list[i])
	avg(sum,list)
def iplist(n):
	list=[]
	print("\n")
	for i in range(n):
		x=input("Enter the "+(str(i+1))+"th element : ")
		list.append(x)
	sum(list)
def main():
	print("\n\n-------- Input --------\n");
	n=(int(input("Enter length of array : ")))
	iplist(n)
main()
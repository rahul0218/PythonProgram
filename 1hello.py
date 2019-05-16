print ("Hello")

#Syntax

if 5>2:
    print("Five is greater number")

#variable
x=5
y="Rahul"
print(x)
print(y)

x=4
x="Rahul"
print(x)


y="Rahul"
print("Programmer Name is :" ,y)

w=5
x="+5+"
y="6"
print("Programmer full name is :", x + y)
print("Programmer full name is :",x,"",y)
#print(w+x) // it cann't support

#Number-> int float complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# casting-> int(), float(), str()

x=int(1)
y=int(2.5)
z=int("3")
print (x,y,z)

x=float(1)
y=float(2.9)
z=float("2.9")
a=float("3")
print(x,y,z,a)

x=str(2)
y=str("2")
z=str(3.0)
print(x,y,z)

#String

r="Rahul Kumar"
print(r[3])

r="Rahul Kumar"
print(r[3:9])#it print from 3 to 9 letter. 

r="     Rahul Kumar        "
print(r.strip())#strip() remove blanck space end & start

r="Rahul, Kumar"
print(len(r))
print(r.lower())
print(r.upper())
print(r.replace("Kumar", "Singh"))
print(a.split(","))
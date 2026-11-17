x = 1
y = 2

x = y
y = x

print("Method1: ",x,y)

x = 1
y = 2 
temp = x
x = y
y = temp

print("Method2:",x,y)


x = 1
y = 2

x , y = y, x
print("Method3:",x,y)
a=".|."
l=input().split()
x=int(l[0])
y=int(l[1])
for i in range(1,x,2):
    print((a*i).center(y,'-'))
print("WELCOME".center(y,'-'))
for i in range(x-2,0,-2):
    print((a*i).center(y,'-'))
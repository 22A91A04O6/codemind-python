a=int(input())
b=a*0.8
c=a*0.2
d=b+c
b=a*0.9
c=a*0.25
g=b+c
b=a*0.95
c=a*0.3
j=b+c
k=d+a
s=g+a
v=j+a
if a<=10000:
    print(f"{k:.2f}")
elif a<=20000:
    print(f"{s:.2f}")
else:
    print(f"{v:.2f}")

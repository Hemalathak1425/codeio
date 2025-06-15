num=int(input("ENter The Number:"))
sum=0
for i in range(0,num+1):
    sum=sum+(num%10)
    num=int(num//10)
print('sum of dogits:',sum)

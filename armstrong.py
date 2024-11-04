i=int(input('Please enter a value:  '))
sum=0
temp=i
while temp>0:
    y=temp%10
    sum=sum+y**3
    temp=temp//10
if i==sum:
    print('Your number is an Armstrong number.')
else:
    print('Your number is not an Armstrong number.')
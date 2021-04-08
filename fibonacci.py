def fibo(num):
    a=0
    b=1
    for i in range(0,num):
        print(a)
        c=a+b
        a=b
        b=c
limit=int(input("Enter your number limit you want to print:"))
fibo(limit)
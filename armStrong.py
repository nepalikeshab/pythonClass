def arm(num):
    sum=0
    usr=num
    while(usr>0):
        rem=usr%10
        sum+=rem **3
        usr=usr//10
    if (sum == num):
        print(num, 'armstrong number ho!')
    else:
        print(num, 'armstrong number haina!!!')
Input=int(input('tero num de:'))
arm(Input)

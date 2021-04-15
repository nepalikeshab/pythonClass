
pro=True

while pro==True:
    s=input('Enter the word you want to check:')
    rev=(s[::-1])
    if rev==s:
        print('That is a palindrome word')
    else:
        print('It is not a palindrome word')

    restart = input('Press yes to continue or enter any key to exit:')
    if restart=='yes':
        continue
    else:
        exit()
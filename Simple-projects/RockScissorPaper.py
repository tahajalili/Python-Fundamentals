from random import randint

o = ['r', 's','p']



countU = 0
countC = 0
x = True

while x:
    ch = randint(0,2)
    choice = input("Your turn r/s/p: ")
    
    if o[ch] == choice:
        print('tie\n')

    elif o[ch] == 'r' and choice == 'p':
        print(o[ch])
        countU += 1
        print('You got a point!\n')
    elif o[ch] == 'r' and choice == 's':
        print(o[ch])
        countC += 1
        print('I got a point!\n')
    elif o[ch] == 's' and choice == 'p':
        print(o[ch])
        countC += 1
        print('I got a point!\n')
    elif o[ch] == 's' and choice == 'r':
        print(o[ch])
        countU += 1
        print('You got a point!\n')
    elif o[ch] == 'p' and choice == 's':
        print(o[ch])
        countU += 1
        print('You got a point!\n')
    elif o[ch] == 'p' and choice == 'r':
        print(o[ch])
        countC += 1
        print('I got a point!\n')
    if countC == 3 or countU == 3:
        x = False
        print('\n')
        print('Results'.center(28,'-'))
        print('user'.ljust(20,'.'), countU)
        print('Computer'.ljust(20,'.'),countC)


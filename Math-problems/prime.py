

con = True

while con:
    num = input("enter a number: ")
    n = int(num)
    le = len(num)
    if le >=7:
            print("Number is too big")
            
    else:
        con = False
        for i in range(2,n):
            
            if n%i == 0:
                print("Not prime, because of: " , i)
        q2 = True
        while q2:        
            q = input("Would you like to Continue? y/n: ")
            
            
            if q == 'y':
                con = True
                q2 = False
            elif q == 'n':
                print('\n ==> Bye <==')
                q2 = False
            else:
                print("invalid answer!")
                q2 = True
                
        


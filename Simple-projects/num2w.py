#This code is written by Taha Jalili at 3/24/2018 : ==>tahajalili@gmail.com<==
#HOW IT WORKS:
#This program takes an Integer from user and convert the Integer number into words.
#For Example: 987 => nine hundred eighty seven.


x = input('enter a number: ') #getting user input
x = str(x)  #converting the Integer value to String. 

#Lists that I used in my Logical parts such as if and else.
num1= ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eightteen','nineteen','twenty']
num2 = ['zero','one','tw0','three','four','five','six','seven','eight','nine']
num3 =['zero','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
num4 = ['hundred','thousands']

#d2 stands for digit2 : is the method that convert numbers with 2 digits

def d2(x):
        
    #2 digit numbers
    if x[0] == '1':
        y = int(x[1])
        print(num1[y])
        
    elif x[0] == '2':
        y = int(x[1])
        if y != 0:
            print(num1[10],num2[y])
        else:
            print(num1[10])

    elif x[0] == '3':
        y = int(x[1])
        if y != 0:
            print(num3[0],num2[y])
        else:
            print(num3[0])

    elif x[0] == '4':
        y = int(x[1])
        if y != 0:
            print(num3[1],num2[y])
        else:
            print(num3[1])

    elif x[0] == '5':
        y = int(x[1])
        if y != 0:
            print(num3[2],num2[y])
        else:
            print(num3[2])  

    elif x[0] == '6':
        y = int(x[1])
        if y != 0:
            print(num3[3],num2[y])
        else:
            print(num3[3])

    elif x[0] == '7':
        y = int(x[1])
        if y != 0:
            print(num3[4],num2[y])
        else:
            print(num3[4])

    elif x[0] == '8':
        y = int(x[1])
        if y != 0:
            print(num3[5],num2[y])
        else:
            print(num3[5])      

    elif x[0] == '9':
        y = int(x[1])
        if y != 0:
            print(num3[6],num2[y])
        else:
            print(num3[6])

#d3 stands for digit3 : is the method that convert numbers with 3 digits
def d3(x):
        
    if x[0] == '1':
        y = int(x[1])
        z = int(x[2])
        if y != 0:
            if z != 0:
                if y ==1 and z == 1:
                    print(num2[1],num4[0],num1[1])
                else:
                    print(num2[1],num4[0],num3[y],num2[z])
            elif z == 0:
                print(num2[1],num4[0],num3[y])
        elif y == 0:
            if z == 0:
                print(num2[1],num4[0])
            else:
                print(num2[1],num4[0],num2[z])

        else:
            print(num2[1],num4[0])

    elif x[0] =='2':
        y = int(x[1])
        z = int(x[2])
        if y != 0:
            if z != 0:
                if y ==1 and z == 1:
                    print(num2[2],num4[0],num1[1])
                else:
                    print(num2[2],num4[0],num3[y],num2[z])
            elif z == 0:
                print(num2[2],num4[0],num3[y])
        elif y == 0:
            if z == 0:
                print(num2[2],num4[0])
            else:
                print(num2[2],num4[0],num2[z])

        else:
            print(num2[2],num4[0])

    elif x[0] == '3':
        y = int(x[1])
        z = int(x[2])
        if y != 0:
            if z != 0:
                if y ==1 and z == 1:
                    print(num2[3],num4[0],num1[1])
                else:
                    print(num2[3],num4[0],num3[y],num2[z])
            elif z == 0:
                print(num2[3],num4[0],num3[y])
        elif y == 0:
            if z == 0:
                print(num2[3],num4[0])
            else:
                print(num2[3],num4[0],num2[z])

        else:
            print(num2[3],num4[0])

    elif x[0] == '4':
        y = int(x[1])
        z = int(x[2])
        if y != 0:
            if z != 0:
                if y ==1 and z == 1:
                    print(num2[4],num4[0],num1[1])
                else:
                    print(num2[4],num4[0],num3[y],num2[z])
            elif z == 0:
                print(num2[4],num4[0],num3[y])
        elif y == 0:
            if z == 0:
                print(num2[4],num4[0])
            else:
                print(num2[4],num4[0],num2[z])

        else:
            print(num2[4],num4[0])
    
    elif x[0] == '5':
        y = int(x[1])
        z = int(x[2])
        if y != 0:
            if z != 0:
                if y ==1 and z == 1:
                    print(num2[5],num4[0],num1[1])
                else:
                    print(num2[5],num4[0],num3[y],num2[z])
            elif z == 0:
                print(num2[5],num4[0],num3[y])
        elif y == 0:
            if z == 0:
                print(num2[5],num4[0])
            else:
                print(num2[5],num4[0],num2[z])

        else:
            print(num2[5],num4[0])

    elif x[0] == '6':
        y = int(x[1])
        z = int(x[2])
        if y != 0:
            if z != 0:
                if y ==1 and z == 1:
                    print(num2[6],num4[0],num1[1])
                else:
                    print(num2[6],num4[0],num3[y],num2[z])
            elif z == 0:
                print(num2[6],num4[0],num3[y])
        elif y == 0:
            if z == 0:
                print(num2[6],num4[0])
            else:
                print(num2[6],num4[0],num2[z])

        else:
            print(num2[6],num4[0])

    elif x[0] == '7':
        y = int(x[1])
        z = int(x[2])
        if y != 0:
            if z != 0:
                if y ==1 and z == 1:
                    print(num2[7],num4[0],num1[1])
                else:
                    print(num2[7],num4[0],num3[y],num2[z])
            elif z == 0:
                print(num2[7],num4[0],num3[y])
        elif y == 0:
            if z == 0:
                print(num2[7],num4[0])
            else:
                print(num2[7],num4[0],num2[z])

        else:
            print(num2[7],num4[0])   

    elif x[0] == '8':
        y = int(x[1])
        z = int(x[2])
        if y != 0:
            if z != 0:
                if y ==1 and z == 1:
                    print(num2[8],num4[0],num1[1])
                else:
                    print(num2[8],num4[0],num3[y],num2[z])
            elif z == 0:
                print(num2[8],num4[0],num3[y])
        elif y == 0:
            if z == 0:
                print(num2[8],num4[0])
            else:
                print(num2[8],num4[0],num2[z])

        else:
            print(num2[8],num4[0])             

    elif x[0] == '9':
        y = int(x[1])
        z = int(x[2])
        if y != 0:
            if z != 0:
                if y ==1 and z == 1:
                    print(num2[9],num4[0],num1[1])
                else:
                    print(num2[9],num4[0],num3[y],num2[z])
            elif z == 0:
                print(num2[9],num4[0],num3[y])
        elif y == 0:
            if z == 0:
                print(num2[9],num4[0])
            else:
                print(num2[9],num4[0],num2[z])

        else:
            print(num2[9],num4[0])
#d4 stands for digit3 : is the method that convert numbers with 4 digits
def d4(x):
    if x[0] == '1':
        y = int(x[1])
        z = int(x[2])
        t = int(x[3])
        if y != 0:
            if z != 0:
                if t != 0:
                    if z == 1 and t == 1:
                        print(num2[1], num4[1],num2[1],num4[0],num1[1])
                    else:
                        print(num2[1], num4[1],num2[y],num4[0],num3[z],num2[t])
    elif x[0] == '2':
        y = int(x[1])
        z = int(x[2])
        t = int(x[3])
        if y != 0:
            if z != 0:
                if t != 0:
                    if  z == 2 and t == 2:
                        print(num2[2], num4[1],num2[2],num4[0],num1[10],num2[2])
                    elif z == 1 and t == 1:
                        print(num2[2], num4[1],num2[y],num4[0],num1[1])
                    else:
                        print(num2[2], num4[1],num2[y],num4[0],num3[z],num2[t])
    
    elif x[0] == '3':
        y = int(x[1])
        z = int(x[2])
        t = int(x[3])
        if y != 0:
            if z != 0:
                if t != 0:
                    if  z == 3 and t == 3:
                        print(num2[3], num4[1],num2[3],num4[0],num3[3],num2[3])
                    elif z == 1 and t == 1:
                        print(num2[3], num4[1],num2[y],num4[0],num1[1])
                    else:
                        print(num2[3], num4[1],num2[y],num4[0],num3[z],num2[t])

    elif x[0] == '4':
        y = int(x[1])
        z = int(x[2])
        t = int(x[3])
        if y != 0:
            if z != 0:
                if t != 0:
                    if  z == 4 and t == 4:
                        print(num2[4], num4[1],num2[4],num4[0],num3[4],num2[4])
                    elif z == 1 and t == 1:
                        print(num2[4], num4[1],num2[y],num4[0],num1[1])
                    else:
                        print(num2[4], num4[1],num2[y],num4[0],num3[z],num2[t])

    
    elif x[0] == '5':
        y = int(x[1])
        z = int(x[2])
        t = int(x[3])
        if y != 0:
            if z != 0:
                if t != 0:
                    if  z == 5 and t == 5:
                        print(num2[5], num4[1],num2[5],num4[0],num3[5],num2[5])
                    elif z == 1 and t == 1:
                        print(num2[5], num4[1],num2[y],num4[0],num1[1])
                    else:
                        print(num2[5], num4[1],num2[y],num4[0],num3[z],num2[t])


#We use some ifs to choose what method to use

if len(x) == 2:
    d2(x)
elif len(x) == 3:
    d3(x)
elif len(x) == 4:
    d4(x)














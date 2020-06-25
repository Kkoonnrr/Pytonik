def operators(y,x, countx, county,result):
    while y[county] != 1 and y[0] != 2 and y[0] != 3 and y[0] != 4:
        print("+ - 1\n- - 2\n* - 3\n/ - 4")
        try:
            y[county]=int(input("Which operator would you like to use: "))
        except:
            print("Please, enter correct number")
        if y[county] != 1 and y[0] != 2 and y[0] != 3 and y[0] != 4:
            print("Please, enter correct number")
    if y[county] == 1:
        y[county]="+"
        for index in range (len(y)):
            print(x[index], end="")
            print(y[index], end="")
        print("")
        if countx>=2:
            result += x[countx-1]
            print("Wynik:")
            print(result)
            return result
        else: return x[0]
    elif y[county] == 2:
        print(x[0], end="")
        print("-")
        y[county] = "+";
    elif y[county] == 3:
        print(x[0], end="")
        print("*")
        y[county] = "+";
    elif y[county] == 4:
        print(x[0], end="")
        print("/")
        y[county] = "+";
result=0
x=[0]
y=[0]
countx=0
county=0
end=False
while end==False:
    while x[countx]==0:
        try:
            x[countx]=float(input("First number: "))
        except:
            print("Please, enter the number")
    x.append(0)
    for index in range(len(y)):
        print(x[index], end="")
        print(y[index], end="")
    print("")
    countx+=1
    z=int(input("Would you like to end? 1-end 0-continue: "))
    if z==1:
        print(result)
        end=True
    result=operators(y,x,countx,county,result)
    county+=1
    y.append(0)
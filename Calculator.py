def operators(y,x, countx, county,result):
    #while y[county-1] != "+" and y[county-1] != "-" and y[county-1] != "*" and y[county-1] != "/":
    if y[county-1] == "+":
        result += x[countx]
        return result
    elif y[county-1] == "-":
        result -= x[countx]
        return result
    elif y[county - 1] == "*":
        result = result-x[countx-1] + x[countx-1]*x[countx]
        return result
    elif y[county - 1] == "/":
        result = result-x[countx-1] + x[countx-1]/x[countx]
        return result
result=0
x=[0]
y=["0"]
countx=0
county=0
count=1
end=False
while end==False:
    while x[countx]==0:
        print(count, end="")
        print(" number: ")
        count+=1;
        try:
            x[countx]=float(input())
        except:
            print("Please, enter the number")
    if countx==0:
        result = x[0]
        for index in range(len(y)):
            print(x[index], end="")
    else:
        result = operators(y, x, countx, county, result)
        for index in range(len(y)):
            print(x[index], end="")
            print(y[index], end="")
        print("")
        print(result)
    x.append(0)
    countx+=1
    y[county]=input()
    for index in range(len(y)):
        print(x[index], end="")
        print(y[index], end="")
    print("")
    county+=1
    y.append(0)
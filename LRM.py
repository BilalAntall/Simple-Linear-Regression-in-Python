import matplotlib.pyplot as plt

def Calculate_SummationX_and_Y(attr1,attr2):
    sumX=0
    sumY=0
    sumXY=0
    for i in attr1:
        sumX+=i
    for i in attr2:
        sumY+=i
    for i,j in zip(attr1,attr2):
        sum = i*j
        sumXY+=sum
    return sumX,sumY,sumXY


def calculate_Xsquare(attr1):
    Xsquare = 0
    for i in attr1:
        Xsquare+=i**2
    return Xsquare

def calculate_n(attr1,attr2):
    if(len(attr1)==len(attr2)):
        return len(attr1)
    else:
        print('The size of two attributes should be the same for Linear Regression Computation!')

def calculate_B0(Xsquare,sumY,sumX,sumXY,n):
    return (((Xsquare*sumY)-(sumXY*sumX))/(n*Xsquare-(sumX)**2))

def calculate_B1(Xsquare,sumY,sumX,sumXY,n):
    return (((n*sumXY)-(sumX*sumY))/((n*Xsquare)-sumX**2))

def Show_Linear_Regression_Equation(B0,B1):
    print('The Linear Regression Equation is',end=': ')
    print('Y =',B0,'+','('+str(B1)+' * X)')

def Scatter_Diagram(attr1,attr2):
    plt.scatter(attr1,attr2,color='blue')
    plt.title('Scatter Plot between X and Y')
    plt.show()

def Line_Of_Best_Fit(attr1,attr2,B0,B1):
    max_val = max(attr1)
    min_val = min(attr1)
    predicted_minval = B0+(B1*min_val)
    predicted_maxval = B0+(B1*max_val)
    x_list = [min_val,max_val]
    y_list = [predicted_minval,predicted_maxval]
    plt.scatter(attr1,attr2,color='blue')
    plt.plot(x_list,y_list)
    plt.title('Scatter Plot between X and Y')
    plt.show()

attr1 = [77,50,71,72,81,94,96,99,67]
attr2 = [82,66,78,34,47,85,99,99,68]

sumX,sumY,sumXY = Calculate_SummationX_and_Y(attr1,attr2)
Xsquare = calculate_Xsquare(attr1)
n = calculate_n(attr1,attr2)
B0 = calculate_B0(Xsquare,sumY,sumX,sumXY,n)
B1 = calculate_B1(Xsquare,sumY,sumX,sumXY,n)
Show_Linear_Regression_Equation(B0,B1)
#Scatter_Diagram(attr1,attr2)
Line_Of_Best_Fit(attr1,attr2,B0,B1)

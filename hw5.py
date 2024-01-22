import sys
import matplotlib.pyplot as plt
import numpy as np

def plotData():
    plt.plot(years, days)
    #plt.xticks(np.arange(min(years), max(years)+1, 20.0))
    plt.ylabel("Number of Frozen Days")
    plt.xlabel("Year")
    plt.savefig("plot.jpg")

def linRes():
    global beta
    xMat = years
    yMat = np.reshape(days, (len(days), 1))
    for i in range(len(xMat)):
        xMat[i] = [1, xMat[i]]
    xMat = np.matrix(xMat)
    print("Q3a:")
    print(xMat)
    print("Q3b:")
    print(np.ravel(yMat))
    
    Z = np.transpose(xMat) * xMat
    print("Q3c:")
    print(Z)
    
    I = np.linalg.inv(Z)
    print("Q3d:")
    print(I)
    
    PI = I * np.transpose(xMat)
    print("Q3e:")
    print(PI)
    
    beta = PI * yMat
    beta = np.ravel(beta)
    print("Q3f:")
    print(beta)
    
def predict(test):
    predval = beta[0] + beta[1] * test
    print("Q4: " + str(predval))
    
def sign():
    if (beta[1] < 0):
        print("Q5a: <")
        print("Q5b: Lake Mendota is frozen for less days on average with every year that passes")
    elif (beta[1] > 0):
        print("Q5a: >")
        print("Q5b: Lake Mendota is frozen for more days on average with every year that passes")
    else:
        print("Q5a: =")
        print("Q5b: Lake Mendota is frozen for the same amount of days on average with every year that passes")

def predictNoFreeze():
    xpred = -(beta[0])/beta[1]
    print("Q6a: " + str(xpred))
    print("Q6b: I think this is a compelling prediction. Based on the observed trends in data, the amount of days in which lake mendota is frozen has been on a steady decline since 1855, with rapid fluctuations. Given enough time, the number of frozen days will eventually hit zero if this trend continues.")

def main(argv):
    global years
    global days
    years = []
    days = []
    file = open(argv[1], 'r')
    file.readline()
    while True:
        line = file.readline()
        
        if not line:
            break
        line = line.split(',')
        years.append(int(line[0]))
        days.append(int(line[1]))
    plotData()
    linRes()
    predict(2022)
    sign()
    predictNoFreeze()

if __name__ == '__main__':
    main(sys.argv)
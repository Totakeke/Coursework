import numpy as np
import matplotlib.pyplot as plt
import math 

def calcPolyValues(x_data, x_pdata, order):
    #Calculate the p-order values by splitting up the x matrix, calculating the values and putting it in x_val, then recombining the matrices in x_pdata
    x_val = [[[0 for i in range(len(x_data))] for i in range(len(x_data[0]))] for i in range(order)]
    for order in range(1,order+1):
        x_val[order-1][0] = np.hsplit(x_data,len(x_data[0]))[0]
        for i in range(1,len(x_data[0])):
                x_val[order-1][i] = np.hsplit(x_data,len(x_data[0]))[i]**order
    for order in range(1,order+1):
        x_pdata[order-1] = x_val[order-1][0].copy()
        for i in range(1,len(x_data[0])):
            for j in range(0,order):
                x_pdata[order-1] = np.hstack((x_pdata[order-1], x_val[j][i]))
    return x_pdata

def sampleData(x_data, y_data, testsize):
    #Combine the x and y data for cross validation, then outputting it in matrix form to simplify matrix calculations
    xy_data = np.hstack((y_data,x_data))
    np.random.shuffle(xy_data)
    xy_test = xy_data[:testsize]
    xy_train = xy_data[testsize:]
    x_train = xy_train[:,1:]
    y_train = xy_train[:,:1]
    x_test = xy_test[:,1:]
    y_test = xy_test[:,:1]

    mx_train = np.asmatrix(x_train)
    my_train = np.asmatrix(y_train)
    mx_test = np.asmatrix(x_test)
    my_test = np.asmatrix(y_test)
    mx_data = np.asmatrix(x_data)
    my_data = np.asmatrix(y_data)

    return mx_test, my_test, mx_train, my_train, mx_data, my_data

def calcWls(x_data, y_data, testsize):
    #Calculate the least squares w terms using matrix operations
    mx_test, my_test, mx_train, my_train, mx_data, my_data = sampleData(x_data,y_data,testsize)
       
    w_ls = (mx_train.T * mx_train).I * mx_train.T * my_train
    my_predict = mx_test * w_ls

    return w_ls

def calcMAE(x_data, y_data, testsize, iterations):
    #Calculate the mean and standard deviation of the MAE using matrix operations
    MAE = []
    for i in range (0, iterations): 
        mx_test, my_test, mx_train, my_train, mx_data, my_data = sampleData(x_data,y_data,testsize)
       
        w_ls = (mx_train.T * mx_train).I * mx_train.T * my_train
        my_predict = mx_test * w_ls

        MAE.append(sum(abs(my_test - my_predict))/testsize)
    return np.mean(MAE), np.std(MAE)

def calcRMSE(x_data, y_data, testsize, iterations):
    #Calculate the mean and standard deviation of RMSE values as well as aggregating all the error values
    error = []
    RMSE = []
    for i in range (0, iterations): 
        mx_test, my_test, mx_train, my_train, mx_data, my_data = sampleData(x_data,y_data,testsize)

        w_ls = (mx_train.T * mx_train).I * mx_train.T * my_train

        my_predict = mx_test * w_ls
        
        error.extend((np.asarray(my_test) - np.asarray(my_predict)).flatten())
        RMSE.append(np.sqrt(sum((np.asarray(my_test) - np.asarray(my_predict))**2)/testsize))
    return error, np.mean(RMSE), np.std(RMSE) 

def plotErrors(error):
    #Plotting the aggregated error values
    xlabel = "Error"
    ylabel = "Frequency"
    plt.figure(1)
    plt.subplot(221)
    plt.hist(error[0],bins=50)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title("Linear Regression")
    plt.xlim(-15,15)
    plt.ylim(0,2000)

    plt.subplot(222)
    plt.hist(error[1],bins=50)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title("2nd Order Polynomial Regression")
    plt.xlim(-15,15)
    plt.ylim(0,2000)

    plt.subplot(223)
    plt.hist(error[2],bins=50)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title("3rd Order Polynomial Regression")
    plt.xlim(-15,15)
    plt.ylim(0,2000)

    plt.subplot(224)
    plt.hist(error[3],bins=50)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title("4th Order Polynomial Regression")
    plt.xlim(-15,15)
    plt.ylim(0,2000)
    plt.show()
    return

def calcErrParams(error):
    #Calculate the mean and variance of the error values
    err_mean = [0 for i in range(4)]
    err_var = [0 for i in range(4)]
    for i in range(4):
         err_mean[i] = np.mean(error[i])
    for i in range(4):
         for j in range(len(error[i])):
             err_var[i] += (error[i][j] - err_mean[i])**2
         err_var[i] = err_var[i]/len(error[i])
    return err_mean, err_var

def calcLogLikelihood(error, err_mean, err_var):
    #Calculate the log likelihood values for each p order
    ll = [0 for i in range(4)]
    for i in range (0,4):
        for j in range (0,20000):
            ll[i] += np.log((1/(np.sqrt(err_var[i]*2*math.pi)))*math.exp(-(error[i][j]-err_mean[i])**2/(2*err_var[i])) * 1)
    return ll

def printResults():
    terms = ['intercept term','number of cylinders','displacement','horsepower','weight','acceleration','model year']
    print "Part 1(a) Maximum Likelihood w values"
    for i in range(len(Wls)):
        print str(terms[i]) + ': ' + str(float(Wls[i]))
    print "\n"
    print "Part 1(b) MAE values"
    print "Mean: " + str(MAE[0])
    print "Standard Deviation: " + str(MAE[1])
    print "\n"
    print "Part 2(a) RMSE values for each p order"
    import pandas as pd
    print pd.DataFrame(RMSE, index=[1,2,3,4], columns=['Mean','Standard Deviation'])
    print "\n"
    print "Part 2(b) Plot of the histograms of errors for each p order"
    plotErrors(error)
    print"\n"
    print "Part 2(c) Log likelihood values for each p"
    for i in range(len(ll)):
        print str(i+1) + ': ' + str(ll[i])

x_data = np.loadtxt('X.txt',delimiter=',')
y_data = np.loadtxt('Y.txt').reshape((-1,1))
testsize = 20
iterations = 1000
order = 4
error = {}
x_pdata = {}
RMSE = [[0 for i in range(2)] for i in range(order)]

Wls = calcWls(x_data, y_data, testsize)
MAE = calcMAE(x_data, y_data, testsize, iterations)
x_pdata = calcPolyValues(x_data, x_pdata, order)

for i in range(1,order+1):
    error[i-1], RMSE[i-1][0], RMSE[i-1][1] = calcRMSE(x_pdata[i-1], y_data, testsize, iterations)

err_mean, err_var = calcErrParams(error)
ll = calcLogLikelihood(error, err_mean, err_var)

printResults()


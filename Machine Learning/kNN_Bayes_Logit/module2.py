import numpy as np
import operator
import random
import matplotlib.pyplot as plt

x_test = np.loadtxt('mnist_csv\Xtest.txt', delimiter=',')
x_train = np.loadtxt('mnist_csv\Xtrain.txt', delimiter=',')
label_test = np.loadtxt('mnist_csv\label_test.txt', delimiter=',')
label_train = np.loadtxt('mnist_csv\label_train.txt', delimiter=',')
Q = np.loadtxt('mnist_csv\Q.txt', delimiter = ',')

step =  0.1/5000
w0 = [1 for i in range(5000)]
w0 = np.asarray(w0)
x_train = np.hstack((w0.reshape(-1, 1),x_train))
xy_train = np.hstack((label_train.reshape((-1,1)),x_train))
x_split = {}

for i in range(10):
    x_split[i] = np.asmatrix(xy_train[(xy_train[:,0] == i),1:])

w = {}
for i in range(10):
    w[i] = (np.zeros(21)).reshape((-1,1))

grad = {}
L = np.zeros((10,1000))

for iter in range(1000):
    for p in range(10):
        grad[p] = np.zeros(21)
        #grad[p] = grad[p].reshape((-1,1))
        collect = []
        for i in range(500):
            norm = 0
            for j in range(10):
                norm = norm + np.exp(x_split[p][i]*w[j])
            collect.append(norm)
            grad[p] = grad[p] + (x_split[p][i] - (x_split[p][i]*np.exp(float(x_split[p][i]*w[p]))/norm))
            L[p][iter] = L[p][iter] + (x_split[p][i]*(w[p].reshape(-1,1))) - np.log(norm)
        w[p] = w[p] + (step * grad[p]).transpose()


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
bias = [1 for i in range(5000)]
bias = np.asarray(bias)
x_train = np.hstack((bias.reshape(-1, 1),x_train))
xy_train = np.hstack((label_train.reshape((-1,1)),x_train))
x_split = {}

for i in range(10):
    x_split[i] = np.asmatrix(xy_train[(xy_train[:,0] == i),1:])

w = np.zeros((10,21))
grad = np.zeros((10,21))
L = np.zeros((10,1000))

for iter in range(5):
    for p in range(10):
        norm = np.sum(np.exp(x_split[p]*w.transpose()),axis=1) #500x1 vector, one norm for each row
        for i in range(500):

            grad[p] = grad[p] + (x_split[p][i] - (x_split[p][i]*np.exp(float(x_split[p][i]*(w[p].reshape((-1,1)))))/norm[i]))
        for j in range (10):
            if j != p:
                for m in range(500):
                    grad[p] = grad[p] - (x_split[p][i]*np.exp(float(x_split[p][i]*(w[p].reshape((-1,1)))))/norm[i])
            L[p][iter] = L[p][iter] + (x_split[p][i]*(w[p].reshape(-1,1))) - np.log(norm[i])

        w[p] = w[p] + (step * grad[p])
    grad = np.zeros((10,21))

bias = [1 for i in range(500)]
bias = np.asarray(bias)
x_test = np.asmatrix(np.hstack((bias.reshape(-1, 1),x_test)))
prob = np.zeros((len(x_test),10))

for i in range(len(x_test)):
    norm = np.sum(np.exp(x_test*w.transpose()),axis=1)
    for p in range(10):
        prob[i][p] = prob[i][p] + (x_test[i]*(w[p].reshape(-1,1))) - np.log(norm[i])

label = np.zeros((500,1))

for i in range(500):
    label[i] = np.argmax(prob[i])

plt.figure(1)
for i in range(10):
    plt.subplot(5,2,i+1)
    plt.plot(L[i])
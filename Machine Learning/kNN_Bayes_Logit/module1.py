import numpy as np
import operator
import random
import matplotlib.pyplot as plt

x_test = np.loadtxt('mnist_csv\Xtest.txt', delimiter=',')
x_train = np.loadtxt('mnist_csv\Xtrain.txt', delimiter=',')
label_test = np.loadtxt('mnist_csv\label_test.txt', delimiter=',')
label_train = np.loadtxt('mnist_csv\label_train.txt', delimiter=',')
Q = np.loadtxt('mnist_csv\Q.txt', delimiter = ',')

xy_train = np.hstack((label_train.reshape((-1,1)),x_train))

x_split = {}
x_mu = {}
x_sigma = {}
x_pi = {}

for i in range(10):
    x_split[i] = np.asmatrix(xy_train[(xy_train[:,0] == i),1:])
    x_mu[i] = x_split[i].sum(axis=0)/len(x_split[i])
    x_sigma[i] = ((x_split[i] - x_mu[i]).transpose() * (x_split[i] - x_mu[i]))/(500)
    x_pi[i] = len(x_split[i])/float(len(xy_train))
    
prob = {}

for i in range(10):
    prob[i] = [0 for m in range(500)]
    for j in range(len(x_split[i])):
        prob[i][j] = ((2*np.pi)**-10)*x_pi[i]*((np.linalg.det(x_sigma[i]))**-.5)*float(np.exp(-.5*((x_test[j] - x_mu[i]) * x_sigma[i].I * (x_test[j] - x_mu[i]).transpose())))
 
predict = []

for i in range(500):
    temp = []
    for j in range(10):
        temp.append(prob[j][i])
    predict.append(np.argmax(temp))

j = 0
for i in range(500):
    if label_test[i] == predict[i]:
        j = j + 1

c_matrix = [[0 for i in range(10)] for i in range(10)]
mislabel = {}
 
for i in range(500):
    c_matrix[int(label_test[i])][int(predict[i])] = c_matrix[int(label_test[i])][int(predict[i])] + 1
    if label_test[i] != predict[i]:
        mislabel[i] = str(label_test[i]) + '_' + str(predict[i])

c_matrix = np.asmatrix(c_matrix)

plt.figure(1)
for i in range(10):
    plt.subplot(2,5,i+1)
    image = (np.asmatrix(Q)*(np.asmatrix(x_mu[i])).T).reshape((28, 28))
    plt.imshow(image,cmap="Greys")

plt.show()

mislabel

plt.figure(1)
n = 1
for item in list:
    plt.subplot(1, 3, n)
    image = (np.asmatrix(Q)*(np.asmatrix(x_test[item])).T).reshape((28, 28))
    plt.imshow(image,cmap="Greys")
    plt.title("Index " + str(item) + ", True: " + (mislabel[item].split('_'))[0] + ", Predicted:" + (mislabel[item].split('_'))[1])
    n = n + 1

plt.show()
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
x_train = np.asmatrix(x_train)

w = np.zeros((10,21))
grad = np.zeros((10,21))
L = np.zeros((10,10000))


for iter in range(10000):
    inner = (x_train*w.transpose())
    exp = np.exp(inner)
    norm = np.sum(exp, axis = 1)
    second = -exp/norm
    for i in range(5000):
        second[i,label_train[i]] = 1 + second[i,label_train[i]]
    grad = (second.transpose())*x_train
    for i in range(10):
        L[i][iter] = (np.sum(inner[i*500:(i*500+500)],axis=0).transpose())[i] - np.sum(np.log(norm[i*500:(i*500+500)]))
        #for j in range(i*500,(i*500+500)):
        #    L[i][iter] = L[i][iter] + (x_train[j]*(w[i].reshape(-1,1))) - np.log(norm[j])
    w = w + (step * grad)

bias = [1 for i in range(500)]
bias = np.asarray(bias)
x_test = np.asmatrix(np.hstack((bias.reshape(-1, 1),x_test)))
prob = np.zeros((len(x_test),10))

for i in range(len(x_test)):
    normtest = np.sum(np.exp(x_test*w.transpose()),axis=1)
    for p in range(10):
        prob[i][p] = prob[i][p] + (x_test[i]*(w[p].reshape(-1,1))) - np.log(normtest[i])

predict = []

for i in range(500):
    predict.append(np.argmax(prob[i]))

plt.figure(1)
for i in range(10):
    plt.subplot(5,2,i+1)
    plt.title("L for class " + str(i))
    plt.ylim([-1200,0])
    plt.plot(L[i])
plt.show()

j = 0
for i in range(500):
     if predict[i] == label_test[i]:
         j = j +1

print j


c_matrix = [[0 for i in range(10)] for i in range(10)]
mislabel = {}
 
for i in range(500):
    c_matrix[int(label_test[i])][int(predict[i])] = c_matrix[int(label_test[i])][int(predict[i])] + 1
    if label_test[i] != predict[i]:
        mislabel[i] = str(label_test[i]) + '_' + str(predict[i])

c_matrix = np.asmatrix(c_matrix)

#plt.figure(1)
#n = 1
#for item in list:
#    plt.subplot(1, 3, n)
#    image = (np.asmatrix(Q)*(np.asmatrix(x_test[item,1:])).T).reshape((28, 28))
#    plt.imshow(image,cmap="Greys")
#    plt.title("Index " + str(item) + ", True: " + (mislabel[item].split('_'))[0] + ", Predicted:" + (mislabel[item].split('_'))[1])
#    n = n + 1

#plt.show()



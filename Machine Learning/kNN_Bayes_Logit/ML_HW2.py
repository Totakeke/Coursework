import numpy as np
import operator
import random
import matplotlib.pyplot as plt

x_test = np.loadtxt('mnist_csv\Xtest.txt', delimiter=',')
x_train = np.loadtxt('mnist_csv\Xtrain.txt', delimiter=',')
label_test = np.loadtxt('mnist_csv\label_test.txt', delimiter=',')
label_train = np.loadtxt('mnist_csv\label_train.txt', delimiter=',')
Q = np.loadtxt('mnist_csv\Q.txt', delimiter = ',')

def kNN():
    global x_test
    global x_train
    global label_test
    global label_train
    #maximum k size for kNN
    size = 5
    array = [[0 for i in range(5000)] for i in range(500)]
    for i in range(len(x_test)):
        array[i] = (x_test[i] - x_train)**2

    dist = [[0 for i in range(5000)] for i in range(500)]
    for i in range(len(array)):
        for j in range(len(array[0])):
            dist[i][j] = (sum(array[i][j]))**.5

    argindex = [[0] for i in range(500)]
    for i in range(len(dist)):
        argindex[i] = np.argsort(dist[i])

    predict = {}
    for k in range(size):
        predict[k] = [0 for i in range(500)]
        for i in range(500):
            labels = {}
            for j in range(k+1):
                if labels.has_key(label_train[(argindex[i][j])]):
                    labels[(label_train[(argindex[i][j])])] = labels[(label_train[(argindex[i][j])])] + 1
                else:
                    labels[(label_train[(argindex[i][j])])] = 1
            labelsort = sorted(labels.items(), key=operator.itemgetter(1), reverse=True)
            #perform a random selection for tie-breakers
            m = 0
            if len(labelsort) > 1:
                for p in range(len(labelsort)-1):
                    if labelsort[p][1] == labelsort[p+1][1]:
                        m = m + 1
            if m != 0:
                choose = random.randint(0,m)
                predict[k][i] = labelsort[choose][0]
            else:
                predict[k][i] = labelsort[0][0]

    c_shell = [[0 for i in range(10)] for i in range(10)]
    c_matrices = {}
    mislabel = {}
    for k in range(size):
        c_matrices[k] = np.asmatrix(c_shell) 
        miss = {}
        for i in range(500):
            c_matrices[k][(label_test[i]),(predict[k][i])] = c_matrices[k][(label_test[i]),(predict[k][i])] + 1
            if label_test[i] != predict[k][i]:
                miss[i] = str(label_test[i]) + '_' + str(predict[k][i])
        mislabel[k] = miss
    return c_matrices, mislabel

def bayes():
    global x_test
    global x_train
    global label_test
    global label_train

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

    c_matrix = [[0 for i in range(10)] for i in range(10)]
    mislabel = {}
 
    for i in range(500):
        c_matrix[int(label_test[i])][int(predict[i])] = c_matrix[int(label_test[i])][int(predict[i])] + 1
        if label_test[i] != predict[i]:
            mislabel[i] = str(label_test[i]) + '_' + str(predict[i])
    c_matrix = np.asmatrix(c_matrix)

    return c_matrix, mislabel

def logit():
    global x_test
    global x_train
    global label_test
    global label_train

    step =  0.1/5000
    bias = [1 for i in range(5000)]
    bias = np.asarray(bias)
    x_train_lg = np.hstack((bias.reshape(-1, 1),x_train))
    x_train_lg = np.asmatrix(x_train_lg)

    w = np.zeros((10,21))
    grad = np.zeros((10,21))
    L = np.zeros((10,1000))

    for iter in range(1000):
        inner = (x_train_lg*w.transpose())
        exp = np.exp(inner)
        norm = np.sum(exp, axis = 1)
        second = -exp/norm
        for i in range(5000):
            second[i,label_train[i]] = 1 + second[i,label_train[i]]
        grad = (second.transpose())*x_train_lg
        for i in range(10):
            L[i][iter] = (np.sum(inner[i*500:(i*500+500)],axis=0).transpose())[i] - np.sum(np.log(norm[i*500:(i*500+500)]))
        w = w + (step * grad)

    bias = [1 for i in range(500)]
    bias = np.asarray(bias)
    x_test_lg = np.asmatrix(np.hstack((bias.reshape(-1, 1),x_test)))
    prob = np.zeros((len(x_test),10))

    for i in range(len(x_test_lg)):
        normtest = np.sum(np.exp(x_test_lg*w.transpose()),axis=1)
        for p in range(10):
            prob[i][p] = prob[i][p] + (x_test_lg[i]*(w[p].reshape(-1,1))) - np.log(normtest[i])

    predict = []

    for i in range(500):
        predict.append(np.argmax(prob[i]))

    c_matrix = [[0 for i in range(10)] for i in range(10)]
    mislabel = {}
 
    for i in range(500):
        c_matrix[int(label_test[i])][int(predict[i])] = c_matrix[int(label_test[i])][int(predict[i])] + 1
        if label_test[i] != predict[i]:
            mislabel[i] = str(label_test[i]) + '_' + str(predict[i])

    c_matrix = np.asmatrix(c_matrix)
    return c_matrix, mislabel

def showImages(list):
    plt.figure(1)
    n = 1
    for item in list:
        plt.subplot(1, 3, n)
        image = (np.asmatrix(Q)*(np.asmatrix(x_test[item])).T).reshape((28, 28))
        plt.imshow(image,cmap="Greys")
        plt.title("Index " + str(item) + ", True: " + (mislabel[item].split('_'))[0] + ", Predicted:" + (mislabel[item].split('_'))[1])
        n = n + 1
    plt.show()

c_matrices, mislabel = kNN()
#c_matrix, mislabel = bayes()
#c_matrix, mislabel = logit()
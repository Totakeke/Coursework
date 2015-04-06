import numpy as np
import random as rnd
import bisect as bst
import matplotlib.pyplot as plt
import operator

def distDraw(n, w):
    k = len(w)
    cdf_w = []   
    t = 0 
    for i in range(k):
        t += w[i]
        cdf_w.append(t)   

    s = np.zeros(n)    
    for i in range(n):
        s[i] = bst.bisect(cdf_w, rnd.random())
    return s

def logit(xy_train_lg):
    global x_test_lg
    global x_train_lg
    global label_test
    global label_train

    step =  0.1/5000

    w = np.zeros((2,10))
    grad = np.zeros((2,10))
    L = np.zeros((2,1000))

    for iter in range(1000):
        inner = (x_train_lg*w.transpose())
        exp = np.exp(inner)
        norm = np.sum(exp, axis = 1)
        second = -exp/norm
        for i in range(len(xy_train_lg)):
            second[i,labels.index(label_train[i])] = 1 + second[i,labels.index(label_train[i])]
        grad = (second.transpose())*x_train_lg
        for i in range(2):
            L[i][iter] = (np.sum(inner[(xy_train_lg[:,0] == labels[i])],axis=0).transpose())[i] - np.sum(np.log(norm[(xy_train_lg[:,0] == labels[i])]))
        w = w + (step * grad)

    prob = np.zeros((len(x_test),2))

    for i in range(len(x_test_lg)):
        normtest = np.sum(np.exp(x_test_lg*w.transpose()),axis=1)
        for p in range(2):
            prob[i][p] = prob[i][p] + (x_test_lg[i]*(w[p].reshape(-1,1))) - np.log(normtest[i])

    predict = []

    for i in range(len(x_test_lg)):
        predict.append(labels[np.argmax(prob[i])])

    c_matrix = [[0 for i in range(2)] for i in range(2)]
 
    for i in range(len(x_test_lg)):
        c_matrix[labels.index(label_test[i])][labels.index(predict[i])] = c_matrix[labels.index(label_test[i])][labels.index(predict[i])] + 1

    c_matrix = np.asmatrix(c_matrix)
    return c_matrix

def logitTest(w,alpha):
    global testResult
    global x_test_lg
    global label_test

    predict = []
    for i in range(len(x_test_lg)):
        if (x_test_lg[i]*w.transpose()) >= 0:
            result = 1.0
        else:
            result = -1.0
        testResult[i] += alpha * result
        if testResult[i] >= 0:
            predict.append(1)
        else:
            predict.append(-1)
    error = 0
    for i in range(len(predict)):
        if predict[i] != label_test[i]:
            error += 1
    error = error / float(len(x_test_lg))
    return error

def logitTrain(w,alpha):
    global trainResult
    global x_train_lg
    global label_train

    predict = []
    for i in range(len(x_train_lg)):
        if (x_train_lg[i]*w.transpose()) >= 0:
            result = 1.0
        else:
            result = -1.0
        trainResult[i] += alpha * result
        if trainResult[i] >= 0:
            predict.append(1)
        else:
            predict.append(-1)
    error = 0
    for i in range(len(predict)):
        if predict[i] != label_train[i]:
            error += 1
    error = error / float(len(x_train_lg))
    return error

def boostLogit():
    iter = 1000
    w = np.zeros((iter+1,len(x_train_lg)))
    w[0].fill(1/float(len(x_train_lg)))

    logit_w = {}

    testErr = np.zeros(iter)
    trainErr = np.zeros(iter)
    alpha = np.zeros(iter)
    eps = np.zeros(iter)
    testResult = np.zeros(len(x_test))
    trainResult = np.zeros(len(x_train))

    for t in range(iter):
        s = distDraw(len(x_train_lg), w[t])

        x_bootstrap_lg = x_train_lg[s[0]]
        label_bootstrap_lg = label_train[s[0]]
        for i in range(1,len(s)):
            x_bootstrap_lg = np.append(x_bootstrap_lg, x_train_lg[s[i]], axis = 0)
            label_bootstrap_lg = np.append(label_bootstrap_lg, label_train[s[i]])

        xy_bootstrap_lg = np.hstack((np.asmatrix(label_bootstrap_lg).transpose(),x_bootstrap_lg))

        logit_w[t] = np.zeros(10)

        step = 0.1

        for i in range(len(xy_bootstrap_lg)):
            exp = np.exp(-label_bootstrap_lg[i]*(x_bootstrap_lg[i]* np.asmatrix(logit_w[t]).transpose()))
            sigmoid = 1/float((1+exp))
            logit_w[t] = logit_w[t] + step * (1-sigmoid) * label_bootstrap_lg[i] * x_bootstrap_lg[i]

        predict = []
        for i in range(len(x_train_lg)):
            if (x_train_lg[i]*logit_w[t].transpose()) >= 0:
                predict.append(1)
            else:
                predict.append(-1)

        for i in range(len(predict)):
            if predict[i] != label_train[i]:
                eps[t] += w[t][i]

        alpha[t] = .5*np.log((1-eps[t])/eps[t])
    
        trainErr[t] = logitTrain(logit_w[t], alpha[t])
        testErr[t] = logitTest(logit_w[t], alpha[t])

        w[t+1] = np.zeros(len(x_train))
        for i in range(len(w[t])):
            w[t+1][i] = w[t][i]*np.exp(-alpha[t]*label_train[i]*predict[i])

        w[t+1] = w[t+1]/np.sum(w[t+1])

    # Plotting
    plt.plot(testErr, label="Test Error")
    plt.plot(trainErr, label="Training Error")
    plt.xlabel('iterations')
    plt.ylabel('error')
    plt.title('Error vs. Iterations for Boosted Logistic Regression Classifier')
    plt.legend()
    plt.show()

    plt.plot(alpha, label="alpha")
    plt.plot(eps, label="epsilon")
    plt.title('Epsilon and alpha values across iterations for Boosted Logistic Regresison Classifier')
    plt.xlabel('iterations')
    plt.legend()
    plt.show()

    # Plotting rows
    change = np.zeros(500)
    for i in range(500):
        change[i] = (max(w[:,i])-min(w[:,i]))

    rowind = change.argsort()[-3:][::-1]
    for i in range(3):    
        plt.plot(w[:,rowind[i]],label="Row " + str(rowind[i]))
    plt.title('Variation of p values across iterations for Boosted Logistic Regresison Classifier')
    plt.xlabel('iterations')
    plt.ylabel('p')
    plt.legend()
    plt.show()

x = np.loadtxt('x.csv', delimiter=',')
y = np.loadtxt('y.csv', delimiter=',')

x_test = x[:183,1:]
x_train = x[183:,1:]
label_test = y[:183]
label_train = y[183:]
labels = list(set(y))
labels.sort()

x_train_lg = x[183:]     
xy_train_lg = np.hstack((label_train.reshape((-1,1)),x_train_lg))   
x_train_lg = np.asmatrix(x_train_lg)
x_test_lg = x[:183]

boostLogit()
unboostedLogit = logit(xy_train_lg)
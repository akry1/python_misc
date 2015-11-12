import numpy as np
import numpy.linalg as la
import sys


def linearReg(trainingset, traininglabel,testset, testlabel):
    with open(trainingset,'r') as file:
        training_data = np.array([i.replace('\n','').split(',') for i in list(file)],dtype=float)
    with open(traininglabel,'r') as file:
        training_labels= np.array([i.replace('\n','').split(',') for i in list(file)],dtype=float)
    with open(testset,'r') as file:
        testing_data = np.array([i.replace('\n','').split(',') for i in list(file)],dtype=float)
    with open(testlabel,'r') as file:
        testing_labels = np.array([i.replace('\n','').split(',') for i in list(file)],dtype=float)

    W = la.inv( training_data.T.dot( training_data ) ).dot( training_data.T.dot( training_labels ) )
    RMSE = (sum((testing_labels - testing_data.dot(W))**2)/float(len(testing_labels)))**(1.0/2)

    print 'RMSE of the predictions : '+ str(RMSE[0])



linearReg('F:\Skydrive\ASU\SMM\\training_data.csv', 'F:\Skydrive\ASU\SMM\\training_labels.csv' \
          ,'F:\Skydrive\ASU\SMM\\testing_data.csv', 'F:\Skydrive\ASU\SMM\\testing_labels.csv')
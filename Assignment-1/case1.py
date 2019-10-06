import helper as hp
from math import log
import numpy as np
from matplotlib import pyplot as plt

class test():
    matrix = [[0,0],[0,0]]
    prob = [0.0,0.0,0.0]
    Mean =[]
    W=[[0,0,0],[0,0,0],[0,0,0]]
    var=-1
    range = [[0.0,0.0],[0.0,0.0]]

    def __init__(self,data):
        for i in range(len(data)):
            self.Mean.append(hp.mean(data[i]))

        X = [[] for i in range(3)]
        Y = [[] for i in range(3)]
        sum=0
        for i in np.arange(min1,max,0.1):
            for j in np.arange(miny,may,0.1):
                sum=sum+1
                G = [ 0 for i in range(3)]
                for k in range(3):
                    G[k] = self.get_Gx(i,j,k);
                C=G.index(max(G));
                X[C].append(i)
                Y[C].append(j)
        print sum
        for i in range(3):
            prob[i]=len(X[i])/sum
            print(prob[i])

        # plt.plot(X[0],Y[0],colour='Red',label= "Class_1")
        # plt.plot(X[1],Y[1],colour='Blue',label= "Class_1")
        # plt.plot(X[2],Y[2],colour='Black',label= "Class_1")
        # plt.show()

        c1_mat = hp.get_mat(data[0])
        c2_mat = hp.get_mat(data[1])
        c3_mat = hp.get_mat(data[2])
        for i in range(2):
            for j in range(2):
                if i==j:
                    self.matrix[i][j]=c1_mat[i][j]+c2_mat[i][j]+c3_mat[i][j]
                    self.matrix[i][j]/3
                else:
                    self.matrix[i][j]=0

        for i in range(2):
            self.var = self.var+self.matrix[i][i]
        self.var=self.var/2;
        self.matrix[0][0]=self.var
        self.matrix[1][1]=self.var
        print "variance:",self.var
        # setting line parameters
        for i in range(len(data)):
            self.W[i][0] = self.Mean[i][0]/self.var
            self.W[i][1] = self.Mean[i][1]/self.var
            self.W[i][2] = np.log(self.prob[i])-((self.Mean[i][0]*self.Mean[i][0]+self.Mean[i][1]*self.Mean[i][1]))/(2*self.var)

    def get_Gx(self,x1,x2,c):
        return self.W[c][2]+x1*self.W[c][0]+x2*self.W[c][1]

    def get_ConfusionMat(self,data):
        conf=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(data)):
            for j in range(len(data[i])):
                maxp = -999999999999.9
                index= -1
                for cls in range(3):
                    g_x=self.get_Gx(data[i][j][0],data[i][j][1],cls)
                    if(maxp<g_x):
                        maxp=g_x
                        index=cls
                conf[i][index]=conf[i][index]+1
        return conf

    def test_result(self,data):
        mat=self.get_ConfusionMat(data)
        print(" ")
        print("-------- Confusion_matrix ---------_")
        print(" ")
        print(np.matrix(mat))
        hp.get_result(mat)

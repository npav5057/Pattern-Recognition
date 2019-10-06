import helper as hp
from math import log
import numpy as np
# from matplotlib import pyplot as plt

class test():
    matrix = [[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]]
    prob = [0.2,0.2,0.2]
    Mean =[]
    W =[[],[],[]]
    def __init__(self,data):
        self.class_data = data
        for i in range(len(data)):
            self.Mean.append(hp.mean(data[i]))
        self.matrix[0] = hp.get_mat(data[0])
        self.matrix[1] = hp.get_mat(data[1])
        self.matrix[2] = hp.get_mat(data[2])

        for i in range(len(data)):
            inv =np.linalg.inv(self.matrix[i])
            mn=np.matrix(self.Mean[i]).transpose()
            term=np.dot(inv,mn)
            # print(mn.transpose())
            self.W[i].append(-0.5*inv)
            self.W[i].append(term.transpose())
            self.W[i].append(-0.5*(np.log(np.linalg.det(self.matrix[i]))+np.dot(mn.transpose(),term)  ))



    def get_Gx(self,x1,x2,c):
        x=np.matrix([x1,x2]).transpose()
        t2=np.dot(self.W[c][1],x)+self.W[c][2]
        t1=np.dot(x.transpose(),np.dot(self.W[c][0],x))
        return t1+t2

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



    # def set_boundry(self):
    #     X = [[] for i in range(3)]
    #     Y = [[] for i in range(3)]
    #     for i in np.arange(-50,50,0.1):
    #         for j in np.arange(-50,50,0.1):
    #             G = [ 0 for i in range(3)]
    #             for k in range(3):
    #                 G[k] = self.get_Gx(i,j,k);
    #             C=G.index(max(G));
    #             X[C].append(i)
    #             Y[C].append(i)
    #     plt.plot(X[0],Y[0],colour='Red',label= "Class_1")
    #     plt.plot(X[1],Y[1],colour='Blue',label= "Class_1")
    #     plt.plot(X[2],Y[2],colour='Black',label= "Class_1")
    #     plt.show()

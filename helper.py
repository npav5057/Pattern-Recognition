
def get_result(mat):
    size= len(mat)
    true_samples=0.0
    total_samples=0.0
    for i in range(size):
        for j in range(size):
            if i==j:
                true_samples=true_samples+mat[i][i];
            total_samples=total_samples+mat[i][j]
    print(" ")

    print "Accuracy of Classifier: ",true_samples*100/total_samples

    print(" ")
    recall =[]
    precision = []
    for i in range(size):
        sum=0.0
        for j in range(size):
            sum=sum+mat[i][j]
        if sum == 0:
            precision.append(sum)
        else:
            precision.append(mat[i][i]/sum)

    print(" ")
    for i in range(size):
        print "precision of class ",(i+1),":",precision[i]
    print(" ")
    for i in range(size):
        sum=0.0
        for j in range(size):
            sum=sum+mat[j][i]
        if sum == 0:
            recall.append(sum)
        else:
            recall.append(mat[i][i]/sum)
    print(" ")
    for i in range(size):
        print "Recall of class ",(i+1),":",recall[i]
    print(" ")
    for i in range(size):
		if ((recall[i]+precision[i]) == 0):
			print"F Measure of Class",(i+1),": 0"
		else:
			print "F Measure of Class",(i+1),":",(2*recall[i]*precision[i])/(recall[i]+precision[i])


def covariance(Class,mean1,mean2,i1,i2):
    val=0.0
    for i in range(len(Class)):
        val=val+(Class[i][i1]-mean1)*(Class[i][i2]-mean2)
    val=val/len(Class)
    return val

def mean(Class):
    mn =[0,0]
    for data in Class:
        for j in range(2):
            mn[j] = mn[j]+data[j]
    for j in range(2):
        mn[j] = mn[j]/len(Class)
    return mn

def get_mat(Class):
    mat=[[0, 0],[0, 0]]
    mn = mean(Class)
    for i in range(2):
        for j in range(2):
            mat[i][j] = covariance(Class,mn[i],mn[j],i,j)
    return mat


def get_data(file):
    c1_train=[]
    c1_test=[]
    c2_train=[]
    c2_test=[]
    c3_train=[]
    c3_test=[]
    f=open(file,"r")
    X=[]
    flag = True
    t=0
    for line in f:
        if flag is True:
            flag =False
        else:
            a,b=line.split()
            X.append([float(a),float(b)])
            t=t+1
            if t == 500:
                c1_train=X[:int(len(X)*(0.8))]
                c1_test=X[int(len(X)*0.8):]
                del X[:]

            if t == 1000:
                c2_train=X[:int(len(X)*(0.8))]
                c2_test=X[int(len(X)*0.8):]
                del X[:]

            if t == 2000:
                c3_train=X[:int(len(X)*(0.8))]
                c3_test=X[int(len(X)*0.8):]
                del X[:]

    f.close()
    return c1_train,c1_test,c2_train,c2_test,c3_train,c3_test

def get_datapoints(file):
    train=[]
    test=[]
    f=open(file,"r")
    X=[]
    for line in f:
        a,b=line.split()
        X.append([float(a),float(b)])
    # 75% of data is training data
    train=X[:int(len(X)*(0.8))]
    # rest is testing data
    test=X[int(len(X)*0.8):]
    del X[:]
    f.close()
    return train,test

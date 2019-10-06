import sys
import case1
import case2
import case3
import case4
from helper import get_datapoints,get_data

if len(sys.argv) is 1:
    print("Chose apropriate option.")
    print("Exiting")
    sys.exit(0);

if(sys.argv[1]=='1'):
    c1_training_data,c1_testing_data = get_datapoints("Data1/Class1.txt")
    c3_training_data,c3_testing_data = get_datapoints("Data1/Class3.txt")
    c2_training_data,c2_testing_data = get_datapoints("Data1/Class2.txt")

if(sys.argv[1]=='3'):
    c1_training_data,c1_testing_data = get_datapoints("Data3/Class1.txt")
    c3_training_data,c3_testing_data = get_datapoints("Data3/Class3.txt")
    c2_training_data,c2_testing_data = get_datapoints("Data3/Class2.txt")

if(sys.argv[1]=='2'):
    c1_training_data,c1_testing_data,c2_training_data,c2_testing_data,c3_training_data,c3_testing_data = get_data("Data2/mixed_data.txt")


train_data = [c1_training_data,c2_training_data,c3_training_data]
test_data  = [c1_testing_data,c2_testing_data,c3_testing_data]
print(train_data[0])

if(sys.argv[2]=='1'):
    print("when covariance of matrix is linier")
    ttt = case1.test(train_data)
    # ttt.test_result(test_data)

if(sys.argv[2]=='4'):
    print("Arbitary covariance matrix")
    ttt=case4.test(train_data)
    ttt.test_result(test_data)

if(sys.argv[2]=='2'):
    print("Same covariance matrix for each class")
    ttt=case2.test(train_data)
    ttt.test_result(test_data)

if(sys.argv[2]=='3'):
    print("Arbitary Digonal matrix")
    ttt=case3.test(train_data)
    ttt.test_result(test_data)

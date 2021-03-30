import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
classfier=SVC(kernel='rbf',C=1)
def getData():
    # 获取数据
    datasets=pd.read_csv('iris.data')
    X=datasets.iloc[:,:-1].values
    Y=datasets.iloc[:,-1].values
    # 进行标签处理
    label=LabelEncoder()
    Y=label.fit_transform(Y)
    return X,Y
def Process(X,Y):
    # 进行训练，并且输出训练后的准确率
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.1,random_state=0)
    classfier.fit(x_train,y_train)
    print(classfier.score(x_test,y_test))
def show(X,Y):
    # 绘图
    plt.scatter(X[:,0],Y)
    x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
    y_min, y_max = Y.min()-1, Y.max()+1
    yy,xx=np.meshgrid(np.arange(x_min,x_max,1),np.arange(y_min,y_max,1))
    plt.show()
if __name__ == '__main__':
    X,Y=getData()
    Process(X,Y)
    show(X,Y)
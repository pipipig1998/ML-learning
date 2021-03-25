import  numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score
from sklearn import tree
import matplotlib.pyplot as plt
"""
    四步走：
    ①数据处理
    ②进行训练
    ③画图
    ④给出准确率打分
"""
#第一步进行数据处理
def DataProcess():
    #读取文本
    dataset=pd.read_csv('iris.csv')
    x=dataset.iloc[1:,1:7].values
    y=dataset.iloc[1:,7].values
    #进行标签的处理，进行labelencode进行编码
    label=LabelEncoder()
    y=label.fit_transform(y)
    for i in range(0,x.shape[1]):
        x[:,i]=label.fit_transform(x[:,i])
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    return x_train,x_test,y_train,y_test
def exec(x_train,x_test,y_train,y_test):
    classfier=DecisionTreeClassifier(criterion='gini')
    classfier=classfier.fit(x_train,y_train)
    y_pred=classfier.predict(x_test)
    print(classfier.score(x_test,y_test))
    # 绘制出生成的决策树
    plt.rcParams['savefig.dpi'] = 200  # 图片像素
    plt.rcParams['figure.dpi'] = 200  # 分辨率
    tree.plot_tree(classfier,filled=True)
    plt.show()
    return y_pred
if __name__ == '__main__':
    x_train,x_test,y_train,y_test=DataProcess()
    y_pred=exec(x_train,x_test,y_train,y_test)
    print(r2_score(y_pred,y_test))
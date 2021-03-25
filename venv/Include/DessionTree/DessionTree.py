import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from treelib import Tree,Node
from collections import Counter
from sklearn.model_selection import train_test_split
"""
    思路：
        ①先进性数据预处理
            标签数字化
            差分数据集和测试集
            这个全是汉字，进行label处理后还是得进行数据的计算
        ②进行二分类决策树的构建
        ③看正确率
        ④绘图
"""
def getEnt(list):
    num=0
    ent=1
    for i in list:
        num=num+i
    for i in list:
        ent=ent-(i/num)**2
    return ent
def DataProcess():
    """
    数据主要是进行标签的处理和数据集的划分
    :return: x_train,x_test,y_train,y_test
    """
    dataset=pd.read_csv('iris.csv')
    # 将X和Y进行标签处理
    label=LabelEncoder()
    x=dataset.iloc[:,1:6].values
    y=dataset.iloc[:,7].values
    y=label.fit_transform(y)
    for i in range(0,x.shape[1]):
        x[:,i]=label.fit_transform(x[:,i])
    # 进行测试集和训练集的划分
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    return x_train,x_test,y_train,y_test
def CreateTree(x_train,y_train,tree):
    """
    if y_train 全是同一个类别
        直接标记类别
        :return
    if x_train 中没有属性，或者属性的取值都一样
        标记成标记最多的类
        :return
    从x_train选择最优划分属性a
    for a的每一个取值:
        if 包含A的数据集为空，标记最多的类
        :return
        else
        递归（新数据集，新的属性）
    """
    # 查看样本是否属于同一个类别
    if len(np.unique(y_train)==1):
        tree.create_node(tag=y_train[0], data=y_train[0])
        return
    #看属性是否为空（数据集是否为空）或者属性的取值是否相同
    l_x=x_train.shape[0]
    l_y=x_train.shape[1]
    flag=False
    for i in l_y:
        if len(np.unique(x_train[:,i]))==1:
            flag=True
            break
    if x_train.size==0 or flag:
        a=np.bincount(y_train)[0]
        b=np.bincount(y_train)[1]
        if a>b:
            tree.create_node(tag=0, data=0)
        else:
            tree.create_node(tag=1, data=1)
    #选择最优划分属性a
    Ent_D=getEnt(np.bincount(y_train).tolist())
    #太麻烦了！！！！！！！！不想干了
if __name__ == '__main__':
    x_train,x_test,y_train,y_test=DataProcess()
    list=[1,1]
    print(getEnt(list))
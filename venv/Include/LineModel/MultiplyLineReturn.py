"""
还是同样的步骤
第一步：数据预处理(读取数据，进行缺失值处理，进行标签的转换，分离测试集和训练集，看是否需要进行归一化处理)
第二部：进行训练集和测试集的分离
第三步：进行画图
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
#数据预处理
def DataProcess():
    #读取数据
    dataset=pd.read_csv('50_Startups.csv')
    x=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values
    #处理标签值
    label=LabelEncoder()
    x[:,-1]=label.fit_transform(x[:,-1])
    # print(label.transform(['California']))
    # hotencode=OneHotEncoder()
    # x=hotencode.fit_transform(x).toarray()
    # x=x[:,1:]
    return x,y

#进行测试集和训练集的拆分
def Process(x,y):
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    regression=LinearRegression()
    regression.fit(x_train,y_train)
    y_pred=regression.predict(x_test)
    return x_train,y_train,y_test,y_pred
if __name__ == '__main__':
    x,y=DataProcess()
    x_train,y_train,y_test,y_pred=Process(x,y)
    print(r2_score(y_test,y_pred))
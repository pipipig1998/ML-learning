"""
第一步：数据预处理(读数据，进行缺失值填充，标签处理，归一化等)
第二步：进行测试集和结果集分类
第三步：进行画图描述
"""
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def DataProcess():
    #进行数据的读取,成功进行X和Y的读取
    dataset=pd.read_csv('studentscores.csv')
    x=dataset.iloc[:,0].values
    y=dataset.iloc[:,1].values
    #进行缺失值的处理
    x=SimpleImputer(missing_values=np.nan,strategy='mean').fit_transform(x.reshape(-1,1))
    #同时由于没有标签等任何因素，不需要进行归一化和标签编码处理
    #直接进行训练集和测试集的划分
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)
    # sc = StandardScaler()
    # x_train = sc.fit_transform(x_train)
    # x_test  =sc.fit_transform(x_test)

    classfier=LinearRegression()
    classfier=classfier.fit(x_train,y_train)
    y_pred=classfier.predict(x_test)
    #进行画图表达结果的性质
    plt.scatter(x_test,y_test,color='green')
    plt.plot(x_test,y_pred,color='yellow')
    plt.show()

if __name__ == '__main__':
    DataProcess();
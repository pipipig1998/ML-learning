"""
    步骤：
    ①导包
    ②导入数据
    ③处理丢失的数据
    ④解析分类数据，例如带标签的将他们变成数字的表达方式
    ⑤差分数据集和测试集
    ⑥将数据进行归一化或者特征值标准化
"""
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
def DataProcess():
    #读取数据
    dataset=pd.read_csv('Data.csv')
    # 这里的values是将dataframe类型转换成ndarray类型
    X=dataset.iloc[:,:-1].values
    Y=dataset.iloc[:,-1].values
    #处理丢失的数据
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    X[:,1:3]=imputer.fit_transform(X[:,1:3])
    # print(X)
    #对数据进行编码
    labelencode_x=LabelEncoder()
    X[:,0]=labelencode_x.fit_transform(X[:,0])
    labelencode_y = LabelEncoder()
    Y = labelencode_x.fit_transform(Y)
    onehotencode_x=OneHotEncoder()
    X=onehotencode_x.fit_transform(X).toarray()
    #分成数据集和测试集
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)
    sc_X=StandardScaler()
    x_train=sc_X.fit_transform(x_train)
    x_test=sc_X.fit_transform(x_test)
    print(x_train)

class MyDataProcess():
    #进行读取数据
    dataset=pd.read_csv('Data.csv')
    x=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1]
    #处理缺失值
    imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
    x[:,1:3]=imputer.fit_transform(x[:,1:3])
    #分类数据处理
    label_x=LabelEncoder()
    x[:,0]=label_x.fit_transform(x[:,0])
    label_y=LabelEncoder()
    y=label_y.fit_transform(y)
    onehotencode=OneHotEncoder()
    x=onehotencode.fit_transform(x).toarray()
    #差分训练集和测试集合
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    #进行归一化处理
    sc_x=StandardScaler()
    x_train=sc_x.fit_transform(x_train)
    x_test=sc_x.fit_transform(x_test)
if __name__ == '__main__':
    MyDataProcess()


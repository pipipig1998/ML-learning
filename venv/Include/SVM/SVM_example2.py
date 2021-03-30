import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
def CreateData():
    # 生成样本
    X=np.sort(np.random.rand(40,1)*5,axis=0)
    Y=np.sin(X).ravel()
    # 增加噪声
    Y[::10] += 3 * (0.5 - np.random.rand(4))
    return X,Y
def Process(X,Y):
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    y_rbf = svr_rbf.fit(X, Y).predict(X)
    y_lin = svr_lin.fit(X, Y).predict(X)
    y_poly = svr_poly.fit(X, Y).predict(X)
    lw = 2
    plt.scatter(X, Y, color='darkorange', label='data')
    plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
    plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
    plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
    plt.xlabel('data')
    plt.ylabel('target')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
if __name__ == '__main__':
    X,Y=CreateData()
    Process(X,Y)
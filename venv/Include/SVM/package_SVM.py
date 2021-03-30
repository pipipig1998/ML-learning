import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
"""
官网的例子，直接用datasets生成数据集，然后训练SVM，进行一个绘图
"""
clf=SVC(kernel='linear',C=0.1)
def CreateData():
    # 生成数据集，集合符合高斯分布的点
    X,y=make_blobs(n_samples=40,centers=2,random_state=6)
    return X,y
def Process(X,y):
    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
    # 进行支持向量机的训练
    clf.fit(x_train,y_train)
    print(clf.score(x_test, y_test))
def show(X,y):
    """
        说一下画图的方法：
            先对样本进行画点
            然后获取当前画布的坐标轴X和Y
            对于X和Y，我们利用numpy进行一个均分，然后形成网格布局的坐标
            而对于网格布局，我们需要进行一个预测，选择等高线为-1 0 1 的等高线进行描绘
    """
    # 取X样本的第0列和第1列，然后画点
    plt.scatter(X[:,0],X[:,1],c=y, s=30, cmap=plt.cm.Paired)
    # 获取当前坐标轴
    ax=plt.gca()
    # 获得X和Y的坐标轴
    xlim=ax.get_xlim()
    ylim=ax.get_ylim()
    # 将X和Y坐标轴进行均分，生成坐标点
    xx=np.linspace(xlim[0],xlim[1],30)
    yy=np.linspace(ylim[0],ylim[1],30)
    # 生成的坐标点形成网格坐标
    YY,XX=np.meshgrid(yy,xx)
    #ravel将数据进行平铺展开，把多维数组变成一维
    # 将一维的数据进行纵向的堆叠，然后转置
    # 举个例子 XX=[[1,2],[3,4]]  YY=[[1,2],[3,4]]
    # ravel进行展开 XX=[1,2,3,4] YY=[1,2,3,4]
    # 堆叠  [1,2,3,4]
    #       [1,2,3,4]
    # 然后转置
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    # 网格中的点到预测的距离，也就是SVM中的W这个距离表达
    Z = clf.decision_function(xy).reshape(YY.shape)
    # 画等高线，选择-1，0，1的线进行绘画
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])
    plt.show()
if __name__ == '__main__':
    X,y=CreateData()
    Process(X,y)
    show(X,y)

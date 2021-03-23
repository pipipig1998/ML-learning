import numpy as np
import matplotlib.pyplot as plt
#线性回归模型代码的编写
class LineReturn:
    def __init__(self,dataX,dataY):
        # 赋值给X和Y，代表X矩阵和Y矩阵
        self.dataX=dataX
        self.dataY=dataY
        # print(type(self.dataX))
        self.dataW=self.getW()
        print(self.dataW)
    def getW(self):
        # 计算W矩阵
        return np.linalg.inv(np.transpose(self.dataX)@self.dataX)@np.transpose(self.dataX)@self.dataY

    def show(self):
        #将样本数据进行绘画
        plt.scatter(self.dataX.flatten(),self.dataY.flatten())
        #输出预测函数曲线，需要注意的是这里W矩阵是一维的，需要X*W
        self._dataY=self.dataX@self.dataW
        plt.plot(self.dataX.flatten(),self._dataY.flatten())
        plt.show()
if __name__ == '__main__':
    l=LineReturn(np.linspace(1,10,9,dtype=int).reshape(-1,1),np.linspace(2,20,9,dtype=int).reshape(-1,1))
    l.show()



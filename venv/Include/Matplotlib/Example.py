import numpy as np
import matplotlib
import matplotlib.pyplot as plt
def One():
    # 数据部分
    N = 5
    menMeans = (20, 35, 30, 35, -27)
    womenMeans = (25, 32, 34, 20, -25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)
    width = 0.35
    fig,ax=plt.subplots()
    p1=ax.bar(ind,menMeans,width,yerr=menStd,label='Men')
    p2=ax.bar(ind, womenMeans, width,bottom=menMeans, yerr=womenStd, label='Women')
    ax.axhline(0, color='grey', linewidth=0.8)


    ax.legend()
    plt.show()
if __name__ == '__main__':
    One()
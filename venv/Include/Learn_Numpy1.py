import numpy as np
if __name__ == '__main__':
    # numpy放入矩阵
    a = np.array([1, 2, 3])
    print(a)
    #numpy的数据类型
    a=np.dtype(np.int32)
    print(a)
    #ndim
    a=np.array([[1,2,3],[2,4,6]])
    print(a.ndim)
    print(a.shape)
    #reshape函数
    print(a.reshape(3,2))
    #创建空的矩阵
    a=np.empty([2,3],dtype=np.int)
    print(a)
    #创建0矩阵
    a=np.zeros((2,3))
    print(a)
    print(np.ones((2, 3)))
    #从迭代对象中创建
    list=range(5)
    it=iter(list)
    print(np.fromiter(it, dtype=int))
    print(np.arange(1, 100, 5, dtype=int))
    #生成等步长的一维数组，和上边的arange相似，但是上边指定步长，下边指定数目
    print(np.linspace(1, 100, 50,dtype=int))
    #生成等比数组
    print(np.logspace(1, 100, 5, dtype=int))


    #切片索引操作
    a=np.arange(1,100,2,dtype=int)
    s=slice(2,7,2)
    print(a[s])

    a=np.asarray([[1,2,3],[2,3,4]])
    print(a[1:])
    print(a[1][1])

    x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    print(type(x[x>2]))

    a=np.linspace(1,100,25,dtype=int).reshape((5,5))
    print(a)
    print(a[[1,3]])
    print(a[np.ix_([1,2,3],[3,2,4])])
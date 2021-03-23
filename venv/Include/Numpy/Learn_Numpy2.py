import numpy as np

if __name__ == '__main__':
    #数组算数运算
    a=np.arange(1,10,2)
    b=np.arange(11,20,2)
    print(a * b)

    #数组迭代
    a=np.arange(1,12,2,dtype=int).reshape(2,3)
    print(a)
    for x in np.nditer(a,order='f',op_flags=['readwrite']):
        x[...]=2*x
    print(a)
    for x in a.flat:
        print(x)
    #拷贝新的数组
    b=a.flatten()
    for x in np.nditer(b,op_flags=['readwrite']):
        x[...]=x/2
    print(b)
    #将数据进行展开
    a=np.linspace(1,100,50,dtype=int).reshape(5,10)
    print(a.ravel())
    #进行矩阵的转置
    print(a)
    # print(np.transpose(a)==np.swapaxes(a,0,1))
    print(np.swapaxes(a,0,1))
    #删除数组一维条目
    a=np.linspace(1,100,50,dtype=int).reshape(1,50)
    b=np.squeeze(a)
    print(b)
    print(b.shape)

    #连接数组
    a=np.arange(1,50,5).reshape(2,5)
    b=np.arange(0,49,5).reshape(2,5)
    print(np.concatenate((a,b),axis=1))

    #堆叠数组
    a=np.array([[1,2],[3,4]])
    b=np.array([[5,6],[7,8]])
    print(np.stack((a,b), 2))
    print(np.stack((a,b), 2).shape)

    #分割数组
    a=np.arange(9,dtype=int)
    #分割成几个
    b=np.split(a,3)
    print(b)
    #在什么位置进行分割
    b=np.split(a,[4,7])
    print(b)
    #
    # a=np.arange(1,11,1).reshape(2,5)
    # print(a)
    # print(np.append(a, [[11, 12, 13, 14, 15]], axis=1))

    #位运算
    a,b=13,17
    print(np.bitwise_or(a,b))
    a=37.513
    print(np.around(a))

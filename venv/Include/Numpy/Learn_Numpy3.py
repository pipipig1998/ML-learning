import numpy as np
if __name__ == '__main__':
    #nump的算数运算
    a=np.linspace(1,100,20,dtype=int).reshape(2,10)
    b=np.linspace(1,10,10,dtype=int)
    print(np.add(a,b))
    print(np.multiply(a,b))
    print(np.divide(a,b))
    print(np.subtract(a,b))

    #求倒数，每个元素逐个求倒数
    a=np.array([0.25,1.33,5,0.4])
    print(a)
    print(np.reciprocal(a))

    #求幂
    a=np.linspace(1,5,5,dtype=int)
    print(a)
    b=np.array([1,2,3,4,5])
    print(b)
    print(np.power(a,b))
    #取余
    print(np.mod(a,b))

    #输出指定轴的最大值和最小值
    a=np.linspace(1,100,20,dtype=int).reshape(2,10)
    print(a)
    print(np.amin(a))
    print(np.amax(a))

    #输出百分比的数据
    a=np.linspace(1,100,20,dtype=int)
    print(a)
    print(np.percentile(a,10))

    #输出最大值和最小值的差，axis=0表示纵轴，axis=1表示横轴
    a = np.linspace(1, 100, 20, dtype=int).reshape(2,10)
    print(a)
    print(np.ptp(a,axis=0))
    print(np.median(a))
    print(np.mean(a))

    #输出算数平均值,returned=True表示是否输出权重的加和
    a=np.linspace(1,100,10)
    b=np.array([0.1,0.3,0.2,0.1,0.1,0.1,0.1,0,0,0])
    print(np.average(a,weights=b,returned=True))

    #输出标准差
    a=np.array([1,1,1,1,1,1])
    print(a)
    print(np.std(a))
    print(np.var(a))

    #排序
    a=np.linspace(1,100,100).reshape(2,50)
    print(np.sort(a,axis=1))

    #输出大于where条件的数据,但是返回的是索引
    a=np.linspace(1,100,5)
    print(a)
    print(np.where(a>3))

    #抽取出满足条件的数据进行返回

    print(np.extract(a>3,a))
    print(a)

    #进行大小端的替换
    a=np.array([1,256,1021])
    print(map(hex,a))
    a.byteswap(True)
    print(a)
    print(map(hex,a))

    #视图和副本
    a=np.linspace(1,100,20)
    b=a
    b.shape=2,10
    print(a.shape)
    print(a)














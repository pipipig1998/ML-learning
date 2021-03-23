import numpy as np
if __name__ == '__main__':
    a=np.arange(0,10,1,dtype=int).reshape(2,5)
    print(a)

    #矩阵转置
    print(np.transpose(a))

    #生成0矩阵
    print(np.zeros((2,2),dtype=int))

    # numpy.matlib.eye(n, M,k, dtype),返回单位阵
    # n表示几行，m表示几列，k表示对角线元素的索引
    print(np.eye(3,3,0,dtype=int))

    #创建一个方阵单位阵
    print(np.identity(5,dtype=int))

    #生成随机矩阵
    print(np.random.rand(3,3))

    #计算内积
    a=np.linspace(1,5,4,dtype=int).reshape(2,2)
    b=np.linspace(1,5,4,dtype=int).reshape(2,2)
    print(a)
    print(b)
    print(np.dot(a,b))
    #计算矩阵的knocdock积
    print(np.multiply(a,b))

    #计算矩阵的值
    print(np.linalg.det(a))

    # 求解ax=b的解
    a=np.array([[1,1,1],[0,2,5],[2,5,-1]])
    print(a)
    b=np.array([6,-4,27])
    print(np.linalg.solve(a,b))

    # 输出逆矩阵
    print(np.linalg.inv(a))

    a=np.array([[1,2],[3,4]])
    b=np.array([1,2]).reshape(2,1)
    print(a@b)
    print(np.matmul(a,b))
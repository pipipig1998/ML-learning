import matplotlib.pyplot as plt
import numpy as np
import math
def one():
    # 创建一个图像
    fig = plt.figure()
    #给图像命名
    fig.suptitle('No axes on this figure')
    # 创建一个2*2的子图，返回图像和坐标轴的索引
    fig, ax_lst = plt.subplots(2, 2)
    x=np.linspace(0,2,100)
    ax_lst[0][0].plot(x,x,label='linear')
    ax_lst[0][1].plot(x,x**2,label='平方')
    # 显示图像
    fig.show()
def two():
    # 画三角函数
    fig=plt.figure()
    x=np.arange(0,math.pi*2,0.02)
    y=np.sin(x)
    plt.plot(x,y)
    plt.xlabel('x_label')
    plt.ylabel('y_label')
    plt.show()
def three():
    #使用面向对象的方法来进行构图
    fig=plt.figure()
    ax=fig.add_axes([0,0,1,1])
    ax.set_xlabel('x_label')
    ax.set_ylabel('y_label')
    ax.set_title('坐标轴')
    plt.show()
def four():
    fig=plt.figure()
    #创建一个n*n的子图
    print(fig.subplots(2, 2))
    # 增加总的标题
    fig.suptitle('我是总标题')
    # 增加一个在x,y的文本S，其中，x,y是在0，1之间，相比较于原点的距离
    fig.text(0.7,0.7,'hahahahh')
    # 返回所有子图坐标系列表
    print(fig.get_axes())
    # 返回当前子图的坐标系对象
    print(fig.gca())
    # 将图像插入一个统一的案例
    fig.legend()
    # 显示图像，类似于plt.show()函数
    fig.show()
if __name__ == '__main__':
    four()
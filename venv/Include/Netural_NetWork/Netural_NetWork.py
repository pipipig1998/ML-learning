import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn import datasets
from sklearn.datasets import fetch_openml
"""
    MNIST数据进行训练
"""
def getDataSet():
    mnist=fetch_openml("mnist_784")
    x=mnist['data']
    y=mnist['target']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=10, alpha=1e-4,
                        solver='sgd', verbose=10, tol=1e-4, random_state=1,
                        learning_rate_init=.1)
    mlp.fit(x_train, y_train)
    print("Training set score: %f" % mlp.score(x_train, y_train))
    print("Test set score: %f" % mlp.score(x_test, y_test))
if __name__ == '__main__':
    getDataSet()
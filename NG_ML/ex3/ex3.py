# 实现手写数字识别
# 本章的重点是梯度的正则化计算、分类器和predict函数
# 注意：这不是神经网络，而是多个逻辑回归组成的多分类器
# 每个分类器只区分是i和不是i的数据，输入和输出都是5000行

import numpy as np
from getData import get_data
from one_vs_all import one_vs_all
from predict_all import predict_all
from sklearn.metrics import classification_report

if __name__ == "__main__":
    data = get_data()
    params = data['X'].shape[1]
    all_theta = np.zeros((10, params+1))
    # rows = data['X'].shape[0]
    # x = np.insert(data['X'], 0, values=np.ones(rows), axis=1)

    # theta = np.zeros(params+1)

    # y_0 = np.array([1 if label == 0 else 0 for label in data['y']])
    # y_0 = np.reshape(y_0, (rows, 1))

    # 怪
    all_theta = one_vs_all(data['X'], data['y'], 10, 1)

    y_pred = predict_all(data['X'], all_theta=all_theta)
    print(classification_report(data['y'], y_pred))
    # print(y_pred)

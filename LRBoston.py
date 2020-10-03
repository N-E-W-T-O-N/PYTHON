import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation, datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import metrics


style.use('fivethirtyeight')


boston = datasets.load_boston()
print(boston.feature_names)
print(boston.DESCR)


## Can convert to pandas dataframe or not. But will be required later.

# bos = pd.DataFrame(boston.data)
#
# print(bos.head())
#
# bos.columns = boston.feature_names
# print(bos.head())
#
# bos['Price'] = boston.target
#
# print(bos.head())
#
# Z = bos['Price']
# X = bos.drop('Price', axis = 1)
# # X = bos.drop('RM', axis = 1)
# X = bos.drop('CRIM', axis = 1)

boston_X = boston.data
print(boston_X)

## In order to plot we need to use only one feature, uncomment this to use later along with plotting code
boston_X = boston.data[:, np.newaxis, 2]
print(boston_X)
X_train, X_test, Z_train, Z_test = cross_validation.train_test_split(boston_X,boston.target,test_size = 0.2)
clf = LinearRegression()

clf.fit(X_train,Z_train)

acc = clf.score(X_test, Z_test)
print(acc)

#
#plt.scatter(X_test, Z_test, color = 'black')
#plt.plot(X_test, clf.predict(X_test), color = 'blue', linewidth = 3)
#
# plt.show()






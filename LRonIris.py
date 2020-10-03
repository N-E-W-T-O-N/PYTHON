import numpy as np
from sklearn import preprocessing, cross_validation, svm, datasets
from sklearn.linear_model import LinearRegression
from matplotlib import style
from sklearn import metrics
style.use('ggplot')


dataset = datasets.load_iris()

model = LinearRegression()

X_train, X_test, Z_train, Z_test = cross_validation.train_test_split(dataset.data, dataset.target, test_size = 0.2)


model.fit(X_train, Z_train)

accu = model.score(X_test, Z_test)
predicted = model.predict(X_test)
print(Z_test)
predicted = np.ceil(predicted)
print(predicted)

print(metrics.classification_report(Z_test, predicted))
print(accu)
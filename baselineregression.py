# Zachary Milner
# 11/30/25
# This file uses a DummyRegressor from sklearn as baseline regression to predict the response time from whether the person was given p or b and whether they were given a vowel after or not.

from opendata import *
import matplotlib.pyplot as plt
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error

train_data, train_labels, test_data, test_labels = load_all("cleanTraining.csv", "cleanTesting.csv")

print(report_data_stats(train_data, test_data))

clf = DummyRegressor(strategy="mean")
clf.fit(train_data, train_labels)
test_predict = clf.predict(test_data)

print(f"Mean = {test_predict[0]}")
print(f"R^2 = {clf.score(test_data, test_labels)}")
print(f"Mean Squared Error = {mean_squared_error(test_labels, test_predict)}")

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter([x[0] for x in test_data], [x[1] for x in test_data], test_predict)
ax.set_xlabel("is b")
ax.set_ylabel("is final")
ax.set_zlabel("pred. reaction_rt")
plt.show()

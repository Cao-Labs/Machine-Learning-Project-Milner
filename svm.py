# Zachary Milner
# 11/30/25
# This file uses a support vector machine to predict the response time based off of p/b given and whether there was a trailing vowel.

from opendata import *
import matplotlib.pyplot as plt
from sklearn import svm

train_data, train_labels, test_data, test_labels = load_all("cleanTraining.csv", "cleanTesting.csv")

print(report_data_stats(train_data, test_data))

clf = svm.SVR()
clf.fit(train_data, train_labels)
test_predict = clf.predict(test_data)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter([x[0] for x in test_data], [x[1] for x in test_data], test_predict)
ax.set_xlabel("is b")
ax.set_ylabel("is final")
ax.set_zlabel("pred. reaction_rt")
plt.show()

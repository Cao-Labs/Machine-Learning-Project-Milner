# Zachary Milner
# 11/29/25
# This file uses a multilayer perceptron regressor to predict the response time based off of p/b given and whether there was a trailing vowel.

import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

def read_file(filename: str) -> str:
    """Read a file as a string."""
    with open(filename) as file:
        return file.read()

def load_data(text: str) -> tuple[list[list[float]], list[float]]:
    """Load data and labels from a string in CSV format."""
    data: list[list[float]] = []
    labels: list[float] = []
    lines: list[str] = text.split('\n')

    for line in lines[1:]:
        trial: list[str] = line.split(',')
        try:
            data.append([1 if trial[-4] == "b" else 0, 1 if trial[-3] == "Final" else 0])
            labels.append(float(trial[9]))
        except:
            print(f"Trial {trial} was unable to be loaded.")

    return data, labels

def split_data(data: list[list[float]], labels: list[float], pc_train: float = 0.7) -> tuple[list[list[float]], list[float], list[list[float]], list[float]]:
    """Split data into training and testing data with a default split of 70% to training."""
    sp_point: int = int(len(data) * pc_train)
    return data[:sp_point], labels[:sp_point], data[sp_point:], labels[sp_point:]

text: str = read_file("../data.csv")
data, labels = load_data(text)
train_data, train_labels, test_data, test_labels = split_data(data, labels)

clf = MLPRegressor(solver='lbfgs',
                    alpha=1e-5,
                    hidden_layer_sizes=(3,2),
                    random_state=1)

clf.fit(train_data, train_labels)
test_predict = clf.predict(test_data)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter([x[0] for x in test_data], [x[1] for x in test_data], test_predict)
ax.set_xlabel("is b")
ax.set_ylabel("is final")
ax.set_zlabel("pred. reaction_rt")
plt.show()

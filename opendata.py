# Zachary Milner
# 12/7/25
# This file contains various functions used by multiple of the machine learning methods.

def read_file(filename: str) -> str:
    """Read a file as a string."""
    with open(filename) as file:
        return file.read()

def load_data(text: str) -> tuple[list[list[float]], list[float]]:
    """Load data and labels from a string in CSV format."""
    data: list[list[float]] = []
    labels: list[float] = []
    lines: list[str] = text.split("\n")

    for line in lines[1:]:
        trial: list[str] = line.split(",")
        try:
            data.append([
                1 if trial[-4] == "b" else 0,
                1 if trial[-3] == "Final" else 0
            ])
            labels.append(float(trial[9]))
        except:
            print(f"Trial {trial} was unable to be loaded")

    return data, labels

def load_all(
    train_filename: str,
    test_filename: str
    ) -> tuple[
        list[list[float]],
        list[float],
        list[list[float]],
        list[float]
    ]:
    """Load data from both training and testing files."""
    train_text: str = read_file(train_filename)
    test_text: str = read_file(test_filename)
    train_data, train_labels = load_data(train_text)
    test_data, test_labels = load_data(test_text)

    return train_data, train_labels, test_data, test_labels

def report_data_stats(
    train_data: list[list[float]],
    test_data: list[list[float]]
    ) -> str:
    """Give some data statistics."""
    return f"In the training data there are {len(train_data)} data points.\nIn the testing data there are {len(test_data)} data points."

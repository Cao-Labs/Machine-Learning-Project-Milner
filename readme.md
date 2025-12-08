# Machine Learning Project

This project uses three machine learning techniques to predict the response speed to answering whether a person heard a final consonant of p or b given whether the consonant was p or b and whether the consonant was followed by a final vowel or was the last phoneme itself.

## Installing Dependencies

Dependencies can be installed using `pip install -r requirements.txt`. You may also need to install `PyQt5` for `matplotlib`'s rendering to properly work, which can be done with `pip install PyQt5`.

## Cleaning

The cleaned data is included as `cleanTraining.csv` and `cleanTesting.csv` but if you would like to generate the cleaned data yourself you can run `python3 cleaner.py 0 0.7 PilotData` in which 0 is the random seed (0 was used to generate the included cleaned files) and 0.7 is the proportion of the data that will be used for training (0.7 was used to generate the included cleaned files). This will generate the cleaned files from all files within the PilotData directory (and within subfolders).

## Running AI Predictions

To run each machine learning technique, you can run them from the command line using `python3` without any other arguments (eg. `python3 neuralnetwork.py`). They will use the `cleanTraining.csv` and `cleanTesting.csv` files from the main directory.

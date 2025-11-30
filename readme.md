# Machine Learning Project

This project uses three machine learning techniques to predict the response speed to answering whether a person heard a final consonant of p or b given whether the consonant was p or b and whether the consonant was followed by a final vowel or was the last phoneme itself.

## Cleaning

The cleaned data is included as `cleaned.csv` but if you want to generate the cleaned data yourself you can run `python3 cleaner.py PilotData`. This will generate `cleaned.csv` from all files within the PilotData directory (and within subfolders).

## Running AI Predictions

To run each machine learning technique, you can run `python3 main.py` from within any of the `neuralnetwork`, `baselineregression`, or `svm` directories.

They will use the `cleaned.csv` file from the parent directory.

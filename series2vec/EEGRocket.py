import numpy as np
import pandas as pd
import re
from sktime.classification.kernel_based import RocketClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, classification_report


def convert_to_series(cell):
    # Fix the string by inserting commas between numbers
    formatted_cell = re.sub(r'(?<=\d)\s+(?=-?\d)', ', ', cell.strip())  # Insert commas between numbers
    # Now we can safely evaluate it as a list
    cell_as_list = eval(formatted_cell)  # or use ast.literal_eval if the strings are safe
    # Convert the list into a pandas Series
    return pd.Series(cell_as_list)


def main():
    task = 'eegage'
    train_df = pd.read_csv('./Dataset/' + task + "/" + "X_train.csv").drop("subject_id", axis=1)
    train_df = train_df.applymap(convert_to_series)
    y_train = pd.read_csv('./Dataset/' + task + "/" + "y_train.csv").to_numpy().flatten()
    test_df = pd.read_csv('./Dataset/' + task + "/" + "X_test.csv").drop("subject_id", axis=1)
    test_df = test_df.applymap(convert_to_series)
    y_test = pd.read_csv('./Dataset/' + task + "/" + "y_test.csv").to_numpy().flatten()
    X_train = convert_to_3D(train_df)
    X_test = convert_to_3D(test_df)

    print(X_train.shape)
    clf = RocketClassifier(n_jobs=-3)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))


def convert_to_3D(df):
    # ChatGPT generated code
    n_instances = df.shape[0]
    n_dimensions = df.shape[1]

    series_length = len(df.iloc[0, 0])

    eeg_data_array = np.zeros((n_instances, n_dimensions, series_length))

    for i in range(n_instances):
        for j in range(n_dimensions):
            eeg_data_array[i, j, :] = df.iloc[i, j]
    return eeg_data_array


if __name__ == '__main__':
    main()

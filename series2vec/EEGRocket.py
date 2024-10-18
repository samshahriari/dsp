import numpy as np
import pandas as pd
import re
from sktime.classification.kernel_based import RocketClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, classification_report


def convert_to_series(cell):
    formatted_cell = re.sub(r'(?<=\d)\s+(?=-?\d)', ', ', cell.strip())
    cell_as_list = eval(formatted_cell)
    return pd.Series(cell_as_list)


def main():
    # task = 'moreChannels'
    task = 'newEEG3_50'
    # task = 'EEGage'
    train_df = pd.read_csv('./Dataset/' + task + "/" + "X_train.csv").drop("subject_id", axis=1)
    train_df = train_df.applymap(convert_to_series)
    y_train = pd.read_csv('./Dataset/' + task + "/" + "y_train.csv").to_numpy().flatten()
    test_df = pd.read_csv('./Dataset/' + task + "/" + "X_test.csv").drop("subject_id", axis=1)
    test_df = test_df.applymap(convert_to_series)
    y_test = pd.read_csv('./Dataset/' + task + "/" + "y_test.csv").to_numpy().flatten()
    X_train = convert_to_3D(train_df)
    X_test = convert_to_3D(test_df)

    test_subject_id = pd.read_csv('./Dataset/' + task + "/" + "X_test.csv")['subject_id'].to_list()

    print(X_train.shape)
    clf = RocketClassifier(n_jobs=-3)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    df = pd.DataFrame({'subject_id': test_subject_id, 'y_pred': y_pred, 'y_test': y_test})
    subject_accuracy = df.groupby('subject_id').apply(lambda x: (x['y_pred'] == x['y_test']).mean())
    subject_accuracy_dict = subject_accuracy.to_dict()
    print(subject_accuracy_dict)

    num_subjects = len(set(test_subject_id))
    subject_count = np.zeros((num_subjects, len(set(y_test))+1))
    y_true_subject = []
    prev_subject_id = ""
    row_index = -1
    sub_id = []
    conv = {'A': 0, 'C': 1, 'F': 2}
    if "age" in task:
        conv = {'F': 0, 'M': 1}

    for i, subject_id in enumerate(test_subject_id):
        if prev_subject_id != subject_id:
            prev_subject_id = subject_id
            row_index += 1
            y_true_subject.append(conv[y_test[i]])
            sub_id.append(subject_id)
        predicted = conv[y_pred[i]]
        subject_count[row_index][predicted] += 1
    y_pred_subject = np.argmax(subject_count, axis=1)
    df1 = pd.DataFrame({'subject_id': sub_id, 'y_test': y_true_subject, 'y_pred': y_pred_subject})
    df = pd.concat([df1, pd.DataFrame(subject_count)], axis=1)
    print(df)
    print(classification_report(y_true_subject, y_pred_subject))


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

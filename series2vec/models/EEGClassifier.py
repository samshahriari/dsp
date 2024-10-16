from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd


def create_classifying_model(X_train, y_train, X_test, y_test, test_subject_id):
    # TODO: jämför med ridgeclasifierCV då det är den som ROCKET använder. alphas = np.logspace(-3, 3, 10)
    classifier = RidgeClassifier()  # RidgeClassifier(alpha=0.1, max_iter=2000, tol=1e-4, solver="sag", class_weight="balanced")
    classifier.fit(X_train.cpu(), y_train)

    y_pred = classifier.predict(X_test.cpu())
    # print(y_test)
    # print(test_subject)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    conf_matrix = confusion_matrix(y_test, y_pred)

    print("printing results")
    print(f"Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(report)

    print("Confusion Matrix:")
    print(conf_matrix)
    print("stopped printing results")

    df = pd.DataFrame({'subject_id': test_subject_id, 'y_pred': y_pred, 'y_test': y_test})
    subject_accuracy = df.groupby('subject_id').apply(lambda x: (x['y_pred'] == x['y_test']).mean())
    subject_accuracy_dict = subject_accuracy.to_dict()
    print(subject_accuracy_dict)

    num_subjects = len(set(test_subject_id))
    subject_count = np.zeros((num_subjects, max(y_test)+1))
    y_true_subject = []
    prev_subject_id = ""
    row_index = -1
    sub_id = []
    for i, subject_id in enumerate(test_subject_id):
        if prev_subject_id != subject_id:
            prev_subject_id = subject_id
            row_index += 1
            y_true_subject.append(y_test[i])
            sub_id.append(subject_id)
        predicted = y_pred[i]
        subject_count[row_index][predicted] += 1
    y_pred_subject = np.argmax(subject_count, axis=1)
    from torch.nn.functional import sigmoid
    df1 = pd.DataFrame({'subject_id': sub_id, 'y_test': y_true_subject, 'y_pred': y_pred_subject})
    df = pd.concat([df1, pd.DataFrame(subject_count)], axis=1)
    print(df)
    print(classification_report(y_true_subject, y_pred_subject))

    return classifier, y_pred

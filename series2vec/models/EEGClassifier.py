from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import confusion_matrix


def create_classifying_model(X_train, y_train, X_test, y_test):
    # TODO: jämför med ridgeclasifierCV då det är den som ROCKET använder. alphas = np.logspace(-3, 3, 10)
    classifier = RidgeClassifier()  # RidgeClassifier(alpha=0.1, max_iter=2000, tol=1e-4, solver="sag", class_weight="balanced")
    classifier.fit(X_train.cpu(), y_train)

    y_pred = classifier.predict(X_test.cpu())

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

    return classifier, y_pred

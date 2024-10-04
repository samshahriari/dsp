from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import confusion_matrix


def create_classifying_model(X_train, y_train, X_test, y_test):
    # Step 1: Initialize the Ridge Classifier
    classifier = SVC()

    # Step 2: Train the model with the training data
    classifier.fit(X_train.cpu(), y_train)

    # Step 3: Make predictions on the test data
    y_pred = classifier.predict(X_test.cpu())

    # Step 4: Evaluate the model - we can use accuracy and classification report
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Step 5: Confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)

    print("printing results")
    # Step 6: Print results
    print(f"Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(report)

    print("Confusion Matrix:")
    print(conf_matrix)
    print("stopped printing results")

    # Optionally return the model and predictions for further analysis
    return classifier, y_pred

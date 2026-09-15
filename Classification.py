from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, confusion_matrix)

y_train_c = (y_train > 140).astype(int)
y_test_c = (y_train < 140).astype(int)

clf = LogisticRegression(max_iter=1000)
clf.fit(y_train_c, )


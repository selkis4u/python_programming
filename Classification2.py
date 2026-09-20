from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                            recall_score, confusion_matrix)
import matplotlib.pyplot as plt



#기존 데이터는 불러오기
X,y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

#1단계 숫자 정답을 예/아니오 정답으로 바꾸기
y_train_c = (y_train > 140).astype(int) #140이 넘으면 1
y_test_c = (y_test > 140).astype(int)

#2단계 모델 만들고 학습시키기
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train_c)

#시험용데이터로 예측하기
clf_pred = clf.predict(X_test)

#4단계 채점하기
clf_score = accuracy_score(y_test_c, clf_pred)
print("정확도=%.4f"%accuracy_score(y_test_c, clf_pred))
print("정밀도=%.4f"%precision_score(y_test_c, clf_pred))
print("재현율=%.4f"%recall_score(y_test_c, clf_pred))
print (f"혼동행렬 \n{confusion_matrix(y_test_c, clf_pred)}")
      
#5단계 기준 모델과 비교하기
base = DummyClassifier(strategy="most_frequent")
base.fit(X_train, y_train_c)

base_pred = base.predict(X_test)
base_acc_score = accuracy_score(y_test_c, base_pred)

print("기준모델 정확도=%.4f"%accuracy_score(y_test_c, base_pred))
print(f"정확도 개선율: {(clf_score - base_acc_score) * 100:.1f}%")
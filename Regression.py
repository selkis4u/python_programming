from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, r2_score

#1단계 테이블 불러오고 나누기
X,y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

#2단계 모델만들고 학습시키기
model = LinearRegression()
model.fit(X_train, y_train)

#3단계 시험용 데이터로 예측하기
pred = model.predict(X_test)

#4단계 채점하기
mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)

print(f"평균오차: {mae:.2f}")
print(f"설명력: {r2:.4f}")

#5단계 기준모델과 비교하기
base = DummyRegressor(strategy='mean')
base.fit(X_train, y_train)
base_pred = base.predict(X_test)

base_mae = mean_absolute_error(y_test, base_pred)
base_r2 = r2_score(y_test, base_pred)

print(f"평균오차: {base_mae:.2f}")
print(f"설명력: {base_r2:.4f}")

#기준모델과 비교
error_reduction = ((base_mae - mae) / base_mae) * 100
print(f"기존 모델 평균 오차 개선률: {error_reduction:.1f}")

from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                            recall_score, confusion_matrix)

y_train_c = (y_train > 140).astype(int)
y_test_c = (y_test > 140).astype(int)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train_c)

clf_pred = clf.predict(X_test)

clf_score = accuracy_score(y_test_c, clf_pred)

print("정확도=%.4f"%accuracy_score(y_test_c, clf_pred))
print("정밀도=%.4f"%precision_score(y_test_c, clf_pred))
print("재현율=%.4f"%recall_score(y_test_c, clf_pred))
print (f"혼동행렬 \n{confusion_matrix(y_test_c, clf_pred)}")
      

base = DummyClassifier(strategy="most_frequent")
base.fit(X_train, y_train_c)

base_pred = base.predict(X_test)
acc_score = accuracy_score(y_test_c, base_pred)

print("정확도=%.4f"%accuracy_score(y_test_c, base_pred))
print(f"정확도 개선율: {(clf_score - acc_score) * 100:.1f}%")
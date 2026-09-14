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

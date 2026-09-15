import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

# [1단계] 데이터 로드 및 타깃 변수 이진화 (140점 기준)
diabetes = load_diabetes()
X = diabetes.data
# 진행도가 140 이상이면 1(고위험), 미만이면 0(저위험)
y = (diabetes.target >= 140).astype(int)

# [2단계] 학습/테스트 데이터셋 분할 (8:2)
# stratify=y 를 통해 분할 후에도 클래스 비율(0과 1)을 동일하게 유지
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# [3단계] 기준 모델(Baseline) 생성 및 평가
# 환자의 특성을 전혀 보지 않고 최빈 클래스로 일괄 찍는 모델
dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)
dummy_pred = dummy.predict(X_test)
dummy_acc = accuracy_score(y_test, dummy_pred)

# [4단계] 머신러닝 분류 모델 (Logistic Regression) 학습
# max_iter는 수렴 반복 한도 (슬라이드 권장값 1000)
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
model_acc = accuracy_score(y_test, y_pred)

# [5단계] 성능 비교 및 혼동 행렬 평가
print("=" * 50)
print(f"기준 모델 (Dummy) 정확도: {dummy_acc:.4f}")
print(f"로지스틱 회귀 모델 정확도: {model_acc:.4f}")
print(f"정확도 개선 폭: {(model_acc - dummy_acc) * 100:.2f}%p")
print("=" * 50)

# 세부 평가 지표 산출
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
print(f"정밀도 (Precision): {prec:.4f}")
print(f"재현율 (Recall)   : {rec:.4f}\n")

print("=== 분류 리포트 (Classification Report) ===")
print(classification_report(y_test, y_pred, target_names=["저위험(0)", "고위험(1)"]))

# 혼동 행렬 생성 및 시각화
cm = confusion_matrix(y_test, y_pred)
print("=== 혼동 행렬 (2x2 Matrix) ===")
print(cm)

# disp = ConfusionMatrixDisplay(
#     confusion_matrix=cm, 
#     display_labels=["저위험군(0)", "고위험군(1)"]
# )
# disp.plot(cmap="Blues")
# plt.title("Confusion Matrix: Logistic Regression")
# plt.show()
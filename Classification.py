# ==============================================================================
# 과제 2. 로지스틱 회귀 기반 당뇨병 고위험군 이진 분류
# ==============================================================================

# 1. 모듈 및 평가 지표 임포트
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, classification_report

# 2. 원본 데이터셋 로드
X, y_continuous = load_diabetes(return_X_y=True)

# 3. 타깃 라벨 이산화: 진행도 점수 140점을 기준으로 고위험군(1)과 저위험군(0) 변환
threshold = 140.0
y = (y_continuous >= threshold).astype(int)

# 데이터 분할 (Train 80%, Test 20%)
# stratify=y를 적용하여 훈련/시험 세트의 클래스 비율(0과 1)을 균등하게 유지
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------------------------------------------------------------------
# 2단계: 분류 모델 생성 및 학습
# ------------------------------------------------------------------------------
clf = LogisticRegression()
clf.fit(X_train, y_train)

# ------------------------------------------------------------------------------
# 3단계: 시험용 데이터(X_test)에 대한 예측 수행
# ------------------------------------------------------------------------------
y_pred = clf.predict(X_test)

# ------------------------------------------------------------------------------
# 4단계: 모델 평가 (정확도 산출)
# ------------------------------------------------------------------------------
acc = accuracy_score(y_test, y_pred)
print(f"[로지스틱 회귀 분류 모델]")
print(f"분류 정확도 (Accuracy): {acc * 100:.2f}%\n")
print("[상세 분류 리포트]")
print(classification_report(y_test, y_pred, target_names=["저위험군(0)", "고위험군(1)"]))

# ------------------------------------------------------------------------------
# 5단계: 기준 모델(DummyClassifier - 최빈값 일괄 예측)과 성능 비교
# ------------------------------------------------------------------------------
base_clf = DummyClassifier(strategy="most_frequent")
base_clf.fit(X_train, y_train)
base_pred = base_clf.predict(X_test)

base_acc = accuracy_score(y_test, base_pred)
print(f"[기준 모델 (Dummy Classifier - 단순 다수 클래스 찍기)]")
print(f"기준 모델 정확도 (Accuracy): {base_acc * 100:.2f}%")

# 성능 개선 검증
improvement = (acc - base_acc) * 100
print(f"\n=> 기준 모델 대비 정확도 {improvement:+.2f}%p 개선 달성")
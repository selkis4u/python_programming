import numpy as np


def sigmoid(x: np.ndarray) -> np.ndarray:
    """Sigmoid 활성화 함수"""
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid_derivative(x: np.ndarray) -> np.ndarray:
    """Sigmoid 도함수: s * (1 - s)"""
    s = sigmoid(x)
    return s * (1.0 - s)

def relu(x: np.ndarray) -> np.ndarray:
    """ReLU 활성화 함수"""
    return np.maximum(0, x)

def relu_derivative(x: np.ndarray) -> np.ndarray:
    """ReLU 도함수 (x > 0 이면 1, 그 외에는 0)"""
    return np.where(x > 0, 1.0, 0.0)

if __name__ == "__main__":
    x = np.array([-2.0, -0.5, 0.0, 0.5, 2.0])

    print("--- 1. Sigmoid 함수 테스트 결과 ---")
    print("sigmoid(x)           :", np.round(sigmoid(x), 6))
    print("sigmoid_derivative(x):", np.round(sigmoid_derivative(x), 6))

    print("\n--- 2. ReLU 함수 테스트 결과 ---")
    print("relu(x)              :", relu(x))
    print("relu_derivative(x)   :", relu_derivative(x))
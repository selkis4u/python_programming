def simulate_gradient_flow():
    layers = 10
    initial_gradient = 1.0

    # 1. Sigmoid 네트워크 기울기 전파 시뮬레이션 (최댓값 0.25 가정)
    sigmoid_gradient = initial_gradient
    for _ in range(layers):
        sigmoid_gradient *= 0.25

    # 2. ReLU 네트워크 기울기 전파 시뮬레이션 (양수 구간 도함수 1.0 가정)
    relu_gradient = initial_gradient
    for _ in range(layers):
        relu_gradient *= 1.0

    print("===== 10개 은닉층 기울기 소실 시뮬레이션 결과 =====")
    print(f"초기 기울기 (출력층): {initial_gradient}")
    print(f"Sigmoid 네트워크 10층 통과 후 최종 기울기: {sigmoid_gradient:.10f}")
    print(f"ReLU 네트워크    10층 통과 후 최종 기울기: {relu_gradient:.1f}")

    """
    [결과 분석 및 주석 서술]
    1. Sigmoid 결과:
       - 10개 층을 거치며 (0.25)^10 = 0.0000009537로 기울기가 거의 0에 수렴함.
       - 역전파 신호가 완벽하게 소실(Vanishing)되어 입력층 근처 파라미터가 갱신되지 못함.

    2. ReLU 결과:
       - 양수 영역에서 도함수가 항상 1.0을 유지하므로 10개 층을 통과해도 초기 기울기 1.0이 보존됨.
       - 따라서 별도의 사전 학습(Pre-training)이나 인위적인 초기화 튜닝 없이도 심층 신경망을 끝까지 안정적으로 학습시킬 수 있음.
    """

if __name__ == "__main__":
    simulate_gradient_flow()
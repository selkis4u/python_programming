import numpy as np


def zero_padding(image: np.ndarray, pad_size: int = 1) -> np.ndarray:
  """입력 이미지 배열의 가장자리에 0을 패딩하는 함수."""
  h, w = image.shape
  padded_image = np.zeros(
      (h + 2 * pad_size, w + 2 * pad_size), dtype=image.dtype
  )
  padded_image[pad_size : pad_size + h, pad_size : pad_size + w] = image
  return padded_image


def conv2d(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
  """입력 이미지와 3x3 커널에 대해 Zero-Padding 후 2D Convolution 연산을 수행하는 함수."""
  # 1. Zero-Padding 적용 (가장자리 보존 및 크기 유지 목적)
  padded = zero_padding(image, pad_size=1)

  k_h, k_w = kernel.shape
  img_h, img_w = image.shape

  feature_map = np.zeros((img_h, img_w), dtype=float)

  # 2. 이미지 위를 커널 윈도우로 슬라이딩하며 요소별 곱합 연산
  for i in range(img_h):
    for j in range(img_w):
      receptive_field = padded[i : i + k_h, j : j + k_w]
      feature_map[i, j] = np.sum(receptive_field * kernel)

  return feature_map


def apply_relu(feature_map: np.ndarray) -> np.ndarray:
  """ReLU(Rectified Linear Unit) 함수: 음수는 0으로, 양수는 그대로 반환."""
  return np.maximum(0, feature_map)


def max_pooling_2x2(feature_map: np.ndarray) -> np.ndarray:
  """2x2 크기 윈도우, 보폭 2로 최대 풀링(Max Pooling)을 수행하는 함수."""
  h, w = feature_map.shape
  out_h, out_w = h // 2, w // 2

  pooled = np.zeros((out_h, out_w), dtype=feature_map.dtype)

  for i in range(out_h):
    for j in range(out_w):
      patch = feature_map[i * 2 : (i + 1) * 2, j * 2 : (j + 1) * 2]
      pooled[i, j] = np.max(patch)

  return pooled


if __name__ == "__main__":
  # --- Step 1: 합성곱(Convolution) 연산 검증 ---
  test_image = np.array([
      [10, 10, 0, 0, 0],
      [10, 10, 0, 0, 0],
      [10, 10, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
  ])

  # 외곽선/엣지 검출을 위한 3x3 커널
  test_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

  conv_result = conv2d(test_image, test_kernel)

  print("=== [Step 1] 원본 입력 데이터 (5x5) ===")
  print(test_image)
  print("\n=== 적용된 필터 커널 (3x3) ===")
  print(test_kernel)
  print("\n=== 합성곱 연산 결과 특징 맵 (5x5) ===")
  print(conv_result)

  # --- Step 2 & 3: 활성화(ReLU) 및 풀링(Pooling) 검증 ---
  sample_feature_map = np.array([
      [15.0, -0.5, 0.0, -10.0],
      [-2.0, 30.0, 0.5, 10.0],
      [0.0, -15.0, 40.0, 25.0],
      [10.0, 20.0, -30.0, -25.0],
  ])

  relu_out = apply_relu(sample_feature_map)
  pool_out = max_pooling_2x2(relu_out)

  print("\n=== [Step 2] 원본 특징 맵 (4x4, 음수 포함) ===")
  print(sample_feature_map)
  print("\n=== ReLU 적용 결과 (음수 제거 및 비선형성 확보) ===")
  print(relu_out)
  print("\n=== [Step 3] 2x2 Max Pooling 결과 (크기 2x2로 다운샘플링) ===")
  print(pool_out)
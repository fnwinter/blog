---
layout: post
title: "ResNet 스킵 커넥션"
author: "jungjik.lee"
categories: article
tags: [resnet skip connection]
---

**ResNet의 Skip Connection 설명**

ResNet(Residual Network)은 딥러닝에서 매우 성공적인 신경망 구조로, 특히 네트워크의 깊이가 깊어짐에 따라 발생하는 **기울기 소멸(Gradient Vanishing) 문제**를 해결하기 위해 설계되었습니다. 이 문제를 해결하는 핵심 개념이 **Skip Connection(또는 Shortcut Connection)**입니다.

---

### 🔍 **1. Skip Connection이란?**
Skip Connection은 특정 레이어의 출력을 몇 개의 레이어를 건너뛰어(즉, "skip"하여) 나중의 레이어 출력에 더하는 연결 방식입니다. 이를 통해 네트워크가 학습하는 데 더 유리한 경로를 제공합니다.

- **표준 신경망 (기본 구조)**
  $\[
  y = f(x; W)
  \]$
  여기서 $\( f(x; W) \)$는 가중치 $\( W \)$를 사용한 비선형 변환입니다.

- **Skip Connection을 추가한 구조 (Residual Block)**
  $\[
  y = f(x; W) + x
  \]$
  여기서 $\( x \)$는 입력값, $\( f(x; W) \)$는 몇 개의 레이어를 거친 출력입니다. 이 두 값을 더하는 것이 **Residual(잔차) 블록**의 핵심 아이디어입니다.

  이를 시각적으로 표현하면 아래와 같습니다.
  ```
  입력 (x) → [Convolution, BatchNorm, ReLU] → 출력 (f(x)) 
      ↘------------------------------------↗
               Skip (x)  +  f(x)
  ```

---

### 🔍 **2. Skip Connection의 목적과 이점**
1. **기울기 소멸(Gradient Vanishing) 문제 해결**
   - 딥러닝 네트워크가 깊어질수록 역전파(backpropagation) 과정에서 기울기가 0에 가까워지는 문제가 발생합니다.
   - Skip Connection은 입력 $\( x \)$가 그대로 다음 레이어로 전달되므로, 경사가 0이 되지 않고 더 잘 유지됩니다.

2. **더 깊은 네트워크 학습 가능**
   - ResNet은 수백, 수천 개의 레이어로 구성된 네트워크에서도 높은 성능을 유지할 수 있습니다.
   - Skip Connection 덕분에 학습이 더 원활해졌고, 더 깊은 네트워크를 학습할 수 있게 되었습니다.

3. **Residual(잔차) 학습**
   - ResNet은 단순히 $\( f(x) \)$를 학습하는 대신, $\( f(x) = H(x) - x \)$의 형태로 **잔차(residual)**를 학습합니다.
   - 이는 학습할 대상이 더 단순해지는 효과가 있어 학습이 더 빨라집니다.

---

### 🔍 **3. 수학적 직관**
Residual Block의 출력은 다음과 같이 나타낼 수 있습니다.
$\[
y = f(x; W) + x
\]$
- 여기서 $\( f(x; W) \)$는 가중치 $\( W \)$와 입력 $\( x \)$를 사용하는 변환입니다.
- 만약 학습 도중 $\( f(x; W) = 0 \)$으로 수렴하더라도, 출력 $\( y \)$는 $\( x \)$가 되어 학습이 중단되지 않고 초기 입력이 보존됩니다. 
- 이런 구조 덕분에 **항등 맵(identity mapping)**이 자연스럽게 보장됩니다.

---

### 🔍 **4. 구현 예시 (PyTorch)**
```python
import torch
import torch.nn as nn

class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        
        # 차원이 다를 경우, 1x1 컨볼루션으로 맞춤
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )

    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = torch.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        out += self.shortcut(x)  # Skip Connection 부분
        out = torch.relu(out)
        return out
```

---

### 🔍 **5. 시각화**
1. **Residual Block 내부 구조**
   ```
    x  -----> [Conv, BN, ReLU] ----> [Conv, BN] ----> + ----> ReLU
      ↘--------------------------------------------↗
   ```

2. **전체 ResNet 구조**
   ```
   입력 -> Conv + BN + ReLU -> Residual Block 1 -> Residual Block 2 -> ... -> Fully Connected (FC) -> 출력
   ```

---

### 🔍 **6. 자주 묻는 질문**
#### Q1. **왜 잔차를 학습하는 것이 더 나은가요?**
- 입력 $\( x \)$에 작은 변화를 추가하는 것이 새로운 출력을 예측하는 것보다 더 쉽기 때문입니다.
- 예를 들어, **항등 맵(Identity mapping)**을 학습해야 하는 경우, 기존의 네트워크는 $\( y = x \)$가 되도록 해야 하지만, Residual Block에서는 $\( f(x) = 0 \)$으로 학습하면 됩니다. 이 과정이 훨씬 쉽습니다.

#### Q2. **차원이 다를 때 어떻게 Skip Connection을 적용하나요?**
- 입력 $\( x \)$의 차원과 출력 $\( f(x) \)$의 차원이 다를 때는, $\( 1 \times 1 \)$ 컨볼루션을 사용하여 입력의 차원을 맞춥니다.
- 코드로는 아래와 같이 구현됩니다.
  ```python
  if stride != 1 or in_channels != out_channels:
      self.shortcut = nn.Sequential(
          nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
          nn.BatchNorm2d(out_channels)
      )
  ```

#### Q3. **ResNet과 다른 네트워크와의 차이점은?**
- 일반 신경망(VGG 등)과 달리, ResNet은 Skip Connection 덕분에 더 깊은 네트워크에서도 **Gradient Vanishing** 문제를 피할 수 있습니다.
- 더 많은 레이어를 쌓아도 성능이 떨어지지 않는다는 점이 큰 차이점입니다.

---

### 🔍 **7. 요약**
- **Skip Connection**은 입력을 그대로 다음 레이어로 전달하여 **항등 맵(Identity Mapping)**을 제공합니다.
- 이를 통해 기울기 소멸 문제를 완화하고, 네트워크가 더 깊어져도 학습이 원활하게 이루어집니다.
- 잔차(Residual)를 학습하는 방식으로 더 빠른 수렴 속도를 보입니다.
- 차원이 다를 때는 $\( 1 * 1 \)$ 컨볼루션을 사용하여 입력과 출력을 맞춥니다.

---

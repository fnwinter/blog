---
layout: post
title: "Backpropagation (역전파)"
author: "jungjik.lee"
categories: article
tags: [backpropagation]
---
역전파역전파
**Backpropagation (역전파)**는 인공 신경망(Artificial Neural Network, ANN)에서 **가중치(weight)와 편향(bias)을 학습**하기 위해 사용하는 핵심 알고리즘입니다. 신경망의 출력 오차를 각 층으로 **거꾸로 전파**하면서 가중치를 조정하는 방식으로, **경사 하강법(Gradient Descent)**의 일부분으로 작동합니다.

---

## 📘 **Backpropagation의 동작 원리**
Backpropagation의 핵심 목표는 **손실(loss) 함수의 오차를 최소화**하기 위해 **가중치와 편향을 조정**하는 것입니다. 

1. **순전파 (Forward Propagation)**
   - 입력 데이터를 받아 신경망의 각 층을 통과시키면서 **출력(ŷ, 예측값)을 계산**합니다.
   - 이 과정에서 가중치(weight)와 편향(bias)이 사용됩니다.
   - 최종 출력(ŷ)과 정답(y) 간의 **손실(loss) 값**을 계산합니다.

2. **손실(loss) 계산**
   - 예측된 출력과 실제 정답 사이의 차이를 손실 함수(예: **Cross-Entropy** 또는 **MSE**)로 측정합니다.
   
3. **오차 역전파 (Backward Propagation)**
   - **출력층에서 입력층으로 역방향으로 오차를 전파**합니다.
   - 미분(기울기, Gradient)을 통해 손실 함수의 변화에 대한 가중치의 변화($\( \frac{\partial L}{\partial w} \)$)를 계산합니다.

4. **가중치와 편향 업데이트**
   - **경사 하강법(Gradient Descent)** 또는 **Adam Optimizer**와 같은 최적화 알고리즘을 사용하여 가중치와 편향을 업데이트합니다.
   $\[
   w_{\text{new}} = w_{\text{old}} - \eta \frac{\partial L}{\partial w}
   \]$
   - $\( \eta \)$는 **학습률(learning rate)**으로, 한 번의 업데이트에서 가중치를 얼마나 조정할지를 결정합니다.

---

## 📘 **수학적 설명**
신경망의 출력 노드 $\( \hat{y} \)$에 대한 손실 $\( L \)$을 최소화하려고 할 때, 각 가중치 $\( w \)$에 대해 **손실의 변화율(기울기, gradient)**를 계산합니다.

### **1️⃣ 순전파 (Forward Propagation)**
- 입력 \( x \)에서 시작하여 **가중치 \( w \)**, **활성화 함수 \( f \)**를 거쳐 최종 예측값 $\( \hat{y} \)$를 구합니다.
$\[
a^{(l)} = f(z^{(l)}) \quad \text{(활성화값)}
\]
\[
z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)} \quad \text{(가중합)}
\]$

### **2️⃣ 손실(Loss) 계산**
- 예측값 $\( \hat{y} \)$와 실제값 $\( y \)$의 손실 $\( L \)$을 계산합니다.
$\[
L = - \sum_{i} y_i \log(\hat{y}_i)
\]$

### **3️⃣ 역전파 (Backward Propagation)**
#### **출력층의 미분**
출력층의 가중치에 대한 손실의 변화율 $\(\frac{\partial L}{\partial W}\)$를 구합니다.
$\[
\frac{\partial L}{\partial z^{(l)}} = \hat{y} - y
\]$
여기서 $\( \hat{y} \)$는 예측값, $\( y \)$는 실제값입니다. 

#### **은닉층의 미분**
은닉층의 가중치에 대한 변화율은 연쇄 법칙(Chain Rule)을 사용합니다.
$\[
\frac{\partial L}{\partial W^{(l)}} = \frac{\partial L}{\partial z^{(l)}} \cdot \frac{\partial z^{(l)}}{\partial W^{(l)}}
\]$
여기서 $\(\frac{\partial z^{(l)}}{\partial W^{(l)}} = a^{(l-1)}\)$ 이기 때문에, 은닉층의 미분은 아래와 같이 표현할 수 있습니다.
$\[
\frac{\partial L}{\partial W^{(l)}} = \delta^{(l)} \cdot a^{(l-1)} 
\]$
여기서 $\(\delta^{(l)}\)$는 오차 신호(error signal)로, 다음 층으로 전파됩니다.

#### **편향의 미분**
편향에 대한 미분도 가중치와 유사하게 계산되며, 편향은 모든 입력에 대해 동일하게 적용되므로 단순히 누적합니다.
$\[
\frac{\partial L}{\partial b^{(l)}} = \delta^{(l)} 
\]$

---

## 📘 **연쇄 법칙 (Chain Rule)**
Backpropagation의 핵심은 **연쇄 법칙(Chain Rule)**을 활용해 손실 함수에 대한 각 가중치의 기울기를 계산하는 것입니다. 연쇄 법칙의 기본 개념은 다음과 같습니다.

$\[
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial w}
\]$

---

## 📘 **Backpropagation 예시**
간단한 2층 신경망이 있다고 가정합니다.

1. **순전파:**
   - 입력 $\( x = 0.5 \)$
   - 가중치 $\( w = 0.8 \)$
   - 출력 $\( z = w \cdot x = 0.8 \cdot 0.5 = 0.4 \)$
   - 활성화 함수 $\( f(z) \)$로 Sigmoid 함수 적용
   $\[
   f(0.4) = \frac{1}{1 + e^{-0.4}} \approx 0.5987
   \]$

2. **손실 계산:**
   - 정답 레이블 $\( y = 1 \)$ (원핫 인코딩)
   - 손실 $\( L = -y \cdot \log(\hat{y}) = -1 \cdot \log(0.5987) \approx 0.513 \)$

3. **역전파:**
   - **출력층**: 오차 계산 $\(\frac{\partial L}{\partial z} = \hat{y} - y = 0.5987 - 1 = -0.4013\)$
   - **은닉층**: 가중치의 변화율 $\(\frac{\partial L}{\partial w} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial w} = -0.4013 \cdot 0.5 = -0.2007\)$

---

## 📘 **Why Backpropagation? (왜 사용하는가?)**
1. **효율적인 학습**: 연쇄 법칙을 사용하여 계산 비용을 줄이기 때문에 신경망 학습을 효율적으로 수행할 수 있습니다.
2. **모든 가중치 업데이트 가능**: 여러 층의 가중치가 동시에 업데이트되어 신경망이 학습합니다.
3. **자동 미분 (Autodiff)**: TensorFlow와 PyTorch는 Backpropagation 알고리즘을 자동으로 수행합니다.

---

## 📘 **요약**
- **Backpropagation**은 신경망에서 **오차를 거꾸로 전파**하여 가중치와 편향을 조정하는 과정입니다.
- **순전파**를 통해 예측값을 계산하고, **손실 함수의 기울기(gradient)를 계산**하여 가중치와 편향을 업데이트합니다.
- **연쇄 법칙(Chain Rule)**을 통해 각 층의 변화율을 효율적으로 계산합니다.
- **경사 하강법**을 사용해 가중치와 편향을 업데이트하여 학습이 이루어집니다.

---

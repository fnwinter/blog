---
layout: post
title: "Xavier 초기화"
author: "jungjik.lee"
categories: article
tags: [Xavier init]
---

"Xavier 초기화"는 신경망에서 가중치를 초기화하는 방법 중 하나로, **균등 분포**나 **정규 분포**를 사용하여 가중치를 설정합니다. 이 방법은 신경망의 학습 속도를 향상시키고, **기울기 소실**(vanishing gradient) 또는 **기울기 폭주**(exploding gradient) 문제를 완화하는 데 도움을 줍니다.

### Xavier 초기화의 수학적 정의

1. **균등 분포 초기화**:  
   - 가중치 $\(\mathbf{W}\)$의 초기값은 균등 분포에서 샘플링됩니다.
   $\[
   W \sim U\left( -\sqrt{\frac{6}{n_{\text{in}} + n_{\text{out}}}}, \sqrt{\frac{6}{n_{\text{in}} + n_{\text{out}}}} \right)
   \]$
   여기서:
   - $\( n_{\text{in}} \)$은 입력 뉴런의 수
   - $\( n_{\text{out}} \)$은 출력 뉴런의 수

2. **정규 분포 초기화**:  
   - 가중치 $\(\mathbf{W}\)$의 초기값은 정규 분포에서 샘플링됩니다.
   $\[
   W \sim \mathcal{N} \left( 0, \frac{2}{n_{\text{in}} + n_{\text{out}}} \right)
   \]$
   여기서:
   - 평균은 0
   - 분산은 $\(\frac{2}{n_{\text{in}} + n_{\text{out}}}\)$로 설정됩니다.

---

### **Xavier 초기화의 목적**
Xavier 초기화는 신경망의 각 층에서 가중치를 적절히 초기화하여, 활성화 함수의 출력이 너무 크거나 작지 않게 유지하도록 합니다. 이 방식은 **시그모이드**나 **하이퍼볼릭 탄젠트(tanh)** 같은 활성화 함수를 사용할 때 유용합니다.

---

### **Xavier 초기화의 장점**
- **기울기 소실/폭주 문제 방지**: 네트워크의 깊이가 깊어질수록 기울기 소실이나 폭주가 발생할 수 있는데, Xavier 초기화는 이를 완화하는 데 도움을 줍니다.
- **학습 속도 향상**: 적절한 초기화로 인해 모델이 더 빠르고 안정적으로 수렴할 수 있습니다.
---
layout: post
title: "벡터 임베딩"
author: "jungjik.lee"
categories: article
tags: [vector embedding]
---


### 📘 **벡터 임베딩(Vector Embedding)란?**

**벡터 임베딩(Vector Embedding)**은 고차원 데이터를 고정된 크기의 실수 벡터로 변환하는 방법입니다. 벡터 임베딩의 목표는 복잡한 데이터(텍스트, 이미지, 사용자 행동 등)를 **수학적 공간에 표현**하는 것입니다. 이를 통해 컴퓨터가 더 쉽게 이해하고 연산할 수 있도록 합니다.

---

### 📌 **벡터 임베딩의 개념**
- **정의**: 단어, 문장, 이미지, 사용자 클릭 기록 등 **비정형 데이터**를 **고정 크기의 벡터**로 변환하는 과정.
- **차원(Dimension)**: 벡터의 크기(예: 300차원, 768차원)로, 고차원 공간에서 데이터를 나타냅니다.
- **목적**: 기계 학습 알고리즘에서 데이터 간의 유사성을 계산하거나, 분류 및 회귀 작업을 수행할 수 있도록 데이터의 표현을 단순화합니다.

---

### 📌 **벡터 임베딩이 필요한 이유**
1. **컴퓨터는 숫자로만 계산할 수 있음**  
   - 텍스트, 이미지 등 비정형 데이터를 **수치 데이터**로 변환해야 함.
   
2. **고차원 공간에서 유사도 계산 가능**  
   - 벡터의 코사인 유사도, 유클리디안 거리 등을 사용해 데이터 간 유사성을 쉽게 계산할 수 있음.
   
3. **차원 축소**  
   - 원래 수백만 개의 차원이 될 수 있는 데이터를 더 작은 차원으로 압축하면서도 의미는 유지함.

---

### 📌 **벡터 임베딩의 예시**

1. **텍스트 임베딩 (Word Embedding)**
   - **Word2Vec**: 단어를 벡터로 변환하는 대표적인 모델.
   - **GloVe**: 단어의 동시 발생 행렬을 통해 임베딩 벡터를 학습.
   - **BERT, GPT**: 문장이나 문서 단위로 더 복잡한 문맥을 이해하는 **문장 임베딩**을 생성.

2. **이미지 임베딩**
   - 이미지의 특성을 벡터로 변환해 이미지 간 유사도를 측정.
   - **Convolutional Neural Networks (CNNs)**가 이미지의 임베딩을 추출하는 데 자주 사용됨.

3. **사용자 행동 임베딩**
   - 사용자의 클릭, 구매 기록을 벡터로 변환해 추천 시스템에 사용.
   - 예: **유저의 구매 이력**을 벡터로 변환해 비슷한 취향의 유저를 찾는 데 활용.

4. **음성 임베딩**
   - 음성 데이터를 벡터로 변환해 발화자 인식, 음성 인식 등에 사용.
   - 예: **DeepSpeaker** 모델이 음성 임베딩을 생성.

---

### 📌 **벡터 임베딩의 활용 분야**
| **분야**         | **활용 예시**                     |
|-----------------|----------------------------------|
| **자연어 처리(NLP)** | 문서 분류, 감정 분석, 챗봇, 번역 등 |
| **컴퓨터 비전(CV)**  | 이미지 검색, 얼굴 인식, 객체 탐지  |
| **추천 시스템**     | 유사한 사용자, 상품 추천            |
| **음성 인식**       | 발화자 인식, 음성 명령 인식         |
| **생체 인식**       | 얼굴, 홍채, 지문 인식              |

---

### 📌 **벡터 임베딩의 유사도 측정 방법**
벡터 간의 유사도를 측정하는 방법으로는 다음과 같은 것들이 있습니다.
- **코사인 유사도(Cosine Similarity)**: 두 벡터 간의 각도를 측정합니다.  
  $\[
  \text{Cosine Similarity} = \frac{A \cdot B}{\|A\| \|B\|}
  \]$
- **유클리디안 거리(Euclidean Distance)**: 두 벡터 간의 직선 거리를 계산합니다.  
  $\[
  \text{Euclidean Distance} = \sqrt{\sum_{i=1}^{n} (A_i - B_i)^2}
  \]$
- **내적(Dot Product)**: 벡터의 내적을 통해 유사성을 측정할 수 있습니다. BERT의 임베딩에서 자주 사용됩니다.

---

### 📌 **벡터 임베딩 생성 방법**
1. **신경망 학습을 통한 생성**  
   - **Word2Vec**, **GloVe**: 단어의 동시 발생을 기반으로 벡터를 학습.  
   - **BERT, GPT**: 문맥 정보를 포함한 문장 단위의 임베딩 벡터 생성.

2. **신경망의 중간 레이어 활용**  
   - CNN, RNN, Transformer 모델의 중간 출력을 **임베딩으로 활용**.

3. **사전 훈련된 모델 사용**  
   - **Huggingface Transformers** 라이브러리에서 사전 학습된 BERT, RoBERTa 등을 활용.

---

### 📌 **벡터 임베딩의 한계**
1. **차원의 저주(Curse of Dimensionality)**
   - 차원이 너무 높으면 벡터 공간 내의 모든 점들이 멀리 떨어져 있는 것처럼 보일 수 있습니다.
   
2. **메모리 및 계산 비용**
   - 대규모 데이터셋에 대해 고차원 벡터를 다루면 계산 및 메모리 비용이 높아집니다.

3. **해석의 어려움**
   - 임베딩 벡터는 인간이 직관적으로 해석하기 어려운 경우가 많습니다.

---

### 📌 **벡터 임베딩의 실제 코드 예시 (Python)**
```python
# 1. Word2Vec으로 벡터 임베딩 생성
from gensim.models import Word2Vec

sentences = [["I", "love", "deep", "learning"],
             ["deep", "learning", "is", "fun"],
             ["I", "like", "NLP", "and", "machine", "learning"]]

# 모델 생성 및 학습
model = Word2Vec(sentences, vector_size=100, window=3, min_count=1, sg=0)

# 'learning'의 벡터 확인
vector = model.wv['learning']
print("learning의 임베딩 벡터: ", vector)
```

```python
# 2. BERT를 사용한 문장 임베딩 생성 (Huggingface Transformers)
from transformers import AutoTokenizer, AutoModel
import torch

# BERT 모델 로드
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

# 입력 문장을 임베딩 벡터로 변환
sentence = "I love deep learning"
inputs = tokenizer(sentence, return_tensors='pt')
with torch.no_grad():
    outputs = model(**inputs)
    
# 마지막 레이어의 임베딩 벡터 추출
embeddings = outputs.last_hidden_state.mean(dim=1)
print("문장 임베딩 벡터: ", embeddings)
```

---

### 📌 **정리**
1. **벡터 임베딩**은 텍스트, 이미지, 오디오 등 다양한 데이터를 **고정 크기의 벡터로 변환**하는 기법입니다.
2. **텍스트 임베딩, 이미지 임베딩, 사용자 행동 임베딩** 등 다양한 유형이 있으며, 다양한 분야(추천 시스템, 자연어 처리, 음성 인식 등)에서 활용됩니다.
3. 대표적인 알고리즘으로는 **Word2Vec, GloVe, BERT, CNN** 등이 있습니다.
4. 벡터 간의 유사성을 측정할 때는 **코사인 유사도, 유클리디안 거리**가 자주 사용됩니다.

---

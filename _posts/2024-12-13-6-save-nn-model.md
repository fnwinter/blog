---
layout: post
title: "torch nn.Model 데이터 저장 방법"
author: "jungjik.lee"
categories: article
tags: [save nn Model]
---

**PyTorch의 `nn.Module` 데이터 저장하는 방법**

PyTorch에서 `nn.Module`의 데이터를 저장하는 방법에는 **모델의 가중치(weight)만 저장**하거나, **모델 전체(구조 + 가중치)를 저장**하는 방법이 있습니다. 여기서는 두 가지 방법을 자세히 설명하겠습니다.

---

## 🔍 **1. 모델의 가중치만 저장 및 불러오기**

이 방법은 모델의 **파라미터(가중치와 편향)**만 저장합니다.  
**장점**: 모델 구조를 별도로 정의할 수 있어서 더 유연합니다.  
**단점**: 모델 클래스를 다시 정의해야 불러올 수 있습니다.

### **📘 저장하는 방법**
```python
import torch

# 모델 인스턴스를 생성
model = MyModel()

# 모델의 가중치만 저장 (state_dict)
torch.save(model.state_dict(), 'model_weights.pth')
```

- `model.state_dict()` : 모델의 모든 가중치와 편향 정보를 딕셔너리 형태로 반환합니다.
- `'model_weights.pth'` : 모델의 가중치를 저장할 파일 경로입니다.

---

### **📘 불러오는 방법**
```python
import torch

# 모델 구조를 다시 정의해야 합니다.
model = MyModel()

# 가중치를 불러옵니다.
model.load_state_dict(torch.load('model_weights.pth'))

# 모델을 평가 모드로 설정 (Dropout, BatchNorm 등 비활성화)
model.eval()
```

- `torch.load('model_weights.pth')` : 저장한 state_dict를 불러옵니다.
- `model.load_state_dict()` : 모델의 가중치를 복원합니다.
- `model.eval()` : 모델을 **평가 모드**로 설정하여 Dropout 및 Batch Normalization을 비활성화합니다.

---

### **예시 코드**
```python
import torch
import torch.nn as nn
import torch.optim as optim

# 예시 모델 정의
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 모델 인스턴스 생성
model = MyModel()

# 가중치 저장
torch.save(model.state_dict(), 'model_weights.pth')

# 가중치 불러오기
model2 = MyModel()  # 모델 클래스 정의 필요
model2.load_state_dict(torch.load('model_weights.pth'))
model2.eval()
```

---

## 🔍 **2. 모델 전체(구조 + 가중치) 저장 및 불러오기**

이 방법은 **모델의 구조와 가중치**를 함께 저장합니다.  
**장점**: 모델 클래스를 다시 정의하지 않아도 됩니다.  
**단점**: PyTorch 버전에 종속적일 수 있습니다.  

---

### **📘 저장하는 방법**
```python
import torch

# 모델 인스턴스를 생성
model = MyModel()

# 모델 전체를 저장 (구조 + 가중치)
torch.save(model, 'model_full.pth')
```

- `'model_full.pth'` : 모델 전체(구조 + 가중치)를 저장할 파일 경로입니다.

---

### **📘 불러오는 방법**
```python
import torch

# 모델 전체를 불러옵니다.
model = torch.load('model_full.pth')

# 평가 모드로 전환
model.eval()
```

- `torch.load('model_full.pth')` : 모델의 구조와 가중치 모두 불러옵니다.
- `model.eval()` : 모델을 **평가 모드**로 전환합니다.

---

### **예시 코드**
```python
import torch
import torch.nn as nn

# 예시 모델 정의
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 모델 생성 및 저장
model = MyModel()
torch.save(model, 'model_full.pth')

# 모델 전체 불러오기 (클래스 정의 없이도 불러올 수 있음)
loaded_model = torch.load('model_full.pth')
loaded_model.eval()
```

---

## 🔍 **3. 언제 어떤 방법을 사용할까?**

| **구분**         | **가중치만 저장 (state_dict)**  | **모델 전체 저장 (torch.save(model))** |
|-----------------|---------------------------------|----------------------------------------|
| **파일 크기**    | 작음                             | 큼                                      |
| **클래스 정의 필요** | 필요                             | 불필요                                 |
| **모델 변경**    | 변경 가능                         | 고정됨                                 |
| **이식성**       | 좋음                             | 버전에 민감                             |
| **추천 상황**    | 코드 유지보수가 필요한 경우       | 빠른 복원 또는 재사용이 필요한 경우    |

---

## 🔍 **4. 추가 정보**
### **Optimizer 상태 저장하기**
훈련 중인 모델을 다시 불러올 때, 모델의 파라미터뿐 아니라 **Optimizer의 상태**도 복원해야 합니다.  
이 경우 `state_dict()`를 통해 Optimizer의 상태를 함께 저장할 수 있습니다.

```python
import torch

# 모델 및 옵티마이저 생성
model = MyModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 가중치와 옵티마이저 상태 저장
checkpoint = {
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'epoch': 10,  # 추가로 epoch 정보도 저장 가능
}
torch.save(checkpoint, 'checkpoint.pth')
```

---

### **체크포인트 불러오기**
```python
import torch

# 모델 및 옵티마이저 생성
model = MyModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 체크포인트 불러오기
checkpoint = torch.load('checkpoint.pth')
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']

# 평가 모드로 전환
model.eval()
```

---

### **GPU와 CPU 간 모델 저장 및 불러오기**
- **GPU에서 저장**하고 **CPU에서 불러오기**:
  ```python
  torch.save(model.state_dict(), 'model.pth')
  model.load_state_dict(torch.load('model.pth', map_location=torch.device('cpu')))
  ```

- **CPU에서 저장**하고 **GPU에서 불러오기**:
  ```python
  model.load_state_dict(torch.load('model.pth'))
  model.to('cuda')
  ```

---

## 🔍 **5. 요약**

| **목표**               | **명령어**                              | **설명**                           |
|----------------------|-----------------------------------------|-----------------------------------|
| **가중치만 저장**     | `torch.save(model.state_dict(), 'model.pth')` | 모델의 가중치만 저장                 |
| **가중치 불러오기**   | `model.load_state_dict(torch.load('model.pth'))` | 모델의 가중치 복원                  |
| **모델 전체 저장**     | `torch.save(model, 'model.pth')`         | 모델 구조 + 가중치 전체 저장         |
| **모델 전체 불러오기** | `model = torch.load('model.pth')`        | 모델 구조 + 가중치 전체 불러오기     |
| **체크포인트 저장**    | `torch.save(checkpoint, 'ckpt.pth')`     | 모델, 옵티마이저 상태 및 에포크 정보 저장 |
| **체크포인트 불러오기**| `torch.load('ckpt.pth')`                 | 체크포인트 불러오기                   |

---

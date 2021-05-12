---
layout: post
title: "unity begins"
author: "jungjik.lee"
categories: article
tags: [unity]
---

# Unity 시작
어떻게 보면 꽤 오랫동안 그래픽스 개발을 했음에도 불구하고, 기초부터 배운게 아니라, 업무 하면서 토막 토막으로 배워서 그런지 알긴 아는데, 정확히 아는게 없다는 생각을 많이 했다. 그래서 이번 기회에 아주 기초부터 하나씩 정리해 볼려고 한다.

# 그래픽스 수학
수학을 잘하는 편이 아니라서 대충 이해만 되면 넘어갔던 부분이 많은데 이제부턴 좀 더 정확하게 정리하려고 한다.

## 유니티로 배우는 게임 수학 (1. 삼각 함수)
- 삼각형 : 세개의 정점으로 이루어진 도형, 정점으로 3개의 edge 변이 정해진다.
- 삼각형 내각 : 두 변이 이루는 각, 내각의 합은 180도
- 직각 삼각형 : 내각 중의 하나가 90도
- 피타고라시의 정리 : 밑변^2 + 높이^2 = 빗변^2
- Sine : 높이/빗변
- Cosine : 밑변/빗변
- Tangent : 높이/밑변
- arcsin(sin(x)) = x
- arcsin(sin(x)) = x

~~~C#
[SerializeField]
public float angle = 0.0f;

float radian_angle = angle * Mathf.Deg2Rad;
float sine = Mathf.Sin(radian_angle);
float arcsine = Mathf.Asin(sine);

// angle 과 degree가 같아야 함
float degree = arcsine * Mathf.Rad2Deg;
~~~

- 빗변이 1이면, x 축는 cos(theta), y 축은 sin(theta) 가 된다.
- cos(t)^2 + sin(t)^2 = 1 이 됨
- 코사인 법칙
  - a^2 = b^2 + c^2 - 2 * b * c * cos(theta)

- 라디안
  - 90 degree = 1/2 pi
  - 180 degree = pi
  - 280 degree = 3/2 pi
  - 원주를 구하는 공식이 C = 2 * pi * r(반지름)
  - 반지름이 1인 경우엔 C = 2 * pi 즉 원주를 360로 나눈 것

- 덧셈 정리
  - P점이 (x, y) = (cos(a), sin(a)) 만큼 이동했을 때, 여기서 b 만큼 더 이동한다면, P' (cos(a+b), sin(a+b)) 의 좌표를 구하는 정리
  - sin(a+b) = sin(a) * cos(b) + cos(a) * sin(b)
  - sin(a-b) = sin(a) * cos(b) - cos(a) * sin(b)
  - cos(a+b) = cos(a) * cos(b) - sin(a) * sin(b)
  - cos(a-b) = cos(a) * cos(b) + sin(a) * sin(b)
  - 그러므로 P' = (cos(a) * cos(b) - sin(a) * sin(b), sin(a) * cos(b) + cos(a) * sin(b))
  - P' = (x * cos(b) - y * sin(b), y * cos(b) + x * sin(b))

- 반각 공식
  - cos(theta) = cos(theta / 2 + theta / 2)
  - theta / 2 = t'
  - cos(t' + t') = cos(t') ^ 2 - sin(t') ^ 2 -> 덧셈정리
  - sin(t') ^ 2 + cos(t') ^ 2 = 1 을 대입
  - = 1 - 2sin(t') ^ 2
  - cos(t) = cos(t') ^ 2 - (1 - cos(t') ^ 2)
  - = 2 * cos(t') ^ 2 - 1
  - -> cos(t') ^ 2 = (cos(t) + 1) / 2
  - -> sin(t') ^ 2 = (1 - cos(t)) / 2

- 사인파, 코사인파
  - sin(0) = 0 이고 sin(pi / 2) = 1 주기는 2 * pi
  - cos(0) = 1 이고 cos(pi / 2) = 1, cos(pi * 3/2) = -1

---
layout: post
title: "C# keywords"
author: "jungjik.lee"
categories: article
tags: [c#, unity]
---

# C# 키워드 정리

C# 가이드 [link](https://docs.microsoft.com/ko-kr/dotnet/csharp/)

### :star: internal
- 동일한 어셈블리의 파일에서만 접근 가능

### :star: ?? , ??=
- 왼쪽 연산자가 null 이면 오른쪽 항을 실행하고 결과를 리턴함.
- ??= 왼쪽 연산자가 null 이면 오른쪽 항을 대입 (C# 8.0 에서만 동작)

### :star: realyonly const
- readonly 는 runtime
- const 는 compile time

### :star: nullable ?
- null 이 될 수 있는 타입, null 허용 정적 분석에 활용

### :star: ! (null-forgiving)
- null 이 아님을 선언함
- [NotNullWhen(true)] 를 통해서 컴파일러에게 null 이 아닐 경우 true가 리턴하도록 명시적으로 선언

### :star: delegate
### :star: @
### :star: =>
### :star:stackalloc

### :star: comment
/// 를 타이핑 하면 주석 Template 이 작성 된다.

### :star: #region ~ #endregion
코드를 접을 수 있다.
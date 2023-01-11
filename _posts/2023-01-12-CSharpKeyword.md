---
layout: post
title: "C# keyword"
author: "jungjik.lee"
categories: article
tags: [C#, keyword]
---

# C# 정리
- 흠, 아주 옛날 이야기 이긴 하지만, 나름 내가 MCSD .NET 자격증이 있었다.
- 그래서 C#을 아주 잘 알꺼라 생각헀지만, 한동안 C++ 만 쓰다가, 다시 유니티 다루면서 내가 너무 모르는게 많구나 깨달았다.
- 그리고 C#이 많이 바뀌었구나 라는 걸 알게 되었다.

## 다시 C# 좀 배우기
- C# [Official Link](https://learn.microsoft.com/en-us/dotnet/csharp/) 

## 몰랐던 keyword
- [internal](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/internal)
    - 같은 Assembly 안에서만 접근할 수 있도록 한정해 주는 keyword
- [sealed](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/sealed)
    - 클라스가 상속 받지 못하도록 한정해 주는 keyword
- [partial](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/partial-type)
    - 하나의 클래스를 파일을 나눠서 작성할 수 있도록 해주는 keyword
- [readonly](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/readonly)
    - 생성자에서만 한번 변경할 수 있고, 그 다음부터는 write 할 수 없도록 만듬.
    - const 와 다른 점은 const는 생성자가 아니라 초기화 할 때 값을 한번 정할 수 있지만, readonly는 다른 생성자에서 다르게 값을 초기화 할 수 있음.
- Structure Layout
    - [StructLayoutAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.structlayoutattribute?view=net-7.0)
    - [MemoryLayout](https://www.csharpstudy.com/DevNote/Article/10)
    - Native 함수를 호출하거나 구조체를 파라미터로 전달하고자 할 때, 정확한 메모리 사이즈의 구조체를 생성할 수 있다.
- [ref](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref)
    - 
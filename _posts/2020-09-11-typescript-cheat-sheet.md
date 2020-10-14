---
layout: post
title: "Typescript Cheat sheet"
author: "jungjik.lee"
categories: article
tags: [typescript, web]
---

## Typescript 실행해 보기
 - 앞으로 설명한 예제는 아래의 playground에서 바로 테스트 해볼 수 있습니다.
 - [typescript playground](https://www.typescriptlang.org/play)

## Typescript 란?
 - 대략 javascript에 super set으로 javascrpit를 strong type 언어로 만들기 위해 컴파일 타임에 type check하는 언어.

## Type
- type
<pre><code>
    const block_scope = "live in block" -> const 는 바꿀 수 없는 상수로 block scope를 갖는다.
    let _num_ : number = 10 -> number type으로 선언, let으로 block scope를 갖는다.
    var _string_ : string = "global scope" -> string type으로 선언, var로 파일 내에서 global scope를 갖는다.
    var _big_int_ : bigint = 1000n -> 큰 정수 표시, target이 es2020 이어야 빌드 된다.
    let s : symbol = Symbol('a') -> symbol type으로 선언 유니크한 값으로 구분할 수 있게 한다. 주로 key에 사용
    var key_value: { [key:number] : boolean } = {10:true} -> [key:number] : boolean -> number type key에 boolean type 값의 dict
    private readonly read_only_property : number; -> property에서 사용하는 const
    var array_number : number[] = {1,2,3} -> array를 [] 또는 Array<number> 로 type 정의
    enum Color { RED, BLUE, GREEN } -> enum 정의, 숫자 문자열 섞어서 선언도 가능
    var tuple_type : [number, string, number] = [10, "tuple", 20] -> tuple로 선언 가능
</code></pre>

## Function
- 함수 선언 방법
  * function FunctionName(parameters: number) : return_type { function_body }
  * let FuncName = function (parameters: number) : return_type { function_body }
  * let FuncName = function (parameters: number) : return_type => { function_body } -> arrow function 허용
  * let FuncName = (parameters: number) => body
<pre><code>
</code></pre>

## Class and Interface

## Advanced Type

## Exception

## Asynchronous event handling

## Module




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
~~~javascript
  const block_scope = "live in block" -> const 는 바꿀 수 없는 상수로 block scope를 갖는다.
  let _num_ : number = 10 -> number type으로 선언, let으로 block scope를 갖는다.
  var _string_ : string = "global scope" -> string type으로 선언, var로 파일 내에서 global scope를 갖는다.
  var _big_int_ : bigint = 1000n -> 큰 정수 표시, target이 es2020 이어야 빌드 된다.
  let s : symbol = Symbol('a') -> symbol type으로 선언 유니크한 값으로 구분할 수 있게 한다. 주로 key에 사용
  var key_value: { [key:number] : boolean } = {10:true} -> [key:number] : boolean -> number type key에 boolean type 값의 dict
  private readonly read_only_property : number; -> property에서 사용하는 const
  var array_number : number[] = {1,2,3} -> array를 [] 또는 Array&lt;number&gt; 로 type 정의
  enum Color { RED, BLUE, GREEN } -> enum 정의, 숫자 문자열 섞어서 선언도 가능
  var tuple_type : [number, string, number] = [10, "tuple", 20] -> tuple로 선언 가능
~~~

## Function
- 함수 선언 방법
~~~javascript
  function FunctionName(parameters: number) : return_type { function_body }
  let FuncName = function (parameters: number) : return_type { function_body }
  let FuncName = function (parameters: number) : return_type => { function_body } -> arrow function 허용
  let FuncName = (parameters: number) => body
~~~

- 기본 파라미터
~~~javascript
  function log(message = "empty") {
    // 이런식으로 message 에 기본 파라미터를 넣을 수 있다.
  }
  type Context = { name? : string, age? : number }
  function input(context = {}) {
    // 이런식으로 context에 파라미터를 전달할 수 있다.
  }
~~~

- 함수 호출
  * call, apply, bind
  * log() 그냥 호출
  * log.apply(null, [param1, param2])
    * null 은 thisArg로 함수 안에서 this로 bind
    * 파라미터를 단일 배열로 전달
  * log.call(null, param1, param2)
    파라미터를 바로 전달
  * log.bind(null, params)()
    * call 과 같은데 함수를 리턴

- 제너레이터
  * 이렇게 함수 이름 앞에 *가 있으면 제너레이터이고, 이터러블 반복자를 반환한다.
~~~javascript
function* createFibonacciGenerator() {
    let a = 0;
    while (true) {
        yield a;
    }
}
~~~

- 함수 시그니처
~~~javascript
type print_log = (message: string) => void
~~~
이런 식으로 명시적인 선언을 할 수 있다.

- 제너릭 타잎
~~~javascript
function map<T,U>(array: T[], f: (item: T) => U) : u[] {
    ...
}
~~~

## Class and Interface

- 클래스 선언
~~~javascript
class Human extends Animal {
  constructor (private readonly DNA: string) {
    this.DNA = DNA;
  }

  sleep(time : number) {
    super.sleep()
  }
}
~~~

- public : 누구나 접근 가능, default
- private : 이 클래스의 인스턴스에서만 접근 가능
- protected : 이 클래스와 서브클래스에서만 접근 가능
- this type return이 된다. 그럼 Human().sleep(10).sleep(10) 계속 잘 수 있다.
~~~javascript
abstract class Animal {
  abstract eat(foot : Food): void {}

  sleep(time: number) : this {
      sleep(time)
  }
}
~~~

- 두개의 인터페이스가 합쳐진다.

~~~javascript
interface User {
    name : string
}

interface User {
    age : number
}

class Memeber implements User {
}
~~~

- 인터페이스는 런타임에 아무것도 안하는데 추상 클래스는 자바스크립트를 만든다.
- 클래스, 인터페이스 둘 다 generic 선언을 할 수 있다.
- @decorator 도 가능 experimentalDecorators : true로 tsconfig에서 수정

## Advanced Type
- keyof 연산자
- Record 타입
  - Record&lt;T, U&gt; 이면 T에 U가 다 맵핑 된 값이어야 함.
- 조건부 타입
  - type IsString&lt;T&gt; = T extends string ? true | false
  - type A = IsString&lt;string&gt; // true
  - type B = IsString&lt;number&gt; // false
- infer
- Exclude <T, U> => T 타입 중에 U에 할당할 수 있는 타입
- NonNullable <T> => T에서 null과 undefined를 제외한 버전
- ReturnType <F> => 함수의 return type을 구한다.
- InstanceType <C> => class 의 instance type을 구한다.

## Exception
- return null 보다는 명시적인 throw Error 를...
- throw new RangeError('...')
- return type에 Error 타입을 넣어서 강제로 처리하도록
~~~javascript
try {

}
catch(e) {

}

function parse (birthday: string) : Date | InvalidDateFormatError {
  ...
}
~~~

- Option&lt;T&gt; 은 Some&lt;T&gt; 또는 None 이 될 수 있다.

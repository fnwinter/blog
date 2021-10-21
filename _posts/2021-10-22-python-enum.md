---
layout: post
title: "python enum auto number"
author: "jungjik.lee"
categories: article
tags: [python, enum]
---

# python enum 확장
python으로 FSM(finite-state machine)을 만들어 볼려고 하는데,
FSM을 만들려면 FSM의 상태를 표현하는 enum이 필요합니다.
python에서 enum은 예약어가 아니기 때문에 import를 하던가 직접 구현을 해야 합니다.

이번엔 직접 구현보다느 import 해서 enum package를 사용해 FSM 상태를 표현해 보겠습니다.

우선 python -m pip install enum 으로 설치를 하고, 기본적인 enum 은 아래처럼 구현합니다.
<pre><code>
>>> from enum import Enum
>>> class Color(Enum):
...     red = 1
...     green = 2
...     blue = 3
</code></pre>
이렇게 구현 되면 Color enum type에 red, green, blue 속성이 있다는 것을 표현합니다.
<pre><code>
>>> print(Color.red)
Color.red
</code></pre>
enum type을 반복 할때는 아래 처럼
<pre><code>
>>> for c in Color:
...     print(c)
Color.red
Color.green
Color.blue
</code></pre>
이렇게 할 수 있습니다.
<pre><code>
>>> type = Color.red
>>> type.name
'red'
>>> type.value
1
</code></pre>
또한 각각의 enum 속성은 name, value 값을 갖고 있습니다.

중요한 점은 enum 속성의 name은 중복 될 수 없지만 value는 중복 될 수 있습니다.
그래서 unique 한 value를 만들기 위해서는  @enum.unique 라를 decorator를 명시적으로 넣어줘야 합니다.
<pre><code>
>>> from enum import Enum, unique
>>> @unique
... class Mistake(Enum):
...     one = 1
...     two = 2
...     three = 3
...     four = 3
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/usr/lib/python3.6/enum.py", line 836, in unique
    (enumeration, alias_details))
ValueError: duplicate values found in <enum 'Mistake'>: four -> three
</code></pre>
그리고 enum의 value를 자동적으로 증가 시켜 주기 위해서는 2.7 에서는 Enum을 상속 받은 AutoNumber라는 클래스를 만들어 줘야 합니다.
<pre><code>
>>> class AutoNumber(Enum):
...     def __new__(cls):
...         value = len(cls.__members__) + 1
...         obj = object.__new__(cls)
...         obj._value_ = value
...         return obj

>>> class Color(AutoNumber):
...     RED = ()
...     GREEN = ()
...     BLUE = ()
</code></pre>

하지만 3.x에서는 auto 라는 클래스가 enum package에 들어가 있어서
<pre><code>
>>> from enum import Enum, auto
>>> class Color(Enum):
...     RED = auto()
...     BLUE = auto()
...     GREEN = auto()
...
>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
</code></pre>
이렇게 사용할 수 있습니다.

# 출저
  - https://docs.python.org/3/library/enum.html
  - https://cpython-test-docs.readthedocs.io/en/latest/library/enum.html

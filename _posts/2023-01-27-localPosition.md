---
layout: post
title: "Unity Local Position"
author: "jungjik.lee"
categories: article
tags: [unity, localposition]
---

# Unity localPosition sample.

A라는 GameObject가 있고, B라는 GameObject가 있을 때,
A와 B가 transform.parent 관계라고 하면 둘 사이의 위치는 transform.localPosition으로 알 수 있다.
그런데 만약 둘이 Parent 관계가 아니라고 하면 둘의 상대적인 Position을 어떻게 알 수 있을까?
다행히 unity builtin function으로 제공한다.

~~~C#
    public GameObject a = null;
    public GameObject b = null;
    public GameObject c = null;

    void Start()
    {
        c.transform.parent = b.transform;
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 a_b_localPosition = b.transform.InverseTransformPoint(a.transform.position);
        c.transform.localPosition = a_b_localPosition;
    }
~~~

A와 B는 같은 레벨의 GameObject 이고, B는 C의 Parent이다.
그런데, A와 B의 상대적인 위치로 C를 움직이고 싶다면, 위의 코드처럼 작성하면 된다.
실행해 보면 A를 움직이면, A와 똑같은 위치에 C가 있는 것을 볼 수 있다.

- :link: [Transform.InverseTransformPoint](https://docs.unity3d.com/ScriptReference/Transform.InverseTransformPoint.html)

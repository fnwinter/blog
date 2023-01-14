---
layout: post
title: "C# float array to string vice versa"
author: "jungjik.lee"
categories: article
tags: []
---

# Float array to string
- 갑자기 float array를 string으로 바꾸었다가 다시 받아서 float array로 바꿔야 하는 일이 생겼다.
- ADB 로 float array를 보내고 다시 받아서 그 값을 써야 하는 이상한 요구 사항이 생겼다.

~~~C#
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using UnityEngine;

public class TestScript : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // float to string
        var source_float_array = new float[] { 0.1f, 0.2f, 0.3f, 0.4f, 0.5f };
        var source_byte_array = new byte[source_float_array.Length * sizeof(float)];
        Buffer.BlockCopy(source_float_array, 0, source_byte_array, 0, source_byte_array.Length);

        string base64Text = Convert.ToBase64String(source_byte_array);
        Debug.Log(base64Text);

        // string to float array
        byte[] dest_byte_array = Convert.FromBase64String(base64Text);
        var dest_float_array = new float[dest_byte_array.Length / sizeof(float)];
        Buffer.BlockCopy(dest_byte_array, 0, dest_float_array, 0, dest_byte_array.Length);
        StringBuilder sb = new StringBuilder();
        foreach (float f in dest_float_array)
        {
            sb.AppendFormat("{0}, ", f);
        }
        Debug.Log(sb.ToString());
    }
}
~~~

- 실행하면 결과는 아래와 같이 나와야 한다.
<pre><code>zczMPc3MTD6amZk+zczMPgAAAD8=
UnityEngine.Debug:Log (object)
TestScript:Start () (at Assets/TestScript.cs:18)

0.1, 0.2, 0.3, 0.4, 0.5, 
UnityEngine.Debug:Log (object)
TestScript:Start () (at Assets/TestScript.cs:29)
</code></pre>

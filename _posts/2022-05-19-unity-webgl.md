---
layout: post
title: "unity webgl intergration"
author: "jungjik.lee"
categories: article
tags: [android, system_uid, permission]
---

# 유니티 WebGL 연결 방법

[Unity Document Link](https://docs.unity3d.com/Manual/webgl-interactingwithbrowserscripting.html)


위 링크처럼 WebGL 과 WebAssembly 를 통해 Unity 를 실행할 수 있다.

그런데 여기서 주의 할 것은 아래의 코드를 Asset/Plugins/js_code.jslib 로 저장하고,
<pre><code>mergeInto(LibraryManager.library, {

  Hello: function () {
    window.alert("Hello, world!");
  },

  HelloString: function (str) {
    window.alert(UTF8ToString(str));
  },

  PrintFloatArray: function (array, size) {
    for(var i = 0; i < size; i++)
    console.log(HEAPF32[(array >> 2) + i]);
  },

  AddNumbers: function (x, y) {
    return x + y;
  },

  StringReturnValueFunction: function () {
    var returnStr = "bla";
    var bufferSize = lengthBytesUTF8(returnStr) + 1;
    var buffer = _malloc(bufferSize);
    stringToUTF8(returnStr, buffer, bufferSize);
    return buffer;
  },

  BindWebGLTexture: function (texture) {
    GLctx.bindTexture(GLctx.TEXTURE_2D, GL.textures[texture]);
  },

});
</code></pre>

C# 코드를 아래와 같이 추가한다.

<pre><code>using UnityEngine;
using System.Runtime.InteropServices;

public class NewBehaviourScript : MonoBehaviour {

    [DllImport("__Internal")]
    private static extern void Hello();

    [DllImport("__Internal")]
    private static extern void HelloString(string str);

    [DllImport("__Internal")]
    private static extern void PrintFloatArray(float[] array, int size);

    [DllImport("__Internal")]
    private static extern int AddNumbers(int x, int y);

    [DllImport("__Internal")]
    private static extern string StringReturnValueFunction();

    [DllImport("__Internal")]
    private static extern void BindWebGLTexture(int texture);

    void Start() {
        Hello();
        
        HelloString("This is a string.");
        
        float[] myArray = new float[10];
        PrintFloatArray(myArray, myArray.Length);
        
        int result = AddNumbers(5, 7);
        Debug.Log(result);
        
        Debug.Log(StringReturnValueFunction());
        
        var texture = new Texture2D(0, 0, TextureFormat.ARGB32, false);
        BindWebGLTexture(texture.GetNativeTexturePtr());
    }
}
</code></pre>

만약 Javascript에서 Unity C# 함수를 호출하고 싶으면 아래와 같이 SendMessage 를 통해서 할 수 있다.

<pre><code>MyGameInstance.SendMessage('MyGameObject', 'MyFunction', 5);
</code></pre>

여기서 MyGameInstance는 index.html 파일에서 UnityInstance를 var MyGameInstance = UnityInstance; 미리 저장하고
호출 한다.

그리고 수정한 index.html은 Asset/WebGLTemplates/MyTemplate/index.html 로 저장하고,

Unity의 Player Setting에서 MyTemplate를 선택하면 수정 된 index.html를 복사해서 node 서버를 실행한다.

 - ![WebGLTemplate](https://fnwinter.github.io/assets/img/webgl.PNG)
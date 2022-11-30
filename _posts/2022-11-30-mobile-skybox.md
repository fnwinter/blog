---
layout: post
title: "unity mobile skybox"
author: "jungjik.lee"
categories: article
tags: [unity, mobile, skybox]
---

# unity default skybox
  * skybox가 무겁다라는 건 알고 있었는데, 디자인팀에서 skybox 좀 확인해 달라고 요청이 와서 좀 알아 봤더니, 기본 skybox가
   1.7k Tris, 5.1k Verts 였다.
  * PC면 무리가 없는데, 모바일 환경에서는 상당히 부담스러운 tris 숫자다.
  * 그래서 다시 검색해 봤더니, 유니티에서 제공하는 mobile skybox shader가 있다. Material을 만들고 Mobile/Skybox를 선택하면
   정육면체에 texture를 넣을 수 있고, 이걸 Skybox에 넣어주면
   22 Tris, 56 Vertex가 된다.
  * Solid Color로 바꾸어도 10 tris, 20 Vertexs이기 때문에 거의 늘어나지 않을 걸 알 수 있다.

# status 의 tris/verts
  * 유니티에서 쿼드를 생성하면 tris가 4개가 올라간다. Wired로 보면 분명 tris 2개만 쓰는데, 이상하게 오브젝트 하나 생성하면 4개씩 증가한다. 그래서 좀 이해가 안되서 찾아 봤더니, Light 나 shader에 따라서 사용하는 tris 수를 합친 거라서 그렇게 status에 표시 된다고 한다. 다시 말해 똑같은 mesh를 built render pipe나 urp 에서 렌더링 하게 되면 다른 tris 숫자가 나온다는 말이다.

  * 이것에 대한 설명은 유니티 포럼에 있다. https://answers.unity.com/questions/1539441/why-does-a-single-flat-quad-in-unity-have-10-tris.html



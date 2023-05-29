---
layout: post
title: "ddx,ddy,fwidth"
author: "jungjik.lee"
categories: article
tags: [shader]
---

# ddx, ddy, fwidth
- hlsl, glsl에서 쓰이는 내장함수인데, 내가 잘못 알고 있었던게 있었네, 우선 fragment shader에서는 독립적으로
shader code가 동작해서 옆에 픽셀이 뭐가 있는지 알 수 없다라고 알고 있었는데, ddx,ddy,fwidth 함수를 통하면
옆에 fragment 값이 뭔지 알 수가 있네.
- 사실 유니티 rounded rectangle 코드 보다가 fwidth 이게 무슨 함수지 하고 찾아보다가 알게 된 함수.
- 이게 무슨 함수냐 하면, x축으로 옆에 있는 픽셀과 값 차이를 보여주는 함수가 ddx,이고 ddy는 y축으로 옆에 픽셀과 값 차이를 보여주는함수.
- fwidth는 x축 차이와 y축 차이의 절대값을 더한 함수

- 가장 설명을 잘해준 유튜브 링크 [link](https://www.youtube.com/watch?v=J1n1yPjac1c)
- 이건 설명을 잘해준 링크 [link](https://www.ronja-tutorials.com/post/046-fwidth/)
- 이건 rounded rectangle 링크 [link](https://docs.unity3d.com/Packages/com.unity.shadergraph@6.9/manual/Rounded-Rectangle-Node.html)
- opengl spec 링크 [link](https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml), [link](https://registry.khronos.org/OpenGL-Refpages/gl4/html/fwidth.xhtml)
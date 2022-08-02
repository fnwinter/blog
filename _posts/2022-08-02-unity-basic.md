---
layout: post
title: "unity basic"
author: "jungjik.lee"
categories: article
tags: [unity, basic]
---

# 유니티 개발 로그
 - 유니티로 개발하면서 이것 저것 해본 것들에 대해서 정리해 볼까한다.
 - 사실 개발과 동시에 뭔가 글로 남기는 것이 쉽지는 않다. 이미 개발해서 코드를 남겼기 때문에
 다시 글을 보고 개발할 일은 없을 것 같지만, 그래도 개발하는 과정에서 배운 지식들을 좀 남겨 보는게
 좋을 것 같아서 유니티 개발 로그를 시작해 본다.

# 유니티 시작하기
 - 유니티는 [다운로드](https://unity.com/kr/download) 여기에서 받을 수 있다.
 - 옛날에는 버전별로 링크가 따로 있어서 버전별로 다운로드 받고 설치했는데, 이제는 유니티 허브가 있어서
 허브를 먼저 설치하고 허브에서 필요한 버전과 모듈을 설치할 수 있다.
 - 보통 버전별로 동작하는게 조금씩 달라서 웬만하면 LTS 버전을 다운받기를 추천한다.
 - [유니티 공식 문서](https://docs.unity3d.com/Manual/index.html)
 - [유니티 에셋 스토어](https://assetstore.unity.com/)
 - [유니티 네이버 카페](https://cafe.naver.com/unityhub)
 - [유니티 포럼](https://forum.unity.com/)
	- 개발하다가 뭔가 잘 안되면 포럼을 찾아보면 웬만한 이슈는 다 있다.
	- 유니티가 버그도 많아서, 다들 똑같은 고통을 겪고 있기 때문에 에러 로그를 키워드로 검색하면
	웬만한 에러는 해결책도 같이 찾을 수 있다.
 - [스택오버플로어](https://stackoverflow.com/questions/tagged/unity3d)
	- 갠적으로 스택오버플로어를 좋아하진 않지만, 그래도 간혹 좋은 글도 있기 때문에 링크 남긴다.
 - [라이더](https://www.jetbrains.com/rider/nextversion/)
	- VS Code를 쓰다가 요즘 라이더로 변경해 보고 있다. 라이더가 아직 커뮤니티 버전이 없고,
	유료라서 우선은 EAP 버전으로 사용 중이다. 괜찮다 싶으면 한 번 구매해 볼까 생각한다.
 - [유튜브 강좌 Brackeys](https://www.youtube.com/c/Brackeys)
 - [유튜브 강좌 GabrielAguiarProd](https://www.youtube.com/c/GabrielAguiarProd)

# 유니티 기본
 - GameObject
	- [이벤트 실행 순서](https://docs.unity3d.com/kr/2022.1/Manual/ExecutionOrder.html)
	- ![GameObjectLifeCycle](https://fnwinter.github.io/assets/img/unity/life-cycle.png)
 - Monobehaviour

# 유니티 단축키
 - 마우스 오른쪽 버튼 : 카메라 View Rotate
 - 마우스 가운데 버튼 : Scene에서 카메라 Y,Z 축 이동
 - 마우스 휠 : Scene에서 카메라 X 축 이동 
 - 마우스 오른쪽 버튼 누르고 W,A,S,D : 카메라 좌표 Scene에서 이동하기
 - Q : Hand tool
 - W : Move, E : Rotate, R : Scale
 - T : Rect Tool

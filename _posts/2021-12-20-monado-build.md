---
layout: post
title: "OpenXR runtime"
author: "jungjik.lee"
categories: article
tags: [openxr, runtime, monado]
---

# OpenXR 정리
  - 이전에 설명했듯이, OpenXR은 API Spec이다. 그래서 실제 구현체는 각 벤더들이 해야 한다. 그래서 실제로 어떻게 구현 되어 있는지 알 수 있는 방법은 없다. 벤더들이 자신들이 구현한 Runtime은 소스 공개를 안하니까.
  - 그런데 OpenXR Spec을 정의 하면서 Khronos와 collabora는 같이 Runtime도 개발하게 된다.
  - 그래서 나온 Open Source OpenXR Runtime이 Monado이다.
  - [https://monado.dev/](https://monado.dev/)
  - Monado 소스를 분석하면, OpenXR이 어떻게 동작하는지 조금 알 수 있다.
  - 그래서 이번에는 Monado 빌드 하고 실행해 보는 걸 해보려고 한다.

# Monado 구성
  - Monado 는 Runtime이기 때문에 Monado 하나만 가지고 동작 시킬 수 없다. Monado를 실행하기 위해서는 Monado의 so 파일을 Load하고 OpenXR API와 연결해 주는 Loader도 필요하고, 안드로이드의 경우에는 어떤 OpenXR Runtime을 사용할지 정해주는 Broker도 필요하다. 그리고 Blender나 Godot 같은 엔진에서 OpenXR 을 사용할 수 있도록 해 주는 Plugin 도 필요하다.
  - OpenXR Android Brkoer : 어떤 Runtime을 실행할지 선택할 수 있도록 도와줌
  - OpenXR Loader : Application이 Runtime을 Load 하고 API 를 호출 할 수 있도록 도와줌
  - OpenXR Plugin : Godot 같은 엔진에서 OpenXR 을 사용할 수 있도록 도와주는 Plugin
  - OpenXR Runtime : 실제로 OpenXR API Spec대로 구현 된 구현체

# Monado 빌드
  - Source code
    - Monado git repo
      [https://gitlab.freedesktop.org/monado/monado](https://gitlab.freedesktop.org/monado/monado)
    - OpenXR Loader git repo
      [https://github.com/KhronosGroup/OpenXR-SDK](https://github.com/KhronosGroup/OpenXR-SDK)
    - Android Broker git repo
      [https://gitlab.freedesktop.org/monado/utilities/openxr-android-broker](https://gitlab.freedesktop.org/monado/utilities/openxr-android-broker)
    - Godot plugin
      [https://github.com/GodotVR/godot_openxr](https://github.com/GodotVR/godot_openxr)
    - Android Teapot Sample
      [https://gitlab.freedesktop.org/monado/demos/androidteapots](https://gitlab.freedesktop.org/monado/demos/androidteapots)
      안드로이드 Teapot 예제를 OpenXR로 구현한 샘플이다.
      또한 OpenXR Hpp 프로젝트를 통해서 OpenXR API를 C++ 형태로 구현한 API를 사용하고 있다.

  - Android build
    - Loader는 그냥 빌드하면 된다. 그러면 loader-debug.aar 파일이 생성이 된다.
    - Broker는 빌드 하면 installable broker가 나오는데 그걸 설치하면 된다.
    - Monado도 그냥 Android 프로젝트 열어서 빌드하면 된다.
    - python3 설치 후에 만약 Windows에서 Windows Market에서 설치했다면, 윈도우 설정에서 앱 실행 별칭을 꺼 준다.
    - glslang가 필요하기 때문에 아래 링크에서 다운 받고 압축을 푼 후에 환경 설정에서 PATH를 추가해 줘야 한다.
      - [https://github.com/KhronosGroup/glslang/releases](https://github.com/KhronosGroup/glslang/releases)
    - eigen 받아서 src/external 에 압축 풀기
      - [https://eigen.tuxfamily.org/index.php?title=Main_Page](https://eigen.tuxfamily.org/index.php?title=Main_Page)
      - 윈도우의 경우에 아래와 같이 FindEigen3.cmake에 PATH를 넣어준다.
      <pre><code>
      +set(EIGEN3_ROOT "C:\\...\\monado\\src\\external\\eigen-3.4.0")
      +set(EIGEN3_INCLUDE_DIR "C:\\...\\monado\\src\\external\\eigen-3.4.0")
      </code></pre>

# Monado 코드를 보면서...
  - 이제 아직 지원하지 않는 Monado Unity Plugin이나 Unreal Plugin도 만들 수 있을꺼 같다. 그리고 전체적으로 OpenXR이 어떻게 동작하고 AR/VR을 위해서는 무슨 기능이 필요한지 알 것 같다.
  - 이제 각각의 기능에 대해서 세부적으로 좀 정리를 해봐야 겠다.
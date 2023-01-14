---
layout: post
title: "XR Forveated Rendering"
author: "jungjik.lee"
categories: article
tags: [OpenXR, Foveated Rendering]
---

# What's Foveated Rendering.
- Foveated Rendering은 VR 또는 XR에서 GPU 리소스를 절약하기 위해서
시야에 들어오는 모든 이미지를 다 섬세하기 그리는 것이 아니라,
중심 시력 부분만 자세하게 그리고, 나머지 주변 시력은 흐릿하게 렌더링해서 그리는 기술을 말한다.
- 보통 눈동자를 따라서 중심 시력 위치를 계산해야 되지만, Eye Tracking 기능을 지원하지 않을 경우,
그냥 중심 부분만 자세하게 그리고 나머지는 흐릿하게 그린다. 이런 기능을 Fixed Foveated Rendering이라고 한다.
- 반면에 Eye Tracking을 통해 동공 방향의 벡터를 구하고, 이를 통해 중심 시야가 바라보는 화면의 위치를
구해서, Foveated Rendering을 하는 것을 Dynamic Foveated Rendering이라고 한다.
- 또는 GPU의 사용량에 따라서 Foveated Rendering 영역의 크기를 변경해 주는 기능을 말한다.
- 그런데 Dynamic Foveated Rendering을 위해서 Eye Tracking 하게 되면, 사실 GPU resource를 줄이는데,
큰 효과를 얻지 못할 수 있다. 그래서 그냥 FFR만 사용하는 경우도 있다. 그리고 해상도가 낮으면 Foveated Rendering
효과가 크지 않을 수 있다. 반면에 해상도가 높아질 수록 GPU 사용이 많아 질 수 있고, 그러면 Foveated Rendering이 효과가 높아질 수 있다..

# OpenXR Foveated Rendering
## OpenXR에서 Foveated Rendering을 구현하기 위한 함수
- xrCreateFoveationProfileFB
- xrDestroyFoveationProfileFB
- XrSwapchainImageFoveationVulkanFB

- OpenXR에서 정의한 Foveated Rendering Level
    - XR_FOVEATION_LEVEL_HIGH_FB 가장 높은 렌더링 레벨이고 높을 수록 넓은 영역이 흐릿하게 그려진다.
<pre><code>// Provided by XR_FB_foveation_configuration
typedef enum XrFoveationLevelFB {
  XR_FOVEATION_LEVEL_NONE_FB = 0,
  XR_FOVEATION_LEVEL_LOW_FB = 1,
  XR_FOVEATION_LEVEL_MEDIUM_FB = 2,
  XR_FOVEATION_LEVEL_HIGH_FB = 3,
  XR_FOVEATION_LEVEL_MAX_ENUM_FB = 0x7FFFFFFF
} XrFoveationLevelFB;

</code></pre>

## Foveated Rendering을 구현하기 위한 다른 참조 링크
- 퀄컴에서 정의한 Foveated Rendering을 위한 Texture Type / Fragment Density Map
    - Qualcomm에서는 FR을 구현하기 Fragment Density Map이라는 Extension을 만들었다.
    - [evolution-high-performance-foveated-rendering-adreno](https://developer.qualcomm.com/blog/evolution-high-performance-foveated-rendering-adreno)
    - [improving-foveated-rendering-fragment-density-map-offset-extension-vulkan](https://developer.qualcomm.com/blog/improving-foveated-rendering-fragment-density-map-offset-extension-vulkan)
    - OpenGL
        - [QCOM_texture_foveated](https://registry.khronos.org/OpenGL/extensions/QCOM/QCOM_texture_foveated.txt)
    - Vulkan
        - [VK_EXT_fragment_density_map](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_EXT_fragment_density_map.html)

- Oculus에서 Foveated Rendering을 활성화 하기 위한 방법
    - [unity-fixed-foveated-rendering](https://developer.oculus.com/documentation/unity/unity-fixed-foveated-rendering/)
    - 아쉽게 오큘러스 외엔 OpenXR 표준으로 Foveated Rendering을 구현한 곳은 없는 것 같다.

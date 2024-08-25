---
layout: post
title: "Cherry NAS and Reflex"
author: "jungjik.lee"
categories: article
tags: [cherry nas, reflex, flask]
---

# Reflex 회고
- 개인 Toy project 하려고 몇 가지 Front/Backend library를 사용해 보았다.
- 처음에는 Bootstrap 과 flask 로 개발하려고 하였는데, frontend 개발하는 것이 어려웠다.
- 몇 가지 이유가 있었는데, 미적 감각과, Javascript/CSS를 배우고 싶지 않은 마음으로 프로젝트를 진행하기 어려웠다.
- 그러다가 Reflex (구 pynecon)을 보았고 파이썬 만으로 front/backend를 동시에 개발할 수 있었으며,
- Javascript/CSS를 배우지 않아도 되는 장점이 좋아 보였다.
- 또한 파이썬 만으로 개발이 가능했고, React를 써 보았기 때문에 쉽게 배울 수 있었다.
- 하지만 사용하면서 몇 가지 단점을 발견하였고, 이 단점이 생각보다 크리티컬해서 다시 Reflex 사용을 재고해야 했다.
- 그중 큰 문제는 다른 경로의 assets은 불러 올 수 없다는 치명적인 단점이 있었다.
- 그래서 다시 flask + frontend library로 개발하려고 한다.


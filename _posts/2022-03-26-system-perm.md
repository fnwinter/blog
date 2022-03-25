---
layout: post
title: "android permission"
author: "jungjik.lee"
categories: article
tags: [android, system_uid, permission]
---

# 오랫만에 안드로이드 개발
 - system uid를 갖고 있는 App이 FileProvider로 파일을 전달하려고 하니 Permission Error가 났다.
 - 이유를 찾아보니까, 아래 링크처럼 프레임워크에서 Permission 에러를 내뱉고 있었고,
 - 유일하게 셋팅만 예외처리를 하고 있었다.
 - 만약 이 기능이 정말 필요하다고 하면, 아래의 링크에서 
 - [UriGrantsManagerService.java](https://android.googlesource.com/platform/frameworks/base/+/master/services/core/java/com/android/server/uri/UriGrantsManagerService.java)
 - 셋팅처럼 예외 처리를 하면 된다.
 - [ref blog](https://blog.karthisoftek.com/a?ID=01700-8f3f34f5-7cdd-4c09-87e9-71296d2a54c8)

# 그리고 느낀 점
 - 난 개인적으로 kotlin 별로다. 짧게 쓸 수 있는 건 좋은데, companion object와 생성자는 너무 이상하다.
 - 안드로이드 문서는 정말 개판이다. deprecated 된 API도 최신 가이드에 나오고, 전체 코드도 아니고 약올리 듯 샘플 코드의 일부만 보여준다. 나머지는 유추해서 짜라는 건가 아니면 프레임 워크를 보라는 건가?
 - 다시 옛날 팝업 메뉴 구현할 때가 생각나네, 리플렉션으로 아무리 sub classing 하려고 해도 안되서 찾아보니까, 구글도 hacky하게 해결하고 주석 남겨 놓은거 보고, 얘들도 사람이구나 싶었는데, 이거 보니까 또 그렇네.

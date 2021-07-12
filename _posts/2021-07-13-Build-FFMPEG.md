---
layout: post
title: "Build FFMPEG"
author: "jungjik.lee"
categories: article
tags: [ffmpeg, toy project]
---

# 서론
 - 자주 글을 남기고 싶은데, 습관이 안되어 있다 보니까, 깜빡하고 지나가게 된다.
 - 하지만 이번에는 toy project에 쓰일 ffmpeg을 빌드해 보려고 한다.

# 갑자기 왜 ffmpeg build?
 - toy project에서 unity의 render texture를 ffmpeg으로 opencv에 전달해 주는 프로그램을 만들고 있다. 용도는 opencv를 좀 배워보고 심심할 때 deep learning 도 좀 돌려 볼까 하는 생각에 synthetic data generating 용으로 만들려고 한다.
 - 그런데 현재 ffmpeg command 를 써서 만들다 보니까, 좀 느린감이 있어서 dll로 빌드해서 직접 메모리를 전달해 줄까 한다.

# ffmpeg 준비물
 - https://sourceforge.net/projects/mingw/
   - 다운로드 받아서 바로 설치
   - MinGW Installation Manager에서 Basic Setup에서 다음의 package 설치
   - mingw32-base, msys-base
   - 윈도우 시스템 속성에서 환경 변수에서 다음의 PATH를 추가
   - C:\MinGW\bin
   - C:\MinGW\msys\1.0
   - C:\MinGW\msys\1.0\bin
 - https://yasm.tortall.net/
   - 다운로드에서 Win64.exe 를 받아서 아래의 폴더에 yasm.exe 이름으로 저장
   - C:\MinGW\bin
 - FFMPEG 소스 코드
   - git config --global core.autocrlf false
   - git clone https://github.com/FFmpeg/FFmpeg.git

# Let's Build
 - cmd.exe 실행 후 msys.bat 실행
 - cd ffmpeg_path
 - ./configure --arch=x86_64 --enable-stripping --disable-w32threads  --disable-static --enable-shared --enable-version3 --disable-doc
 - make -j 8
 - troubleshooting
   - error:'ERROR_NOT_ENOUGH_MEMORY' undeclared 이런 컴파일 에러 나오면 아래 헤더 파일 추가
   - #include "winerror.h"

# Test

# 코드 분석

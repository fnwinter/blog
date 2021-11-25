---
layout: post
title: "프로그램 설치 하기"
author: "jungjik.lee"
categories: article
tags: [new start]
---

1. winget 설치하기
    * 앱 설치 관리자 설치 하기 [Link](https://www.microsoft.com/en-us/p/app-installer/9nblggh4nns1?activetab=pivot:overviewtab)
2. winget 으로 자주 쓰는 프로그램 설치하기
    * winget install Notepad++ --exact
    * winget install 7-Zip --exact
    * winget install Paint.Net
    * winget install Telegram -s winget3. python3 alias 설정 변경
    * winget install vscode
    * winget install Steam -s winget
    * winget install ridibooks
    * winget install PowerToys -s winget
    * winget install Ubuntu --id Canonical.Ubuntu.2004 -s winget
    * winget install potplayer --id XP8BSBGQW2DKS0
    * winget install kakaotalk
    * winget install Git --id Git.Git -s winget
    * winget install terminal -s winget
    * winget install python3
3. python3 alias 설정 변경
    * 설정 > 앱 > 앱 실행 별칭 > 앱 설치 관리자에서 python.exe python3.exe 끔
4. 안드로이드 스튜디오를 쓴다면, 코드 폴더 예외 처리 하기
    * Windows 보안 > 바이러스 및 위협 방지 > 바이러스 및 위협 방지 설정 (설정관리) > 제외
    * 다음의 폴더 추가
      * C:\Users\\<계정>\AndroidStudioProjects
      * C:\Users\\<계정>\AppData\Android\Sdk
5. ssh 폴더 복사 하기
    * Powershell로 ~/.ssh 에 복사한다.
    * cp -r /mnt/c/Users/<계정>/.ssh/ ~/
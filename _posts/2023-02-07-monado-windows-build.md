---
layout: post
title: "Monado OpenXR Runtime Window build"
author: "jungjik.lee"
categories: article
tags: [monado, openxr, runtime, 3d tv]
---

# Monado OpenXR Runtime Window build

결혼 할 때 산 3D TV가 딱히 쓸모가 없었는데, 양안으로 렌더링 하면 <br/>
3D 효과를 얻을 수 있을 것 같아서 한 번 시도해 보았다. <br/>

우선 Monado 를 빌드하려면 vcpkg 를 설치해야 된다.<br/>
https://vcpkg.io/ 여기서 git clone https://github.com/Microsoft/vcpkg.git 실행하고,<br/>
.\vcpkg\bootstrap-vcpkg.bat 실행한 다음에, clone 한 path를 환경 변수 PATH에 넣어준다.<br/>
vcpkg install 을 실행할 수 있으면 준비 끝.<br/>

Monado Code (https://gitlab.freedesktop.org/monado/monado)<br/>
git clone https://gitlab.freedesktop.org/monado/monado.git<br/>
여기서 monado 소스를 clone 한다.<br/>

Powershell을 실행하고, 터미널의 스크립트 실행 권한을 바꾼다.<br/>
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser<br/>

추가로 Visual Studio 가 설치 되어 있어야 한다.<br/>

그리고 아래와 같이 수정을 한다.<br/>

<pre><code>
diff --git a/.gitlab-ci/windows/monado_build.ps1 b/.gitlab-ci/windows/monado_build.ps1
index 8751ef20..d54d9c53 100644
--- a/.gitlab-ci/windows/monado_build.ps1
+++ b/.gitlab-ci/windows/monado_build.ps1
@@ -29,7 +29,7 @@ Write-Host "Compiling Monado"
 $sourcedir = (Resolve-Path "$PSScriptRoot/../..")
 $builddir = Join-Path $sourcedir "build"
 $installdir = Join-Path $sourcedir "install"
-$vcpkgdir = "c:\vcpkg"
+$vcpkgdir = "C:\Users\__user_id__\Desktop\dev\monado\vcpkg"
 $toolchainfile = Join-Path $vcpkgdir "scripts/buildsystems/vcpkg.cmake"

 Remove-Item -Recurse -Force $installdir -ErrorAction SilentlyContinue
@@ -44,7 +44,7 @@ Write-Output "toolchainfile:$toolchainfile"
 # if (!$installPath) {
 #     throw "Could not find VS2022 using vswhere!"
 # }
-$installPath = "C:\BuildTools"
+$installPath = "C:\Program Files\Microsoft Visual Studio\2022\Professional"
 Write-Output "installPath: $installPath"

 # We have to clear this because some characters in a commit message may confuse cmd/Enter-VsDevShell.
</code></pre>

그리고  .\.gitlab-ci\windows\monado_build.ps1 를 실행한다.
그러면 .\monado\build\src\xrt\targets\service 폴더에 monado-service.exe 서비스 실행 파일이 생성이 된다.

이 파일을 실행 시키고, 유니티에 OpenXR 설정을 한다.

유니티에서 Windows > Package Manager 에서 OpenXR Plugin 을 설치한다.

Project Setting에서 XR Plug-in Management 에서 Play Mode OpenXR Runtime 메뉴에서 Other를 선택하고,

.\monado\build 폴더의 openxr_monado-dev.json 파일을 선택해 준다.

그리고 유니티 Play 버튼을 누르면 새로운 창이 뜨면서 양안으로 보인다. 이걸 TV 화면으로 옮기고

양안 모드를 선택하면 3D 게임을 할 수 있다.
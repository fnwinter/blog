---
layout: post
title: "Android HAL"
author: "jungjik.lee"
categories: article
tags: [android, hal]
---

Android HAL(Hardware Abstraction Layer) 개발 방법에 대해 설명드리겠습니다. HAL은 Android 운영체제에서 하드웨어와 소프트웨어 간의 추상화 레이어를 제공하여, 애플리케이션이 하드웨어에 직접 접근하지 않고도 하드웨어 기능을 사용할 수 있게 합니다. HAL을 개발하려면 다음과 같은 단계로 진행할 수 있습니다.

### 1. **개발 환경 설정**
   - **Android NDK 설치:** HAL 개발을 위해서는 Native Development Kit(NDK)가 필요합니다. NDK를 설치하고, 환경 변수를 설정합니다.
   - **Android 소스 코드 다운로드:** Android의 AOSP(Android Open Source Project) 소스 코드를 다운로드하여 설정합니다. HAL은 주로 이 소스 코드 내에서 작업하게 됩니다.

### 2. **HAL 인터페이스 정의**
   - **HAL 인터페이스 정의 파일 작성:** Android에서는 HAL 인터페이스를 `.hal` 파일로 정의합니다. 이는 HIDL(HAL Interface Definition Language)로 작성됩니다.
   - **HIDL 컴파일:** HIDL 파일을 작성한 후, 이를 컴파일하여 Stub 코드와 인터페이스 코드를 생성합니다.

### 3. **HAL 구현**
   - **HAL 인터페이스 구현:** 인터페이스를 정의한 후, 이를 실제로 구현하는 코드를 작성합니다. 이 구현은 보통 C/C++로 작성되며, 하드웨어 드라이버와 상호작용합니다.
   - **구현된 HAL 모듈 컴파일:** 구현된 HAL 모듈을 컴파일하여 Android 시스템에서 사용할 수 있는 `.so`(Shared Object) 라이브러리를 생성합니다.

### 4. **HAL 모듈 등록**
   - **Android.mk 또는 Android.bp 파일 수정:** 생성한 HAL 모듈을 Android 빌드 시스템에 등록합니다. 이를 위해 Android.mk 또는 Android.bp 파일을 수정하여, HAL 모듈이 빌드 프로세스에 포함되도록 합니다.
   - **HAL 등록:** HAL 모듈은 `hw_module_t` 구조체를 통해 Android 시스템에 등록됩니다. 이 구조체에 HAL 모듈의 정보와 함수 포인터를 설정합니다.

### 5. **테스트 및 디버깅**
   - **Android Emulator 또는 실제 디바이스에서 테스트:** HAL 모듈이 정상적으로 작동하는지 확인하기 위해, 에뮬레이터나 실제 디바이스에서 테스트합니다.
   - **로그 및 디버깅:** 문제가 발생할 경우, `logcat`을 통해 로그를 확인하고, gdb를 사용하여 디버깅합니다.

### 6. **HAL 서비스화**
   - **서비스로 등록:** 구현된 HAL 모듈을 시스템 서비스로 등록하여, 다른 애플리케이션이나 서비스가 이를 사용할 수 있도록 합니다.
   - **AIDL(Android Interface Definition Language):** 필요에 따라 AIDL을 사용하여 애플리케이션이 HAL을 통해 하드웨어에 접근할 수 있는 인터페이스를 정의할 수 있습니다.

### 7. **빌드 및 배포**
   - **전체 시스템 빌드:** HAL 모듈을 포함하여 전체 Android 시스템 이미지를 빌드합니다.
   - **디바이스에 배포:** 빌드된 이미지를 디바이스에 플래싱하여, HAL 모듈이 정상적으로 동작하는지 최종 확인합니다.

위의 과정을 통해 Android HAL을 개발할 수 있습니다. HAL 개발은 하드웨어와 소프트웨어 간의 복잡한 상호작용을 포함하므로, 하드웨어에 대한 깊은 이해와 C/C++ 프로그래밍에 대한 숙련도가 필요합니다.

-------------------------------------

Android HAL 구현을 이해하는 데 도움이 될 수 있는 간단한 샘플 코드를 제공합니다. 이 예제는 매우 기본적인 형태의 HAL 모듈을 구현하며, 디바이스에서 간단한 정보를 제공하는 HAL을 만들어보겠습니다.

### 1. HAL 인터페이스 정의 (`.hal` 파일)
먼저, `hello_hal.hal` 파일을 작성합니다. 이 파일은 HAL 인터페이스를 정의하는데 사용됩니다.

```hal
package android.hardware.hello@1.0;

interface IHello {
    string sayHello();
};
```

### 2. HIDL 컴파일
HIDL 파일을 작성한 후, 이를 컴파일하여 Stub 코드를 생성합니다. 다음과 같은 명령어를 사용합니다.

```bash
hidl-gen -o . -r android.hardware:hardware/interfaces -L c++-impl -r android.hidl:system/libhidl/transport hello_hal.hal
```

이 명령어는 `IHello.h`와 같은 헤더 파일을 생성합니다.

### 3. HAL 구현 (`hello_hal.cpp`)
이제 HAL 인터페이스를 구현하는 코드를 작성합니다. `hello_hal.cpp` 파일을 생성합니다.

```cpp
#include <android/log.h>
#include "IHello.h"

#define LOG_TAG "HelloHal"

namespace android {
namespace hardware {
namespace hello {
namespace V1_0 {
namespace implementation {

class Hello : public IHello {
public:
    // sayHello() 함수 구현
    Return<::android::hardware::hidl_string> sayHello() override {
        ALOGI("Hello from HAL!");
        return "Hello from HAL!";
    }
};

// HAL 모듈 인스턴스 생성
extern "C" IHello* HIDL_FETCH_IHello(const char* name) {
    return new Hello();
}

}  // namespace implementation
}  // namespace V1_0
}  // namespace hello
}  // namespace hardware
}  // namespace android
```

### 4. Android.mk 또는 Android.bp 작성
HAL 모듈을 빌드하기 위해 `Android.bp` 파일을 작성합니다.

```bp
cc_library_shared {
    name: "android.hardware.hello@1.0-impl",
    srcs: ["hello_hal.cpp"],
    shared_libs: [
        "libhidltransport",
        "libhwbinder",
        "liblog",
    ],
    cflags: ["-Wall"],
    export_include_dirs: ["include"],
}

hidl_interface {
    name: "android.hardware.hello",
    root: "android.hardware",
    vendor_available: true,
    version: "1.0",
    srcs: ["IHello.hal"],
}
```

### 5. HAL 모듈 등록 (`Android.mk`)
HAL 모듈을 시스템에 등록하는 코드입니다.

```makefile
LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := hello_hal.default
LOCAL_SRC_FILES := hello_hal.cpp
LOCAL_MODULE_TAGS := optional
LOCAL_SHARED_LIBRARIES := liblog libhwbinder libutils
include $(BUILD_SHARED_LIBRARY)
```

### 6. 빌드 및 테스트
모든 파일을 작성한 후, 전체 Android 빌드를 실행하여 HAL 모듈을 빌드합니다.

```bash
source build/envsetup.sh
lunch aosp_your_device-userdebug
make -jN
```

### 7. 서비스에서 사용
빌드가 완료된 후, 디바이스에서 해당 HAL 모듈이 제대로 동작하는지 확인합니다. 이를 위해 HAL 모듈을 호출할 수 있는 간단한 테스트 애플리케이션을 작성하거나 `adb shell`을 사용하여 직접 HAL을 호출할 수 있습니다.

위 샘플 코드는 매우 간단한 형태의 HAL 구현입니다. 실제 프로젝트에서는 더 복잡한 데이터 처리와 하드웨어와의 상호작용이 필요할 수 있습니다. HAL 개발에 필요한 다양한 기술과 도구들을 사용하여 더 복잡한 기능을 구현할 수 있습니다.

---------------------------------------

구현한 HAL을 사용하기 위한 간단한 테스트 애플리케이션 코드를 제공하겠습니다. 이 애플리케이션은 HAL에서 제공하는 `sayHello` 함수를 호출하여 결과를 출력하는 역할을 합니다.

### 1. **테스트 애플리케이션 코드 (`HelloTest.java`)**

Android 애플리케이션에서 HAL을 호출하는 방법은 AIDL을 사용하는 것과 유사합니다. 다음은 Java로 작성된 간단한 Android 애플리케이션 코드입니다.

```java
package com.example.hellotest;

import android.os.Bundle;
import android.util.Log;
import androidx.appcompat.app.AppCompatActivity;
import android.hardware.hello.V1_0.IHello;
import android.os.RemoteException;
import java.util.NoSuchElementException;

public class HelloTest extends AppCompatActivity {

    private static final String TAG = "HelloTest";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        try {
            // IHello HAL 인터페이스 가져오기
            IHello helloService = IHello.getService();
            if (helloService != null) {
                // sayHello 함수 호출
                String response = helloService.sayHello();
                Log.d(TAG, "HAL response: " + response);
            } else {
                Log.e(TAG, "Failed to get HAL service.");
            }
        } catch (RemoteException e) {
            Log.e(TAG, "RemoteException occurred while communicating with HAL", e);
        } catch (NoSuchElementException e) {
            Log.e(TAG, "IHello HAL service not found", e);
        }
    }
}
```

### 2. **`AndroidManifest.xml`**

애플리케이션을 정상적으로 실행하려면 `AndroidManifest.xml` 파일에 필요한 권한과 액티비티를 등록해야 합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.hellotest">

    <application
        android:allowBackup="true"
        android:label="HelloTest"
        android:supportsRtl="true"
        android:theme="@style/Theme.AppCompat.Light.DarkActionBar">
        <activity android:name=".HelloTest">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

### 3. **빌드 및 실행**

이제 애플리케이션을 빌드하고, 디바이스에서 실행하여 HAL의 `sayHello` 메서드를 호출해볼 수 있습니다. 디바이스에 설치한 후, `adb logcat` 명령어를 사용하여 로그를 확인하고, HAL로부터 반환된 메시지를 확인합니다.

```bash
adb logcat | grep HelloTest
```

이 애플리케이션은 HAL에서 제공하는 기능을 호출하고 그 결과를 출력하는 간단한 예제입니다. 실제로는 HAL을 호출할 때 발생할 수 있는 다양한 예외 처리와 더 복잡한 로직을 추가할 수 있습니다.
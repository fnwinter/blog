---
layout: post
title: "web assembly"
author: "jungjik.lee"
categories: article
tags: [web assembly, emscripten, rust]
---

# Web Assembly ?

## Web Assembly는 대략 이런 특징이 있습니다.
- Web Assembly 는 브라우저 (또는 node.js) 자바스크립트 엔진에 포함 된 stack machine 입니다.
- byte code를 바로 실행하기 때문에, 자바스크립트에서 런타임에 실행 되는 AST 만드는 작업이 필요 없고, 낮은 수준의 JIT만 동작하기 때문에 성능적 부분에서 훨씬 빠릅니다.
- 자바스크립트 엔진에서 동작하기 때문에 Web API를 호출 할 수 있고, same-origin 같이 브라우저 보안 정책을 따르기 때문에 보안에 안전합니다.
- byte code 외에 읽을 수 있는 s-expression 문법으로 표현 가능하고, 브라우저에서 디버깅 할 수 있습니다.
- C/C++/Python/Rust 등 다양한 언어로 작성 된 코드도 LLVM을 통해 byte code를 생성할 수 있습니다.
- Web 생태계에 포함 되어 있기 떄문에 JRE/NaCl/ActiveX 처럼 별도의 플러그인을 설치할 필요가 없습니다.

구글에서 NaCl/PNaCl을 밀고 있을 때, 모질라에서는 asm.js를 만듭니다. 구글의 NaCl은 C/C++을 빌드해서 네이티브 코드를 생성하면 자바스크립트 인터페이스를 통해 이를 로드해서 실행 시켜주는 방법이라 구 시대 유물이라 평가 받는ActiveX(?)와 유사합니다. 물론 NaCl toolchain으로 컴파일 단계에서 시스템콜을 완전히 방지해, 그냥  실제로 시스템 접근에 필요한 호출은 브라우저를 통해서 할 수 있도록 만들었다 것을 제외하면 말이죠.
그리고 별도의 툴체인, 웹 개발자에게는 어려운 개발 환경이라 모두 외면할 수 밖이 없는 플랫폼이었죠.

하지만 모질라는 전혀 다른 방법으로 브라우저 성능을 높이고자 합니다. 그냥 assembly 언어 같은 형식으로 브라우저의 가상 머신에서 실행하면 되지 않을까라고요. 일반적인 개발자가 봐도 후자가 더 멋지죠.  http://asmjs.org/

이후에 마이크로소프트 엣지가 asm.js 그룹에 합류하고, 애플이 나중에 합류 하므로써, 표준을 만드는 쪽으로 가게 되었고, 후에 구글도 NaCl/PNaCl을 포기하고 WebAssembly 표준화에 가담하게 됩니다.

그리고 지금은 익스플로러을 제외하고는 거의 대부분의 모던 브라우저에서 지원하고 있습니다.

* 참고 : stack machine 은 레지스터를 사용하는 대신 스택을 사용하는 가상 머신으로 성능은 레지스터 방식보다 느리지만 개발이 용이 하다고 합니다. https://en.wikipedia.org/wiki/Stack_machine

개인적인 생각은 앞으로 웹 기술 중에서 가장 핫한 기술이 되지 않을까 싶습니다.

그 이유는 다양한 언어로 개발할 수 있다는 점 (굳이 Javascript로 개발하지 않아도 된다는 점), 성능이 빠르다는 점, 추후에 가비지 컬렉팅 기술이 들어간다면 메모리도 효율적으로 쓸 수 있다는 점, 또는 개인적으로 모듈화가 편할 수 있고 bundling,minify,uglify 등의 비효율적인 부분이 없다는 점, 나중에 Web API를 바로 호출 할 수 있다면 엄청난 성능 개선이 나오지 않을까 싶네요.

# Rust with WebAssembly

예전에 옆에 앉은 동료가 rust를 공부해서 호기심에 나도 rust를 대략 1주일 정도 본 적이 있었습니다.
언어의 컨셉도 너무 멋지고, 신기한 문법도 많아서 재미있게 공부했는데, 막상 공부하고 나서 주 사용 언어도 아니고 개발하고 있는 프로젝트에 적용할 수 있는 것도 아니라서 문법도 거의 까먹고 있었습니다.

그런데 emscripten의 target로 rust가 지원이 되서 다시 한 번 rust로 wasm을 컴파일하고 브라우저에서 예제를 실행해 보려고 합니다.
SDL에 emscripten port도 있어서 개인적으로는 이런 조합으로 웹앱을 개발해 본다면 참신할 것 같은데 막상 시도하려니 뭘 만들어야 될지도 안떠오르고,
그래서 우선 예제 실행 방법만 살펴 보도록 하겠습니다.

구글링을 해보니까 rust를 프로젝트를 개발하는 방법이 두 가지 정도 있는 것 같은데, 하나는 webpack 을 이용해 완전한 base template를 통해서 개발하는 방법과 emscripten으로 target 언어를 rust로 지정해 빌드하는 방법 이렇게 두 가지 중 후자만 살펴 보도록 하겠습니다.

이번에 참조한 문서는 https://github.com/raphamorim/wasm-and-rust 입니다.

## 1. rust 설치
  - rustup 설치
  <pre><code>
  $ curl https://sh.rustup.rs -sSf | sh
  </code></pre>

  - 설치 후에 path 추가
  <pre><code>
  $ source $HOME/.cargo/env
  </code></pre>

만약 rust가 이미 설치 되어 있다면 apt-get remove rustc 로 설치 된 rust를 지우고 다시 설치해야 됩니다.

- rust up 설정
<pre><code>
rustup default stable
rustup target add wasm32-unknown-emscripten
</code></pre>

## 2. emscripten 설치
<pre><code>
curl https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-portable.tar.gz | tar -zxv -C ~/
cd ~/emsdk-portable
./emsdk update
./emsdk install sdk-incoming-64bit
./emsdk activate sdk-incoming-64bit
</code></pre>
또는
<pre><code>
git clone https://github.com/juj/emsdk.git
cd emsdk
./emsdk install latest
./emsdk activate latest
source ./emsdk_env.sh
</code></pre>
이후에
$ emcc -v 로 설치 되어 있는지 확인
<pre><code>
emcc (Emscripten gcc/clang-like replacement + linker emulating GNU ld) 1.38.20
clang version 6.0.1  (emscripten 1.38.20 : 1.38.20)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /home/jungjik.lee/dev/emscripten/emsdk/clang/e1.38.20_64bit
Found candidate GCC installation: /usr/lib/gcc/i686-linux-gnu/5
Found candidate GCC installation: /usr/lib/gcc/i686-linux-gnu/5.4.0
Found candidate GCC installation: /usr/lib/gcc/i686-linux-gnu/6
Found candidate GCC installation: /usr/lib/gcc/i686-linux-gnu/6.0.0
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/5
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/5.4.0
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/6
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/6.0.0
Selected GCC installation: /usr/lib/gcc/x86_64-linux-gnu/5.4.0
Candidate multilib: .;@m64
Candidate multilib: 32;@m32
Candidate multilib: x32;@mx32
Selected multilib: .;@m64
shared:INFO: (Emscripten: Running sanity checks)
</code></pre>

## 3. Project 생성
<pre><code>
cargo init wasm-demo --bin && rustup override set stable
</code></pre>
main.rs 파일의 코드를 아래와 같은 예제코드로 변경
<pre><code>
let greetings = ["Hello", "Hola", "Bonjour",
                "Ciao", "こんにちは", "안녕하세요",
                "Cześć", "Olá", "Здравствуйте",
                "Chào bạn", "您好", "Hallo",
                "Hej", "Ahoj", "سلام","สวัสดี"];

for (num, greeting) in greetings.iter().enumerate() {
  print!("{} : ", greeting);
    match num {
    0 => println!("This code is editable and runnable!"),
    1 => println!("¡Este código es editable y ejecutable!"),
    2 => println!("Ce code est modifiable et exécutable !"),
    3 => println!("Questo codice è modificabile ed eseguibile!"),
    4 => println!("このコードは編集して実行出来ます！"),
    5 => println!("여기에서 코드를 수정하고 실행할 수 있습니다!"),
    6 => println!("Ten kod można edytować oraz uruchomić!"),
    7 => println!("Este código é editável e executável!"),
    8 => println!("Этот код можно отредактировать и запустить!"),
    9 => println!("Bạn có thể edit và run code trực tiếp!"),
    10 => println!("这段代码是可以编辑并且能够运行的！"),
    11 => println!("Dieser Code kann bearbeitet und ausgeführt werden!"),
    12 => println!("Den här koden kan redigeras och köras!"),
    13 => println!("Tento kód můžete upravit a spustit"),
    14 => println!("این کد قابلیت ویرایش و اجرا دارد!"),
    15 => println!("โค้ดนี้สามารถแก้ไขได้และรันได้"),
    _ => {},
    }
  }
}
</code></pre>
## 4. Compile rust code

cargo build --target=wasm32-unknown-emscripten --release

## 5. Load wasm file
site 폴더를 만들고 거기에 index.html 파일을 만든 다음 아래와 같이 html 코드 작성,
그리고 compile 된 wasm_demo.js 를 site.js로 변경 후 브라우저에서 index.html 파일
열면 아래와 같이 실행 된 결과를 볼 수 있습니다.
<pre><code>
<&zwj;!DOCTYPE html>
<&zwj;html lang="en">
<&zwj;head>
  <&zwj;meta charset="UTF-8">
  <&zwj;title>Wasm/Rust<&zwj;/title>
  <&zwj;script>
    // This is read and used by `site.js`
    var Module = {
      wasmBinaryFile: "wasm_demo.wasm"
    }
  <&zwj;/script>
  <&zwj;script src="site.js"><&zwj;/script>
<&zwj;/head>
<&zwj;body><&zwj;/body>
<&zwj;/html>
</code></pre>

## 6. 참고 자료
그리고 마자막으로 찾은 rust/wasm의 다른 자료들 입니다.
- [https://github.com/raphamorim/wasm-and-rust](https://github.com/raphamorim/wasm-and-rust)
- [https://rustwasm.github.io/book/](https://rustwasm.github.io/book/)
- [https://kripken.github.io/blog/binaryen/2018/04/18/rust-emscripten.html](https://kripken.github.io/blog/binaryen/2018/04/18/rust-emscripten.html)
- [https://developer.mozilla.org/ko/docs/WebAssembly](https://developer.mozilla.org/ko/docs/WebAssembly)
- [https://wasdk.github.io/WasmFiddle/](https://wasdk.github.io/WasmFiddle/)
- [https://github.com/mdn/webassembly-examples](https://github.com/mdn/webassembly-examples)


# Emscripten WebAssembly

## emscripten 설치 및 hello world 출력하기.
<pre><code>
git clone https://github.com/juj/emsdk.git
cd emsdk
git pull
./emsdk install latest
./emsdk activate latest
source ./emsdk_env.sh
</code></pre>
emcc -v 헀을 때, 아래와 같이 나오면 정상.
<pre><code>
emcc (Emscripten gcc/clang-like replacement + linker emulating GNU ld) 1.38.21

clang version 6.0.1  (emscripten 1.38.21 : 1.38.21)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /mnt/f/dev/emscripten/emsdk/clang/e1.38.21_64bit
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/5
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/5.4.0
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/6
Found candidate GCC installation: /usr/lib/gcc/x86_64-linux-gnu/6.0.0
Selected GCC installation: /usr/lib/gcc/x86_64-linux-gnu/5.4.0
Candidate multilib: .;@m64
Selected multilib: .;@m64
shared:INFO: (Emscripten: Running sanity checks)
shared:WARNING: java does not seem to exist, required for closure compiler, which is optional (define JAVA in /home/fnwinter_linux/.emscripten if you want it)
shared:WARNING: closure compiler will not be available
</code></pre>

## hello_world.c 소스 코드 파일
<pre><code>
#include <&zwj;stdio.h>

int main() {
  printf("hello, world!\n");
  return 0;
}
</code></pre>

위 코드를 emcc hello_world.c 파일로 컴파일 하면 a.out.js 이 나오고, node a.out.js 실행하면 아래처럼 출력이 됨
<pre><code>
hello, world!s
</code></pre>
또는 emcc hello_world.c -out hello_world.html 로 컴파일하면 아래 처럼 html 파일이 하나 생기는데, 브라우저에서 실행하면 아래와 같이 나옴.

---
layout: post
title: "라즈베리파이 피코 프로젝터"
author: "jungjik.lee"
categories: article
tags: [raspberry pi, pico, projector, dlp, evm 2000]
---

# :cherries: 시작하기 전에
 - 집에서 놀고 있는 Raspberry pi 4가 하나 있어서 이걸로 뭐 할만한게 있을까 하다가 우연히 찾게 된 링크
 [link](http://frederickvandenbosch.be/?p=2948)
 - 이걸 만들면 잼있겠다 싶어서 시작, 이번 포스트는 만들면서 삽질한 걸 정리해 볼려고 합니다.

# 시작하기
## 부품
  - 라즈베리파이 4, 또는 3 Model B
  - DLP® LightCrafter™ Display 2000 Evaluation Module [link](https://www.ti.com/store/ti/en/p/product/?p=DLPDLCR2000EVM)
  - 점퍼 케이블 (10cm 짜리로 F/F, M/F) [link](https://www.devicemart.co.kr/goods/view?no=1328410) [link](https://www.devicemart.co.kr/goods/view?no=1328408)
  - 황동 서포터 [link](https://www.devicemart.co.kr/goods/view?no=1360715)
  - 5V 3A 아답터 [link](https://www.devicemart.co.kr/goods/view?no=12233453)

## 주문
  - DLP는 구매 대행 해주는 곳이 있었는데 그냥 직접 TI 사이트에서 구매 하였습니다.
  - 공홈에서 13만원 정도 했는데, 배송비 포함해서 다른 곳보다 오히려 저렴했습니다.
    ![shipping](https://fnwinter.github.io/assets/img/projector/shipping.JPG)
  - 배송은 DHL로 왔는데 배송이 지금 미국 사정 때문에 그런지 예상 날짜 보다 많이 늦게 왔고, 심지어 배송 완료 되었는데 실제 배송이 안되었고, 게다가 송장 번호도 달라서 애 먹었습니다.
  - 나머지 부품은 그냥 디바이스 마트에서 주문했습니다.

## 조립
   - 첨부한 사진 처럼 조립하면 됩니다. 간단 간단.
     ![assemble](https://fnwinter.github.io/assets/img/projector/real.jpg)
   - 점퍼 케이블을 연결하는 걸 좀 조심해야 되지만, 술 먹고 하는게 아닌 이상 어렵지 않습니다.
     ![pin](https://fnwinter.github.io/assets/img/projector/pin.png)
   - 아래 그림은 라즈베리 핀의 설명, 라즈베리파이의 3번 핀이 P1 의 27번 핀 VSYNC 에 연결하라는 뜻입니다.
     ![rasp_pin](https://fnwinter.github.io/assets/img/projector/rasp_pin.png)

# 삽질 기록, 라즈베리파이 설정하기
## 라즈베리파이 OS 다운로드
  - https://www.raspberrypi.com/software/ 여기서 OS를 다운로드 합니다.
  - Micro SD 카드에 OS를 Write 합니다.
    ![OS DOWNLOAD](https://fnwinter.github.io/assets/img/projector/OS_download.JPG)

## HDMI 와 키보드를 연결 후 setting을 시작 합니다.
  - sudo apt-get full-upgrade
  - sudo raspi-config
  - Interface Options에서 enable I2C 를 선택함, 동일하게 enable ssh 를 실행함
    ![setting](https://fnwinter.github.io/assets/img/projector/raspberry-config.JPG)
    ![setting2](https://fnwinter.github.io/assets/img/projector/i2c.JPG)
  - wifi 연결 후 터미널에서 ifconfig를 실행해 주소 알아 두기
    - 우선 wifi를 연결하고 그 다음 부터는 putty로 연결합니다.
    - hdmi 가 연결 된 상태에서는 가끔 i2c 버스 번호가 바뀌는 것 같아서 그냥 이후 작업은 hdmi 연결 안하고 작업 합니다.
    - putty로 연결할 때 ID 는 pi이고 PASSWORD는 시작할 때 정의해 놓은 비번 입니다.

## Display 설정
  - 아래 텍스트를 /boot/config.txt 파일 마지막에 추가함
  - sudo mousepad /boot/config.txt 로 읽어서 마지막에 추가
  <pre><code>
  dtoverlay=i2c-gpio,bus=2,i2c_gpio_sda=23,i2c_gpio_scl=24,i2c_gpio_delay_us=2

  dtoverlay=dpi18
  overscan_left=0
  overscan_right=0
  overscan_top=0
  overscan_bottom=0
  framebuffer_width=864
  framebuffer_height=480

  enable_dpi_lcd=1

  display_default_lcd=1

  dpi_group=2
  dpi_mode=87

  dpi_output_format=458773
  dpi_timings=864 0 0 0 12 480 0 2 3 9 0 0 0 60 1 24883200 3
  </code></pre>
  - 부팅 시에 실행 될 수 있도록 아래의 명령어 /etc/rc.local 파일에 저장
  - sudo mousepad /etc/rc.local
  - exit 0 명령어 이전에 추가
  <pre><code>
  sudo i2cset -y 2 0x1b 0x0c 0x00 0x00 0x00 0x15 i
  sudo i2cset -y 2 0x1b 0x0b 0x00 0x00 0x00 0x00 i
  </code></pre>
  - 만약 안되면, sudo i2cdetect -y 2 해서 i2c 연결이 잘 되었는지 확인해 볼 필요가 있음

# 프로그램 설치
## Netflix
  - sudo apt-get install libwidevinecdm0

## SteamLink
  - sudo apt-get install steamlink

## 한글 지원
  - sudo apt install -y fonts-unfonts-core

# 실제 동작 화면
  - ![steamlink](https://fnwinter.github.io/assets/img/projector/steam.jpg)
  - ![movie](https://fnwinter.github.io/assets/img/projector/movie.jpg)
  - 문제점
    - 아직 화면 떨림이 있다. 프레임 수를 낮춰 볼까 한다.
    - RBP 3에서는 3A 면 충분하다고 했는데, 실제 Netflix 돌리면 전력이 부족하다고 뜬다. 하지만 계속 재생은 된다.

# 참고 링크
  - [참고 link1](https://e2e.ti.com/support/dlp-products-group/dlp/f/dlp-products-forum/850392/dlpdlcr2000evm-resolution-problem-settings-with-i2c-and-raspberry-pi/3155530#3155530)
  - [참고 link2](https://www.element14.com/community/roadTestReviews/2682/l/dlp-pico-display-projector-evm-beaglebone-black-review?utm_source=pocket_mylist)
  - [라즈베리 파이 문서 link](https://wikidocs.net/3281?utm_source=pocket_mylist)

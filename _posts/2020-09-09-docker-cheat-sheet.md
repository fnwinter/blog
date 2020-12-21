---
layout: post
title: "Docker Cheat sheet"
author: "jungjik.lee"
categories: article
tags: [docker]
---

Docker Cheat sheet

## 1. Install
---
이전 docker 삭제
<pre><code>
$ sudo apt-get remove docker docker-engine docker.io containerd runc
</code></pre>

새로 설치
~~~shell
$ sudo apt-get update

$ sudo apt-get install &#92;
    apt-transport-https &#92;
    ca-certificates &#92;
    curl &#92;
    gnupg-agent &#92;
    software-properties-common

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

$ sudo apt-key fingerprint 0EBFCD88
pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid           [ unknown] Docker Release (CE deb) docker@docker.com
sub   rsa4096 2017-02-22 [S]

$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

$ sudo apt-get update

$ sudo apt-get install docker-ce docker-ce-cli containerd.io
~~~

## 2. 이미지 만들기
---
https://docs.docker.com/engine/reference/builder/

파일 이름이 Dockerfile 이어야 함.
파일을 작성하고, "docker build ." 실행해 주면 됨.
<pre><code>
FROM 기본 이미지
MAINTAINER (deprecated)

COPY Local Container 파일 복사
ADD Local Container 파일 추가
- COPY와 같지만 정규식으로 복수 파일들을 복사 가능
- tar 압축 파일일 경우 Container path에 압축 풀기
=> ADD hom* /my_dir/

RUN 프로그램 실행
CMD shell 통해서 실행하고 싶지 않을 경우 사용
ENTRYPOINT 컨테이너 시작 시 프로그램 실행
=> ENTRYPOINT ["top", "-b"]

WORKDIR 작업 폴더 설정
ENV KEY VALUE 환경 변수 설정

EXPOSE 8080 => 노출 할 port 번호 8080
VOLUME ["/var/www"] => mount 할 path ("/var/www") 설정
</code></pre>

## 3. 명령어
---
<pre><code>
컨테이너 시작
$ sudo docker start CONTAINER

컨테이너 종료
$ sudo docker stop CONTAINER

모든 컨테이너 종료
$ sudo docker stop $(sudo docker ps -a -q)

컨테이너 이미지 빌드
(Working path에 Dockerfile 존재, 태그 : -t tag_name)
$ sudo docker build . -t tag_name

모든 컨테이너 이미지 삭제
$ sudo docker rmi -f $(sudo docker images -a -q)
$ sudo docker container prune

컨테이너의 /bin/bash 실행
$ sudo docker run -it /bin/bash

실행 중인 컨테이너 보기
$ sudo docker ps

Kill 메시지 보내기
$ sudo docker kill CONTAINER
</code></pre>

## 4. 컴퓨터 부팅 후 자동 시작
---
<pre><code>
$ cd /etc/systemd/system
$ sudo echo "
[Unit]
Description=my_service Service
After=docker.service
Requires=docker.service

[Service]
TimeoutStartSec=0
Restart=always
ExecStart=/usr/bin/docker start [CONTAINER]

[Install]
WantedBy=multi-user.target
" > my_service

서비스 등록
$ sudo systemctl enable my_service

서비스 시작
$ sudo service start my_service

서비스 종료
$ sudo service stop my_service
</code></pre>

## 5. Image 실행
---

이미지 실행을 위한 추가 옵션
https://docs.docker.com/engine/reference/commandline/run/

### 5.1 Volume mapping
도커와 볼륨 연결하기
<pre><code>
$ sudo docker run -v [HOST_PATH]:[DOCKER_PATH] CONTAINER
</code></pre>

### 5.2. Port bind
도커 이미지 만들 때, EXPOSE PORT_NO 가 있어야 함.
<pre><code>
$ sudo docker run -p 127.0.0.1:80:8080 nginx:latest
$ sudo docker run -p 127.0.0.1:[HOST_PORT]:[CONTAINER_PORT] nginx:latest
</code></pre>
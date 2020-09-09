Docker Cheat sheet
===

## 1. Install
---
이전 docker 삭제
<pre>
<code>
$ sudo apt-get remove docker docker-engine docker.io containerd runc
</code>
</pre>

새로 설치
<pre>
<code>
$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo apt-key fingerprint 0EBFCD88
pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
sub   rsa4096 2017-02-22 [S]
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
</code>
</pre>

## 2. 이미지 만들기
---

## 3. 명령어
---

## 4. 자동 시작
---
<pre>
<code>
$ cd /etc/systemd/system
$ touch my_service
```
[Unit]
Description=my_service Service
After=docker.service
Requires=docker.service

[Service]
TimeoutStartSec=0
Restart=always
ExecStart=/usr/bin/docker start <process_name>

[Install]
WantedBy=multi-user.target
```
$ sudo systemctl enable my_service
서비스 시작
$ sudo service start my_service
서비스 종료
$ sudo service stop my_service
</code>
</pre>

## 5. Volume mount
---

## 6. Port bind
---

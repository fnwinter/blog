---
layout: post
title: "python virtualenv"
author: "jungjik.lee"
categories: article
tags: [python, virtualenv]
---

## virtualenv 설치
~~~shell
pip install virtualenv
~~~

## venv activate/deactivate
- 환경 설치
~~~shell
python -m virtualenv venv
~~~

- Windows
~~~shell
venv\Scripts\activate.bat
venv\Scripts\deactivate.bat
~~~

- Linux
~~~shell
source ./venv/script/activate
source ./venv/script/deactivate
~~~

## Freeze packages
~~~shell
pip freeze > requirements.txt
~~~

## Install packages
~~~shell
pip install -r requirements.txt
~~~
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
~~~shell
python -m virtualenv venv

Windows
  venv\Scripts\activate.bat
  venv\Scripts\deactivate.bat

Linux
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
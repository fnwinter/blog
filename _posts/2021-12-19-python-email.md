---
layout: post
title: "send email by python via gmail"
author: "jungjik.lee"
categories: article
tags: [python, email]
---

# :email: python으로 email 보내기 via gmail
- 여기에 아주 잘 정리 되어 있다. 굳이 또 정리할 필요가 없지만, 그래도 짧게 코드 정리 해 본다.
  - link : [https://s-engineer.tistory.com/234](https://s-engineer.tistory.com/234)
  - python tutorial link : [https://docs.python.org/ko/3/library/smtplib.html](https://docs.python.org/ko/3/library/smtplib.html)
- Step
  1. 중요한 건 Gmail Setting에서 IMAP을 켜고,
  2. Google Account로 가서 보안 탭 > Google에 로그인 > 앱 비밀번호를 선택하고,
  3. 메일 > Windows 컴퓨터 선택, 생성 버튼 누름.
  4. 생성 된 비밀번호(16자리)를 python code에서 비밀번호 대신에 넣은 것.
- code
<pre><code>

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_URL = "smtp.gmail.com"
SMTP_PORT = 465

class EMail(object):
  sender_email = "fnwinter@gmail.com"
  receiver_email = "fnwinter@gmail.com"
  password = "" # google app password
  title = ""
  text = ""
  html = ""

  def __init__(self, receiver = None):
    self.message = MIMEMultipart("alternative")
    self.message["Subject"] = self.title
    self.message["From"] = self.sender_email
    self.message["To"] = self.receiver_email
    if receiver:
      self.receiver_email = receiver

  def set_title(self, title):
    self.title = title

  def set_text(self, text):
    self.text = text

  def set_html(self, html):
    self.html = html

  def send_mail(self):
    part1, part2 = None, None
    if self.text:
      part1 = MIMEText(self.text, "plain")
      self.message.attach(part1)
    if self.html:
      part2 = MIMEText(self.html, "html")
      self.message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_URL, SMTP_PORT, context=context) as server:
        server.login(self.sender_email, self.password)
        server.sendmail(
            self.sender_email, self.receiver_email, self.message.as_string()
        )
        server.quit()
</code></pre>

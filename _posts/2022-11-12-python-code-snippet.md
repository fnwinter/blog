---
layout: post
title: "python code snippet"
author: "jungjik.lee"
categories: article
tags: [python, telegrambot, yfinance]
---

# yahoo finance에서 KRW 환율 정보 얻어오기

## yfinance 설치
- pip install yfinance

## yfiance code
<pre><code>import yfinance as yf
krw = yf.Ticker("KRW=X")
exchange_rate = krw.info.get('bid')
</code></pre>

# telegram bot 으로 message 보내기
<pre><code>import time
import telegram
TOKEN = "YOUR_TOKEN"
CHAT_ID = "1234567890"

bot = telegram.Bot(TOKEN)
while True:
    time.sleep(1)
    updates = bot.getUpdates()
    if updates:
        for u in updates:
            print(u.message.chat_id)
            print(u)
    bot.sendMessage(chat_id = CHAT_ID, text="저는 봇입니다.")
</code></pre>
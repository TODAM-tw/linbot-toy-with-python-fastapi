# -*- coding: utf-8 -*-
'''
Create Date: 2024/04/01
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import uvicorn
import os

from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = FastAPI()

_ = load_dotenv(find_dotenv())
line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.post("/callback")
async def callback(request: Request):
    signature = request.headers['X-Line-Signature']

    body = await request.body()
    body = body.decode('utf-8')

    with open('./logs/event.log', 'a') as f:
        f.write(body)
        f.write('\n')

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return JSONResponse(status_code=400, content={"message": "Invalid signature"})

    return JSONResponse(status_code=200, content={"message": "OK"})


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )
    except Exception as e:
        print(e)


def main() -> None:
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8080,
        reload=True,
    )


if __name__ == '__main__':
    main()

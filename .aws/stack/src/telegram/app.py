import os
import logging
import requests
from dataclasses import dataclass
# from dynamo.table import *


def handler(event, context):
    if type(context).__name__ == "FakeLambdaContext":
        logging.info("get test event:")
        logging.info(event)
        return {
            'statusCode': 200
        }
    message = event['body']
    chat_id = message['message']['chat']['id']
    reply = message['message']['text']

    tg = TelegramHandler()
    tg.send_message(chat_id, reply)
    return {
        'statusCode': 200
    }


class TelegramHandler:

    def __init__(self):
        self._bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
        self._base_url = f"https://api.telegram.org/bot{self._bot_token}"

    @property
    def bot_token(self) -> str:
        return self._bot_token

    @property
    def base_url(self) -> str:
        return self._base_url

    def send_message(self, chat_id: str, text: str) -> None:
        final_text = f"You said: {text}"
        url = f"{self.base_url}/sendMessage?text={final_text}&chat_id={chat_id}"
        requests.get(url)

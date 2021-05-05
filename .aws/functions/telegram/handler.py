import os
from telegram.client import Telegram


def handler(event, context):
    return


class TelegramHandler(Telegram):

    def __init__(self, api_id: int, api_hash: str, phone: str, database_encryption_key: str):
        super(TelegramHandler, self).__init__(api_id, api_hash, phone, database_encryption_key)
        self.login()
        self._chat_id = os.environ["TELEGRAM_CHAT_ID"]

    @property
    def chat_id(self) -> str:
        return self._chat_id

    def subscribe(self, ticker_code: str):
        return

    def unsubscribe(self, ticker_code: str):
        return

    def ask_for_permission(self):
        return

    def list_subscription(self):
        return

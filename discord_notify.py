import requests
import os
from datetime import datetime
from position_manager import (
    load_position
)
from dotenv import load_dotenv

#===============================
# 機密情報の読み込み
#
# .envファイル
#===============================

load_dotenv()
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
DISCORD_ALERT_WEBHOOK = os.getenv("DISCORD_ALERT_WEBHOOK")
DISCORD_ENTRY_OR_CLOSE_WEBHOOK = os.getenv("DISCORD_ENTRY_OR_CLOSE_WEBHOOK")

#===============================
# 基本関数
#
#
#===============================
def send_discord(webhook_url, message):

    requests.post(
        webhook_url,
        json={
            "content": message
        }
    )

#===============================
# 以下
# 色々あります。
#
#===============================

# プログラム起動確認通知
def notify_startup(message):

    now = datetime.now()
    send_discord(
        DISCORD_WEBHOOK, f"🟢 BOT START | {now:%Y-%m-%d %H:%M} | {message}"
    )

# トレード通知　新規エントリ、決済(損切、利確)
def send_trade_message(message):

    now = datetime.now()

    send_discord(
        DISCORD_ENTRY_OR_CLOSE_WEBHOOK,
        f"{now:%m-%d %H:%M} | {message}"
    )

# 異常時通知 注文エラーなど。
def send_alert(message):

    now = datetime.now()

    send_discord(
        DISCORD_ALERT_WEBHOOK,
        f"🚨 {now:%m-%d %H:%M} | {message}"
    )


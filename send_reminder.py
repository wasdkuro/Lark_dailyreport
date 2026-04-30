import requests, os
from datetime import datetime

WEBHOOK_URL = os.environ["LARK_WEBHOOK_URL"]

def send_reminder():
    today = datetime.now().strftime("%Y年%m月%d日")
    message = {
        "msg_type": "text",
        "content": {
            "text": (
                f"【日報提出リマインド】📋\n"
                f"日付：{today}\n"
                f"─────────────────\n"
                f"本日の日報を提出してください。\n"
                f"期限：19:00まで"
            )
        }
    }
    resp = requests.post(WEBHOOK_URL, json=message, timeout=10)
    print(f"Status: {resp.status_code}, Body: {resp.text}")

if __name__ == "__main__":
    send_reminder()

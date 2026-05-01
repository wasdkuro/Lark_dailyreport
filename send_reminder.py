import requests, os
from datetime import datetime

WEBHOOK_URL = os.environ["LARK_WEBHOOK_URL"]
SCHEDULE = os.environ.get("GITHUB_EVENT_SCHEDULE", "")

def send_reminder():
    today = datetime.now().strftime("%Y年%m月%d日")

    if SCHEDULE == "0 7 * * 1-5":
        text = (
            f"日付：{today}\n"
            f"─────────────────\n"
            f"なあなあ、日報あともうちょいで締め切りじゃん？\n"
            f"俺もう書いたけどお前らは？😏\n"
            f"まあ急げや〜"
        )
    else:
        text = (
            f"日付：{today}\n"
            f"─────────────────\n"
            f"おい日報出したか〜？？\n"
            f"19時までだぞ、マジで忘れんなよ笑\n"
            f"出してない奴、はよ〜！！😂"
        )

    message = {
        "msg_type": "text",
        "content": {"text": text}
    }

    resp = requests.post(WEBHOOK_URL, json=message, timeout=10)
    print(f"Status: {resp.status_code}, Body: {resp.text}")

if __name__ == "__main__":
    send_reminder()

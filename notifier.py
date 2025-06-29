# notifier.py

import os
from datetime import datetime

LOG_PATH = "logs/notify.log"

def notify(message: str, level: str = "INFO"):
    """
    通知メッセージを出力し、ログにも記録する。
    :param message: 通知内容
    :param level: ログレベル（例：INFO, WARNING, ERROR）
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] [{level}] {message}"
    print(full_message)
    
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(full_message + "\n")

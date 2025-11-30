import os
import json
from datetime import datetime

class Logger:
    def __init__(self, log_dir):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def save(self, message, tokens, config, token_prices):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}.json"
        full_path = os.path.join(self.log_dir, filename)

        data = {
            "messages": message,
            "tokens": tokens,
            "config": {
                "model": config.model,
                "api_key_present": config.api_key is not None
            },
            "token_prices": {
                "input_price_per_million": token_prices["input"],
                "output_price_per_million": token_prices["output"]
            }
        }

        with open(full_path, "w", encoding="utf-8") as f:
            json.dumps(data, f, indent=4, ensure_ascii=False)
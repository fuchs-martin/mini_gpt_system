from openai import OpenAI

class Client:
    def __init__(self, config):
        self.client = OpenAI(api_key=config.api_key)
        self.model = config.model

    def send(self, messages, tools=None):
        if tools is None:
            return self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
        else:
            return self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools,
                tool_choice="auto"
            )
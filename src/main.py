from src.config import Config
from src.message_store import MessageStore
from src.tools import Tools
from src.client import Client
from src.tokens import Tokens
from src.agent import Agent
from src.logger import Logger

def main():
    config = Config()
    store = MessageStore()
    tools = Tools()
    client = Client(config)
    tokens = Tokens()
    logger = Logger("logs/conversations")
    agent = Agent(client, store, tools, tokens)

    print("MINI GPT SYSTEM")
    print("----------------")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            tokens.print_summary()
            logger.save(
                store.get_all_messages(),
                tokens.to_dict(),
                config,
                {
                    "input": tokens.INPUT_PRICE,
                    "output": tokens.OUTPUT_PRICE
                }
            )
            break

        answer = agent.proces(user_input)
        print("Assistant: ", answer)

if __name__ == "__main__":
    main()
from config import Config
from message_store import MessageStore
from tools import Tools
from client import Client
from tokens import Tokens
from agent import Agent
from logger import Logger

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
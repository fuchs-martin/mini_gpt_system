# Mini ChatGPT System  
A modular, function-calling driven chatbot backend built with the OpenAI API.  
This project demonstrates clean architecture design, LLM orchestration, conversational memory, tool execution, and token accounting within a CLI-based chatbot.

---

## Features

### Function Calling (Tools)
The system automatically detects when the model wants to execute a tool and handles it through a fully dynamic Python registry.

**Available tools:**
- `add_numbers(x, y)`
- `reverse_text(text)`
- `get_current_time()`
- `get_weather(city)`
- `get_random_number(min, max)`

### Conversational Memory
All messages are stored with roles:
- `system`  
- `user`  
- `assistant`  
- `tool`

Structured exactly as required by OpenAI’s Chat Completion API.

### Modular Architecture
The project is structured as a clean Python package:

src/  
├── agent.py # LLM orchestration (core logic)  
├── client.py # OpenAI API wrapper  
├── config.py # environment & model configuration  
├── logger.py # logging conversations to JSON  
├── main.py # CLI entry point  
├── message_store.py # conversation state  
├── tokens.py # token & cost tracking  
└── tools.py # function-calling registry

### Token Tracking & Cost Calculation
Every request logs:
- prompt tokens
- completion tokens
- total tokens
- input/output cost
- session total cost

Displayed automatically upon exit/quit.

### Conversation Logging
Each session is saved to:

logs/conversations/`<timestamp>`.json

The file includes:
- full message history  
- tool call traces  
- model configuration  
- token usage and cost metrics  

---

## Demo (CLI Example)

MINI GPT SYSTEM
`----------------`
You: write hello  
Assistant:  Hello! How can I assist you today?

You: What's the weather in Paris?  
Assistant:  The current weather in Paris is 15°C with rainy conditions.

You: reverse apple  
Assistant:  The reverse of "apple" is "elppa".

You: quit

==== SESSION TOKEN SUMMARY ====  
Total input tokens: 788  
Total output tokens: 62  
Total tokens: 850  
`-----------------------------------`  
Total session cost: 0.000155$  
`=================================`

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/fuchs-martin/mini_gpt_system
cd mini_gpt_system
```
### 2. Create virtual environment and install dependencies
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Configure environment variables
Create .env:  
OPENAI_API_KEY=sk-xxxxxxx  
**Usage**  
Run the system via module mode:
```
python3 -m src.main
```
**Architecture Overview**  
flowchart TD

A[User Input] --> B[MessageStore]  
B --> C[Agent]  
C --> D[OpenAI Client]  
D --> E[Model Response]  

E --> |Tool Call| F[Tools Registry]  
F --> G[Execute Python Function]  
G --> H[Result to Model]  
H --> C

E --> |Normal Response| I[Assistant Message]  
I --> B

**License**  
This project is licensed under the MIT License, allowing free use, modification, and distribution while preserving attribution.

**Author**  
Developed by Martin Fuchs  
Python & AI Engineering
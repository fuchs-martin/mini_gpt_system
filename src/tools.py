import json
import random
from datetime import datetime

class Tools:
    def __init__(self):
        self.registry = {
            "get_wheather": self.get_weather,
            "add_numbers": self.add_numbers,
            "get_current_time": self.get_current_time,
            "reverse_text": self.reverse_text,
            "get_random_number": self.get_random_number,
        }

        self.schemas = [

            # add_numbers
            {
                "type": "function",
                "function": {
                    "name": "add_numbers",
                    "description": "Add two numbers together.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "x": {"type": "number"},
                            "y": {"type": "number"}
                        },
                        "required": ["x", "y"]
                    }
                }
            },

            # reverse_text
            {
                "type": "function",
                "function": {
                    "name": "reverse_text",
                    "description": "Reverse a piece of text.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"}
                        },
                        "required": ["text"]
                    }
                }
            },

            # get_current_time
            {
                "type": "function",
                "function": {
                    "name": "get_current_time",
                    "description": "Return the current date and time.",
                    "parameters": {
                        "type": "object",
                        "properties": {},  # no arguments
                        "required": []
                    }
                }
            },

            # get_weather
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Return simulated weather data for a given city.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string"}
                        },
                        "required": ["city"]
                    }
                }
            },

            # get_random_number
            {
                "type": "function",
                "function": {
                    "name": "get_random_number",
                    "description": "Return a random number between min and max.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "min": {"type": "integer"},
                            "max": {"type": "integer"}
                        },
                        "required": ["min", "max"]
                    }
                }
            }
        ]
    
    def get_schemas(self):
        return self.schemas
    
    def handle_tool(self, tool_name, tool_arg):
        if tool_name not in self.registry:
            raise ValueError(f"Unknnown tool: {tool_name}")
        
        if isinstance(tool_arg, str):
            args = json.loads(tool_arg)
        else:
            args = tool_arg
        
        result = self.registry[tool_name](**args)
        return json.dumps(result)
    
    def add_numbers(self, x, y):
        return x + y
    
    def get_weather(self, city):
        weather_data = {
            "temperature": random.randint(-20, 35),
            "conditions": random.choice(["sunny", "cloudy", "rainy", "storm"]),
            "city": city
        }
        return weather_data
    
    def reverse_text(self, text):
        return text[::-1]
    
    def get_current_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_random_number(self, min, max):
        return random.randint(int(min), int(max))
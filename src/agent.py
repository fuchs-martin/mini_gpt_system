import json

class Agent:
    def __init__(self, client, store, tools, tokens):
        self.client = client
        self.store = store
        self.tools = tools
        self.tokens = tokens
    
    def process(self, user_input):
        self.store.add("user", user_input)

        try:
            response = self.client.send(
                messages=self.store.get_all_messages(),
                tools=self.tools.get_schemas()
            )
        except Exception as e:
            error_msg = f"Error contacting the model: {str(e)}"
            self.store.add("assistant", error_msg)
            return error_msg
        
        self.tokens.add_usage(response.usage, label="input_completion")

        tool_calls = response.choices[0].message.tool_calls
        if not tool_calls:
            answer = response.choices[0].message.content
            self.store.add("assistant", answer)
            return answer
        
        call = tool_calls[0]
        tool_name = call.function.name
        tool_args = call.function.arguments

        try:
            result = self.tools.handle_tool(tool_name, tool_args)
        except Exception as e:
            error_msg = f"Tool execution failed: {str(e)}"
            self.store.add_tool_message(call.id, json.dumps({"error": error_msg}))
            return error_msg
        
        assistant_message = {
            "role": "assistant",
            "content": "",
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": tool_name,
                        "arguments": tool_args
                    }
                }
            ]
        }

        self.store.add(assistant_message)
        self.store.add_tool_message(call.id, result)

        try:
            response2 = self.client.send(
                messages=self.store.get_all_messages()
            )
        except Exception as e:
            error_msg = f"Error after tool execution: {str(e)}"
            self.store.add("assistant", error_msg)
            return error_msg
        
        self.tokens.add_usage(response2.usage, label="tool_followup")

        answer = response2.choices[0].message.content
        self.store.add("assistant", answer)
        return answer
class MessageStore:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant in a CLI application called Mini GPT System."
            }
        ]
    
    def add(self, role_or_message, content=None):
        if isinstance(role_or_message, dict):
            self.messages.append(role_or_message)
            return
        
        self.messages.append({
            "role": role_or_message,
            "content": content
        })
    
    def add_tool_message(self, call_id, content):
        self.messages.append({
            "role": "tool",
            "tool_call_id": call_id,
            "content": content
        })
    
    def get_all_messages(self):
        return self.messages
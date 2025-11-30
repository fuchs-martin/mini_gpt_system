class Tokens:
    def __init__(self):
        self.INPUT_PRICE = 0.15
        self.OUTPUT_PRICE = 0.60

        self.usage_history = []
    
    def add_usage(self, usage, label="request"):
        entry = {
            "label": label,
            "prompt_tokens": usage.prompt_tokens,
            "completion_tokens": usage.completion_tokens,
            "total_tokens": usage.total_tokens,
            "input_cost": (usage.prompt_tokens / 1_000_000) * self.INPUT_PRICE,
            "output_cost": (usage.completion_tokens / 1_000_000) * self.OUTPUT_PRICE,
        }
        entry["total_cost"] = entry["input_cost"] + entry["output_cost"]

        self.usage_history.append(entry)
    
    def get_session_totals(self):
        total_prompt = sum(u["prompt_tokens"] for u in self.usage_history)
        total_completion = sum(u["completion_tokens"] for u in self.usage_history)
        total_tokens = sum(u["total_tokens"] for u in self.usage_history)
        total_cost = sum(u["total_cost"] for u in self.usage_history)

        return {
            "prompt_tokens": total_prompt,
            "completion_tokens": total_completion,
            "total_tokens": total_tokens,
            "total_cost": total_cost
        }
    
    def print_summary(self):
        totals = self.get_session_totals()
        print("\n==== SESSION TOKEN SUMMARY ====")
        print(f"Total input tokens: {totals['prompt_tokens']}")
        print(f"Total output tokens: {totals['completion_tokens']}")
        print(f"Total tokens: {totals['total_tokens']}")
        print("-----------------------------------")
        print(f"Total session cost: {totals['total_cost']:.6f}$")
        print("=================================\n")
    
    def to_dict(self):
        return {
            "usage_history": self.usage_history,
            "session_totals": self.get_session_totals()
        }
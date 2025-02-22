#summarise an input text
from .agent_base import AgentBase

class SummarizeTool(AgentBase):
    def __init__(self, name="SummarizeTool", max_retries=3, verbose=True):
        super().__init__(name, max_retries, verbose)
    
    def execute(self, text):
        messages = [    
            {
                "role": "system", 
                "content": "You are an AI assistant that summarizes the given text:"
            },
            {
                "role": "user", 
                "content": (
                    "Please provide a concise summary of the following text:\n"
                    f"{text}\n\Summary:"
                )
            }
        ]
        summary = self.call_openai(messages, max_tokens=100)
        return summary
    
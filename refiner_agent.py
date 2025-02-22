from .agent_base import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self, name="RefinerAgent", max_retries=3, verbose=True):
        super().__init__(name, max_retries, verbose)
    
    def execute(self, draft):
        messages = [    
            {
                "role": "system", 
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant that refines and enhances articles for clarity, coherence, and readability."
                    }
                ]
            },
            {
                "role": "user", 
                "content": [
                    {
                        "type": "text",
                        "text": "Refine and enhance the following article\n\n"f"{draft}\n\nRefined Article:"
                    },
                ]
            }
        ]
        refined_text = self.call_openai(messages=messages, temperature=0.3, max_tokens=100)
        return refined_text
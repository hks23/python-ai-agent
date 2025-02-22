from .agent_base import AgentBase

class WriteArticleTool(AgentBase):
    def __init__(self, name="WriteArticleTool", max_retries=3, verbose=True):
        super().__init__(name, max_retries, verbose)
    
    def execute(self, title,outline=None):
        system_message = "You are an AI assistant that writes an article based on the given title and outline"
        user_content = f"write a research article based on the following title and outline:\nTitle: {title}\n"
        if outline:
            user_content += f"Outline:\n {outline}\n\n"
        user_content += f"Article:\n"


        messages = [    
            {
                "role": "system", 
                "content": system_message
            },
            {
                "role": "user", 
                "content": user_content
            }
        ]
        article = self.call_openai(messages, max_tokens=100)
        return article
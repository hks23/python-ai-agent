from .agent_base import AgentBase

class SummarizeValidatorAgent(AgentBase):
    def __init__(self, name="SummarizeValidatorAgent", max_retries=3, verbose=True):
        super().__init__(name, max_retries, verbose)
    
    def execute(self, original_text, summary):
        system_message = "You are an expert AI assistant that validates the summarization of medical data by checking the removal of PHI"
        user_content = (
            "Given the original data and sanitized data, verify that all the PHI has been removed.\n"
            "Provide a brief analysis and rate the summarization from 1 to 10, 10 being the highest.\n"
            f"Original text: {original_text}\n"
            f"Sanitized Data: {summary}\n"
            "Validation"
        ) 
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]

        validation = self.call_openai(messages, max_tokens=100)
        return validation
from .agent_base    import AgentBase    

class WriteArticleValidatorAgent(AgentBase):
    def __init__(self, name="WriteArticleValidatorAgent", max_retries=3, verbose=True):
        super().__init__(name, max_retries, verbose)

    def execute(self, topic, article):
        system_message = "You are an AI assistant that validates the given article for factual accuracy, coherence, and readability."
        user_content = (
            "Given the following article, validate its factual accuracy, coherence, and readability Provide a brief analysis and rate the article from 1 to 10, 10 being the highest."
            f"Topic: {topic}\n\n"
            f"Article: {article}\n\n"
            "Validation"
        )

        messages =[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}

        ]
        validation = self.call_openai(messages, max_tokens=100)
        return validation
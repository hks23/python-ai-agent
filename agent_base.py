import openai
from abc import ABC, abstractmethod
from loguru import logger
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI() # This is the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")

class AgentBase(ABC):
    def __init__(self, name, max_retries=3, verbose=True):
        self.name = name
        self.verbose = verbose
        self.max_retries = max_retries

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_openai(self, messages, temperature=0.7, max_tokens=100):
        response = None
        retries = 0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"Calling OpenAI API with messages: {messages}")
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                return response.choices[0].message.content
            except Exception as e:
                retries += 1
                logger.error(f"OpenAI API call failed: {e}")
                if retries >= self.max_retries:
                    raise
                logger.info(f"Retrying... {retries}/{self.max_retries}")
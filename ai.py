
from openai import OpenAI

class AiServices:
    def __init__(self,apiKey:str,modelLink:str):
        self.apiKey = apiKey
        self.modelLink = modelLink
        self.client :OpenAI

    def setup(self):
        self.client = OpenAI(
            base_url=self.modelLink,
            api_key=self.apiKey
        )

    def Ask(self,input:str):
        responses = self.client.chat.completions.create(
            model="qwen/qwen3.8-flash",
            messages=[
                {
                    "role": "user",
                    "content": f"{input}"
                }
            ],
            max_tokens=1000,
            extra_body={
                "reasoning": {
                "enabled": True
                }
            }

        )

        return responses
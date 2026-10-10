
from openai import OpenAI

from schema import AiResponseSchema

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

        return AiResponseSchema(
            question=input,
            response=responses.choices[0].message.content
        )



#-------------------TESTING---------------------------
# obj = AiServices(
#     apiKey=
#     modelLink=
# )
# obj.setup()
# response = obj.Ask("Who is the founder of Google ")

# print(response)


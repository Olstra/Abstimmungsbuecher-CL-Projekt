import json
import logging
from dataclasses import asdict

import requests

from src.DTOs.openAiRequestDTO import ChatRequestDTO

logging.basicConfig(level=logging.INFO)


class OpenaiModel:
    """
    Class for interacting with openai API.
    Define prompt through 'set_messages()'.
    Get Answer through 'answer_query()'
    """
    URL = "https://api.openai.com/v1/chat/completions"
    TEST_PROMPT = "Hi, how are you?"
    API_KEY = "TODO"

    def __init__(self):

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }

        self.data = ChatRequestDTO(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'please set messages!'"}],
            temperature=0.2
        )

    def set_model(self, model_name):
        self.data.model = model_name

    def set_messages(self, prompt, new_role="user"):
        self.data.messages = [{"role": new_role, "content": prompt}]

    def set_temperature(self, temperature):
        self.data.temperature = temperature

    def get_prompt(self):
        return self.data.messages[0]["content"]

    def make_request(self):
        return requests.post(self.URL, headers=self.headers, data=json.dumps(asdict(self.data)))

    def answer_query(self):
        response = self.make_request()
        response_code = str(response.status_code)
        if response_code != '200':
            logging.error(f'Error while making request: {response_code}\nResponse: {response.json()}')
            return

        response_content = response.json()['choices'][0]['message']['content']

        logging.info(f'Successfully requested answer from API. Response was: {response_content}')

        return response_content

    def test_question(self, text: str) -> str:
        prompt = f'{self.TEST_PROMPT}: {text}'
        self.set_messages(prompt)
        return self.answer_query()


if __name__ == '__main__':
    model = OpenaiModel()
    example_text = "TODO"
    answer = model.test_question(example_text)
    print(answer)

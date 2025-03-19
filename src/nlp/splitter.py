import nltk
import spacy
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

from src.config import config_instance


class SentenceSplitter:

    def __init__(self):
        # TODO: how to not hard-code lang names?
        self.language_map = {
            'DE': "de_dep_news_trf",
            'FR': "fr_dep_news_trf",
            'IT': "it_core_news_lg",
            'RM': "it_core_news_lg"
        }

    def split_into_sentences(self, text: str, language: str) -> list[str]:
        sentences = []
        language_to_load = self.language_map.get(language)

        if language_to_load is None:
            raise ValueError(f"Invalid language: '{language}'")

        nlp = spacy.load(language_to_load)
        doc = nlp(text)
        for sentence in doc.sents:
            sentences.append(str(sentence).strip())

        return sentences

    @staticmethod
    def split_into_sentences_nltk(text: str) -> list[str]:
        return nltk.sent_tokenize(text)

    @staticmethod
    def split_into_sentences_openai(text: str) -> list[str]:
        model = ChatOpenAI(model="gpt-4", api_key=config_instance.gpt_api_key)
        messages = [
            SystemMessage(content="Split this input text into sentences. Output should be a list of sentences"),
            HumanMessage(content=text),
        ]
        result = model.invoke(messages).content
        return result

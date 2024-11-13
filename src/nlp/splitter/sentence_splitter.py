import nltk
import spacy
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

from src.common.ch_languages import ch_langs
from src.config import config_instance


class SentenceSplitter:
    # TODO: refactor a la PDFReader
    # TODO: make private?
    openai_api_key: str = config_instance.gpt_api_key

    def __init__(self):
        self.language_map = {
            ch_langs.DE: "de_dep_news_trf",
            ch_langs.FR: "fr_dep_news_trf",
            ch_langs.IT: "it_core_news_lg",
            ch_langs.RM: "it_core_news_lg"
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
    def split_into_sentences_openai(self, text: str) -> list[str]:
        model = ChatOpenAI(model="gpt-4", api_key=self.openai_api_key)
        messages = [
            SystemMessage(content="Split this input text into sentences. Output should be a list of sentences"),
            HumanMessage(content=text),
        ]
        result = model.invoke(messages).content
        return result

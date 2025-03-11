from sklearn.metrics.pairwise import cosine_similarity

from src.common.ch_languages import ch_langs
from src.model import sentenceEmbeddings
from src.model.CHSentencesLists import CHSentencesLists
from src.model.sentenceEmbeddings import SentenceEmbedding
from src.nlp.embedder.swissbert import SwissbertEmbedder


class SentenceAlignerCosine:
    def __init__(self, base_lang=ch_langs.RM):
        self.base_lang = base_lang
        self.all_embeddings = {}
        self.embedder = SwissbertEmbedder()

    def align_sentences(self, all_sentences: CHSentencesLists) -> CHSentencesLists:
        # TODO: vorwissen benutzen, sätze sind immer der Reiehe nach, 1. satz muss nicht mit letztem satz aligniert werden etc.
        for lang in ch_langs.__dict__.values():
            # TODO: line too long, make normal loop instead of list comprh.
            self.all_embeddings[lang] = [SentenceEmbedding(s, self.embedder.generate_embeddings(s, lang)) for s in all_sentences.get[lang]]

        # Initialize result with sentences from the base language (RM)
        result = CHSentencesLists(get={self.base_lang: [obj.sentence for obj in self.all_embeddings[self.base_lang]]})

        other_langs = self._ch_langs_without_base_lang()
        for lang in other_langs.values():
            result.get[lang] = self._align_sentences_bilingual(self.all_embeddings[self.base_lang], self.all_embeddings[lang])

        return result

    @staticmethod
    def _align_sentences_bilingual(base_lang_embeddings: list[sentenceEmbeddings], other_lang_embeddings: list[sentenceEmbeddings]) -> list[str]:
        result = []

        for base_lang_obj in base_lang_embeddings:
            max_score = 0
            most_similar = None
            for other_lang_obj in other_lang_embeddings:
                score = cosine_similarity(base_lang_obj.embeddings, other_lang_obj.embeddings)[0][0]
                if score > max_score:
                    most_similar = other_lang_obj
                    max_score = score
            result.append(most_similar.sentence)

        return result

    def _ch_langs_without_base_lang(self) -> dict:
        ch_langs_copy = ch_langs.__dict__.copy()
        key_to_remove = [key for key, value in ch_langs_copy.items() if value == self.base_lang][0]
        ch_langs_copy.__delitem__(key_to_remove)

        return ch_langs_copy

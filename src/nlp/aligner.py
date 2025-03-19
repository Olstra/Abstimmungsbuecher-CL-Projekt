from sklearn.metrics.pairwise import cosine_similarity

from src.common.ch_languages import CH_LANG_CODES
from src.model import sentenceEmbeddings
from src.utils.create_sentences_per_lang_container import create_sentences_per_lang_container


class Aligner:
    def __init__(self, base_lang='RM'):
        self.base_lang = base_lang

    def align_sentences(self, all_embeddings: dict) -> list[list[str]]:
        # TODO: vorwissen benutzen, sätze sind immer der Reiehe nach, 1. satz muss nicht mit letztem satz aligniert werden etc.

        result = create_sentences_per_lang_container()

        # Initialize result with sentences in the base language
        for obj in all_embeddings[self.base_lang]:
            result[self.base_lang].append(obj.sentence)

        for lang, lang_code in self._get_langs_without_base_lang().items():
            aligned_sentences = self._align_sentences_bilingual(all_embeddings[self.base_lang], all_embeddings[lang])
            result[lang].append(aligned_sentences)

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

    def _get_langs_without_base_lang(self) -> dict:
        return {key: val for key, val in CH_LANG_CODES.items() if val != self.base_lang}

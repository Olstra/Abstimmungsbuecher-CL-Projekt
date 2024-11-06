from webbrowser import Error

from sklearn.metrics.pairwise import cosine_similarity

from src.swissbert.generate_sentence_embeddings import generate_sentence_embedding
from src.swissbert.models.sentenceEmbeddings import SentenceEmbedding


def align_sentences(lang_1: str, sentences_lang_1: list[str], lang_2: str, sentences_lang_2: list[str]):
    # TODO: what do if arrays have different total nr of sentences?
    embeddings_lang_1 = [SentenceEmbedding(s, generate_sentence_embedding(s, language=lang_1)) for s in sentences_lang_1]
    embeddings_lang_2 = [SentenceEmbedding(s, generate_sentence_embedding(s, language=lang_2)) for s in sentences_lang_2]

    if len(embeddings_lang_1) != len(embeddings_lang_2):
        raise Error(f"Not same length. {lang_1}: {len(embeddings_lang_1)}, {lang_2}: {len(embeddings_lang_2)}")

    result = []
    for lang_1_obj in embeddings_lang_1:
        max_score = 0
        most_similar = None
        for lang_2_obj in embeddings_lang_2:
            score = cosine_similarity(lang_1_obj.embeddings, lang_2_obj.embeddings)[0][0]
            if score > max_score:
                most_similar = lang_2_obj
                max_score = score
        result.append([lang_1_obj.sentence, most_similar.sentence])
        # TODO?: remove from list to avoid duplicates?
        # embeddings_lang_2.pop(most_similar)

    return result

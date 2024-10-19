import torch
from transformers import AutoModel, AutoTokenizer
from sklearn.metrics.pairwise import cosine_similarity

from src.constants import CH_LANG_RM, CH_LANG_DE, SWISSBERT_MODEL_NAME
from src.swissbert.sentences_embedder import generate_sentence_embedding

# Load SwissBERT model and tokenizer
model = AutoModel.from_pretrained(SWISSBERT_MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(SWISSBERT_MODEL_NAME)


def align_sentences(rm_sentences: list, de_sentences: list):
    rm_embeddings = []
    de_embeddings = []

    # Generate embeddings for RM and DE sentences
    for rm_sentence in rm_sentences:
        rm_embeddings.append(generate_sentence_embedding(rm_sentence, CH_LANG_RM))

    for de_sentence in de_sentences:
        de_embeddings.append(generate_sentence_embedding(de_sentence, CH_LANG_DE))

    # Convert embeddings to numpy for similarity calculation
    rm_embeddings = torch.stack(rm_embeddings).squeeze().numpy()
    de_embeddings = torch.stack(de_embeddings).squeeze().numpy()

    # Compute cosine similarity between every RM and DE sentence
    similarity_matrix = cosine_similarity(rm_embeddings, de_embeddings)

    # Find the best match for each RM sentence with DE sentences
    aligned_sentences = []
    for i, rm_sentence in enumerate(rm_sentences):
        best_match_idx = similarity_matrix[i].argmax()  # Get index of the best matching DE sentence
        best_match_score = similarity_matrix[i][best_match_idx]
        aligned_sentences.append((rm_sentence, de_sentences[best_match_idx], best_match_score))

    return aligned_sentences

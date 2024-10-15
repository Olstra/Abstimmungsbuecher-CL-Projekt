import re

import fitz
import nltk
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModelForMaskedLM, AutoModel, XLMRobertaTokenizer

#model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
#model = AutoModelForMaskedLM.from_pretrained("ZurichNLP/swissbert")

# Load SwissBERT model and tokenizer
model_name = "ZurichNLP/swissbert"
#tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModel.from_pretrained(model_name)


def extract_text(path: str):
    result = ""

    doc = fitz.open(path)

    for page in doc:
        result += page.get_text("text")

    return result


def clean_text(text: str):
    text = re.sub(r'[0-9%]+', '', text)
    return ' '.join(text.split())


def split_into_sentences(text: str):
    return nltk.sent_tokenize(text)


def align_sentences_cosine_old(german_sentences, romansh_sentences):

    german_embeddings = model.encode(german_sentences)
    romansh_embeddings = model.encode(romansh_sentences)

    similarity_matrix = cosine_similarity(german_embeddings, romansh_embeddings)

    # Find the best matching sentences
    aligned_sentences = []
    matched_romansh_indices = set()

    for i, german_sentence in enumerate(german_sentences):
        # Find the Romansh sentence with the highest similarity score
        most_similar_index = np.argmax(similarity_matrix[i])
        similarity_score = similarity_matrix[i][most_similar_index]

        # Avoid duplicate matching by ensuring each Romansh sentence is only used once
        if most_similar_index not in matched_romansh_indices:
            matched_romansh_indices.add(most_similar_index)
            aligned_sentences.append(
                f"German: {german_sentence}\nRomansh: {romansh_sentences[most_similar_index]}\nSimilarity: {similarity_score:.4f}\n"
            )

    return aligned_sentences


def embed_sentences(sentences):
    inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

    # Pass through the model to get the hidden states
    with torch.no_grad():
        outputs = model(**inputs)
        # We use the mean of the last hidden layer as sentence embeddings
        embeddings = outputs.last_hidden_state.mean(dim=1)

    return embeddings.numpy()


def align_sentences_cosine(german_sentences, romansh_sentences):
    model.set_default_language("de_CH")
    german_embeddings = embed_sentences(german_sentences)

    romansh_embeddings = embed_sentences(romansh_sentences)

    similarity_matrix = cosine_similarity(german_embeddings, romansh_embeddings)

    aligned_sentences = []
    matched_romansh_indices = set()

    for i, german_sentence in enumerate(german_sentences):
        # Find the Romansh sentence with the highest similarity score
        most_similar_index = np.argmax(similarity_matrix[i])
        similarity_score = similarity_matrix[i][most_similar_index]

        # Avoid duplicate matching by ensuring each Romansh sentence is only used once
        if most_similar_index not in matched_romansh_indices:
            matched_romansh_indices.add(most_similar_index)
            aligned_sentences.append(
                f"German: {german_sentence}\nRomansh: {romansh_sentences[most_similar_index]}\nSimilarity: {similarity_score:.4f}\n"
            )

    return aligned_sentences


if __name__ == "__main__":
    # DE
    test_path_de = "../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_DE_web.pdf"
    text_de = extract_text(test_path_de)
    cleaned_text_de = clean_text(text_de)
    sentences_de = split_into_sentences(cleaned_text_de)

    # RM
    test_path_rm = "../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_RM_web.pdf"
    text_rm = extract_text(test_path_rm)
    cleaned_text_rm = clean_text(text_rm)
    sentences_rm = split_into_sentences(cleaned_text_rm)

    #result = align_sentences_cosine(sentences_de, sentences_rm)
    #print(result)

    print(embed_sentences(sentences_de))

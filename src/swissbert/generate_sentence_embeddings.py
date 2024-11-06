import torch
from transformers import AutoModel, AutoTokenizer

from src.constants import SWISSBERT_MODEL_NAME

# Load swissBERT for sentence embeddings model
model = AutoModel.from_pretrained(SWISSBERT_MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(SWISSBERT_MODEL_NAME)


def generate_sentence_embedding(sentence, language):

    model.set_default_language(language)

    # # Set adapter to specified language
    # if "de" in language:
    #     model.set_default_language("de_CH")
    # if "fr" in language:
    #     model.set_default_language("fr_CH")
    # if "it" in language:
    #     model.set_default_language("it_CH")
    # if "rm" in language:
    #     model.set_default_language("rm_CH")

    # Tokenize input sentence
    inputs = tokenizer(sentence, padding=True, truncation=True, return_tensors="pt", max_length=512)

    # Take tokenized input and pass it through the model
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract sentence embeddings via mean pooling
    token_embeddings = outputs.last_hidden_state
    attention_mask = inputs['attention_mask'].unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * attention_mask, 1)
    sum_mask = torch.clamp(attention_mask.sum(1), min=1e-9)
    embedding = sum_embeddings / sum_mask

    return embedding

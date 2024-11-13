import torch

from transformers import AutoModel, AutoTokenizer


class SwissbertEmbedder:
    model_name: str = "jgrosjean-mathesis/sentence-swissbert"

    def __init__(self):
        self.model = AutoModel.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def generate_embeddings(self, sentence, language):
        self.model.set_default_language(language)

        # Tokenize input sentence
        inputs = self.tokenizer(sentence, padding=True, truncation=True, return_tensors="pt", max_length=512)

        # Take tokenized input and pass it through the model
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Extract sentence embeddings via mean pooling
        token_embeddings = outputs.last_hidden_state
        attention_mask = inputs['attention_mask'].unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * attention_mask, 1)
        sum_mask = torch.clamp(attention_mask.sum(1), min=1e-9)
        embedding = sum_embeddings / sum_mask

        return embedding
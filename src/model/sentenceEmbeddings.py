from dataclasses import dataclass

import torch


@dataclass
class SentenceEmbedding:
    sentence: str
    embeddings: torch.Tensor

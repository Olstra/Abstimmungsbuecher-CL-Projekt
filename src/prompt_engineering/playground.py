import fitz  # PyMuPDF
import nltk
import json
import re
from sentence_transformers import SentenceTransformer, util

# Download NLTK resources
nltk.download('punkt')


def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text


def split_and_clean_text(text):
    # Split into sentences
    sentences = nltk.sent_tokenize(text)

    # Clean sentences
    cleaned_sentences = []
    for sentence in sentences:
        # Remove numbers and special characters
        cleaned = re.sub(r'[^A-Za-zäöüÄÖÜß\s]', '', sentence)
        cleaned = cleaned.strip()
        if cleaned:
            cleaned_sentences.append(cleaned)
    return cleaned_sentences


def compute_cosine_similarity(sentences1, sentences2, model):
    # Encode sentences
    embeddings1 = model.encode(sentences1, convert_to_tensor=True)
    embeddings2 = model.encode(sentences2, convert_to_tensor=True)

    # Calculate cosine similarities
    cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
    return cosine_scores


def main():
    # Paths to your PDF files
    #pdf_path_rm = '../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_RM_web.pdf'
    pdf_path_de = '../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_DE_web.pdf'
    pdf_path_fr = '../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_FR_web.pdf'
    #pdf_path_it = 'path/to/italian.pdf'

    # Extract and clean text from PDFs
    texts = {
        #"rumansch": split_and_clean_text(extract_text_from_pdf(pdf_path_rm)),
        "german": split_and_clean_text(extract_text_from_pdf(pdf_path_de)),
        "french": split_and_clean_text(extract_text_from_pdf(pdf_path_fr)),
        #"italian": split_and_clean_text(extract_text_from_pdf(pdf_path_it))
    }

    # Initialize sentence transformer model
    model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

    # Compare each language with the others
    alignment_results = []
    for lang1, sentences1 in texts.items():
        for lang2, sentences2 in texts.items():
            if lang1 != lang2:
                cosine_scores = compute_cosine_similarity(sentences1, sentences2, model)
                for i, score in enumerate(cosine_scores):
                    for j, sim in enumerate(score):
                        alignment_results.append({
                            "lang1": lang1,
                            "sentence1": sentences1[i],
                            "lang2": lang2,
                            "sentence2": sentences2[j],
                            "similarity_score": sim.item()
                        })

    # Write results to JSON file
    output_path = 'results/aligned_sentences.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(alignment_results, f, ensure_ascii=False, indent=4)

    print(f"Alignment results saved to '{output_path}'.")


if __name__ == "__main__":
    main()

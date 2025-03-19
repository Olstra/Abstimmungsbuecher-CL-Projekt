from src.common.ch_languages import CH_LANG_CODES
from src.file_handling.text_extractor import extract_text_from_pdf
from src.file_handling.to_json_converter import write_to_json
from src.nlp.aligner import Aligner
from src.nlp.text_cleaner import TextCleaner
from src.nlp.splitter import SentenceSplitter
from src.nlp.embedder import Embedder


def main():

    # 1 page
    base_path = "data/test_samples/one_pagers/Seite_5-Erlaeuterungen_Juni"
    # 5 pages
    #base_path = "data/test_samples/five_pagers/Erste_5-Erlaeuterungen_Juni"
    # FULL pdfs
    #base_path = "data/pdf/Erlaeuterungen_Juni"

    data_paths = {
        lang: f"{base_path}_{lang}_web.pdf"
        for lang, lang_code in CH_LANG_CODES.items()
    }

    preprocessor = TextCleaner()
    splitter = SentenceSplitter()

    # main process
    sentences_by_lang = {}
    for lang, path in data_paths.items():
        text = preprocessor.preprocess(extract_text_from_pdf(path))
        sentences_by_lang[lang] = splitter.split_into_sentences(text, lang)

    embeddings = Embedder().generate_embeddings_for_all_langs(sentences_by_lang)

    result = Aligner().align_sentences(embeddings)

    for lang, lang_code in CH_LANG_CODES.items():
        write_to_json(result[lang], lang)


if __name__ == "__main__":
    #main()
    base_path = "data/test_samples/one_pagers/Seite_5-Erlaeuterungen_Juni"
    data_paths = {
        lang: f"{base_path}_{lang}_web.pdf"
        for lang, lang_code in CH_LANG_CODES.items()
    }
    for lang, path in data_paths.items():
        text = extract_text_from_pdf(path)
        print(text)
        print("=====================================")

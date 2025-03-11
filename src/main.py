from src.common.ch_languages import ch_langs
from src.document.pdf_reader import PDFReader
from src.file.to_json_converter import write_to_json
from src.model.CHSentencesLists import CHSentencesLists
from src.nlp.aligner.cosine_similarity import SentenceAlignerCosine
from src.nlp.preprocessor.preprocessor import Preprocessor
from src.nlp.splitter.sentence_splitter import SentenceSplitter


def main():

    # 1 page
    base_path = "data/test_samples/one_pagers/Seite_5-Erlaeuterungen_Juni"
    # 5 pages
    # base_path = "data/test_samples/five_pagers/Erste_5-Erlaeuterungen_Juni"
    # FULL pdfs
    # base_path = "data/pdf/Erlaeuterungen_Juni"

    data_paths = {
        lang_code: f"{base_path}_{lang}_web.pdf"
        for lang, lang_code in ch_langs.__dict__.items()
    }

    reader = PDFReader()
    preprocessor = Preprocessor()
    splitter = SentenceSplitter()

    sentences_by_lang = CHSentencesLists({
        lang: splitter.split_into_sentences(preprocessor.preprocess(reader.extract_text(path)), lang)
        for lang, path in data_paths.items()
    })

    result = SentenceAlignerCosine().align_sentences(sentences_by_lang)

    for lang in ch_langs.__dict__.values():
        write_to_json(result.get[lang], lang)


if __name__ == "__main__":
    main()

from src.common.ch_languages import ch_langs
from src.document.pdf_reader import PDFReader
from src.file.to_json_converter import write_to_json
from src.model.CHSentencesLists import CHSentencesLists
from src.nlp.aligner.cosine_similarity import SentenceAlignerCosine
from src.nlp.preprocessor.preprocessor import Preprocessor
from src.nlp.splitter.sentence_splitter import SentenceSplitter


def main():
    # define data to be used
    base_path = "Abstimmungsbuecher-CL-Projekt/data/test_samples"

    # One page sample
    one_page_path = "/one_pagers/Seite_5-Erlaeuterungen_Juni"
    de_data_path = f"{base_path}{one_page_path}_DE_web.pdf"
    rm_data_path = f"{base_path}{one_page_path}_RM_web.pdf"
    fr_data_path = f"{base_path}{one_page_path}_FR_web.pdf"
    it_data_path = f"{base_path}{one_page_path}_IT_web.pdf"

    # # 5 pages sample
    # five_pages_path = "/five_pagers/Erste_5-Erlaeuterungen_Juni"
    # de_data_path = f"{base_path}{five_pages_path}_DE_web.pdf"
    # rm_data_path = f"{base_path}{five_pages_path}_RM_web.pdf"
    # fr_data_path = f"{base_path}{five_pages_path}_FR_web.pdf"
    # it_data_path = f"{base_path}{five_pages_path}_IT_web.pdf"

    # # full pdfs
    # de_data_path = "../../abstimmungsbuecher/Erlaeuterungen_Juni_DE_web.pdf"
    # rm_data_path = "../../abstimmungsbuecher/Erlaeuterungen_Juni_RM_web.pdf"
    # fr_data_path = "../../abstimmungsbuecher/Erlaeuterungen_Juni_FR_web.pdf"
    # it_data_path = "../../abstimmungsbuecher/Erlaeuterungen_Juni_IT_web.pdf"

    pdf_reader = PDFReader()
    preprocessor = Preprocessor()
    de_text = preprocessor.preprocess(pdf_reader.extract_text(de_data_path))
    rm_text = preprocessor.preprocess(pdf_reader.extract_text(rm_data_path))
    fr_text = preprocessor.preprocess(pdf_reader.extract_text(fr_data_path))
    it_text = preprocessor.preprocess(pdf_reader.extract_text(it_data_path))

    splitter = SentenceSplitter()
    de_sentences = splitter.split_into_sentences(de_text, ch_langs.DE)
    rm_sentences = splitter.split_into_sentences(rm_text, ch_langs.RM)
    fr_sentences = splitter.split_into_sentences(fr_text, ch_langs.FR)
    it_sentences = splitter.split_into_sentences(it_text, ch_langs.IT)

    result = SentenceAlignerCosine().align_sentences(
        CHSentencesLists({
            ch_langs.DE: de_sentences,
            ch_langs.RM: rm_sentences,
            ch_langs.IT: it_sentences,
            ch_langs.FR: fr_sentences
        })
    )

    for lang in ch_langs.__dict__.values():
        write_to_json(result.get[lang], lang)


if __name__ == "__main__":
    main()

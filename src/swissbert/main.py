from src.constants import *
from src.swissbert.align_sentences import align_sentences
from src.util.extract_to_json import write_sentences_to_json
from src.util.parser import Parser


def main():
    parser = Parser()

    # define data to be used
    base_path = "../../test_data"

    # # One page sample
    # one_page_path = "/one_pagers/Seite_5-Erlaeuterungen_Juni"
    # de_data_path = f"{base_path}{one_page_path}_DE_web.pdf"
    # rm_data_path = f"{base_path}{one_page_path}_RM_web.pdf"
    # fr_data_path = f"{base_path}{one_page_path}_FR_web.pdf"
    # it_data_path = f"{base_path}{one_page_path}_IT_web.pdf"

    # 5 pages sample
    five_pages_path = "/five_pagers/Erste_5-Erlaeuterungen_Juni"
    de_data_path = f"{base_path}{five_pages_path}_DE_web.pdf"
    rm_data_path = f"{base_path}{five_pages_path}_RM_web.pdf"
    fr_data_path = f"{base_path}{five_pages_path}_FR_web.pdf"
    it_data_path = f"{base_path}{five_pages_path}_IT_web.pdf"

    # extract sentences
    de_sentences = parser.extract_text_from_pdf(de_data_path).clean_text().split_into_sentences()
    rm_sentences = parser.extract_text_from_pdf(rm_data_path).clean_text().split_into_sentences()
    fr_sentences = parser.extract_text_from_pdf(fr_data_path).clean_text().split_into_sentences()
    it_sentences = parser.extract_text_from_pdf(it_data_path).clean_text().split_into_sentences()

    # align sentences with help of cosine similarity
    result_de_rm = align_sentences(CH_DE, de_sentences, CH_RM, rm_sentences)
    write_sentences_to_json(result_de_rm, CH_DE, CH_RM)

    result_fr_it = align_sentences(CH_FR, fr_sentences, CH_IT, it_sentences)
    write_sentences_to_json(result_fr_it, CH_FR, CH_IT)


if __name__ == "__main__":
    main()

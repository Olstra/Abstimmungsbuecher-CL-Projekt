import unittest

from src.swissbert.align_sentences import align_sentences
from src.util.extract_to_json import write_sentences_to_json
from src.util.parser import Parser


class MyTestCase(unittest.TestCase):
    def test_align_de_and_rm(self):
        parser = Parser()

        # DE
        de_data_path = "../../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_DE_web.pdf"
        de_sentences = parser.extract_text_from_pdf(de_data_path).clean_text().split_into_sentences()

        # RM
        rm_data_path = "../../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_RM_web.pdf"
        rm_sentences = parser.extract_text_from_pdf(rm_data_path).clean_text().split_into_sentences()

        # FR
        fr_data_path = "../../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_FR_web.pdf"
        fr_sentences = parser.extract_text_from_pdf(fr_data_path).clean_text().split_into_sentences()

        # IT
        it_data_path = "../../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_IT_web.pdf"
        it_sentences = parser.extract_text_from_pdf(it_data_path).clean_text().split_into_sentences()

        result = align_sentences("de", de_sentences, "rm", rm_sentences)
        write_sentences_to_json(result, "de", "rm")

        result = align_sentences("fr", fr_sentences, "it", it_sentences)
        write_sentences_to_json(result, "fr", "it")


if __name__ == '__main__':
    unittest.main()

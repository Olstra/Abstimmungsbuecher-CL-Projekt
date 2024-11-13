"""
Documentation about layout algorithm:
https://pdfminersix.readthedocs.io/en/latest/topic/converting_pdf_to_text.html#layout-analysis-algorithm
"""

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LAParams


def extract_text_boxes(pdf_path: str) -> list[str]:
    laparams = LAParams()
    result = []

    for page_layout in extract_pages(pdf_path, laparams=laparams):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                result.append(element.get_text().strip())

    return result


if __name__ == "__main__":
    input_data_path = "../../../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_RM_web.pdf"
    output_path = "../results/result.json"
    result = extract_text_boxes(input_data_path)
    print(result)
